import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime
import numpy as np

def get_new_links():
    '''
    Scrapes links from page and filters out non-github links
    '''
    response = requests.get('https://www.theinsaneapp.com/2021/09/best-github-repository-for-machine-learning.html', headers={"user-agent": "Codeup DS"})
    soup = BeautifulSoup(response.text)
    links = [link.attrs['href'] for link in soup.select_one('.post-body').select('a')]
    github_links = [link for link in links if link.startswith('https://github.com')]
    today = strftime('%Y-%m-%d')
    np.save(f'github_links-{today}.npy', github_links)
    return github_links

def get_cached_links():
    '''
    Get list of cached links from local
    '''
    cached_links = np.load(f'github_links-2021-10-29.npy').tolist() # change this name to match file name in repo
    return cached_links