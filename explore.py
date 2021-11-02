####### NLP EXPLORE MODULE #######

import pandas as pd
import matplotlib.pyplot as plt

def plot_stacked_all(word_counts):
    '''
    Takes in word_counts df with an 'All' column and produces stacked bar chart for each category for top num_top words in all classes
    '''
    (word_counts.sort_values('All', ascending=False)
     .head(20)
     .apply(lambda row: row/row['All'], axis = 1)
     .drop(columns = 'All')
     .sort_values(by = 'JavaScript')
     .plot.barh(stacked = True, width = 1, ec = 'lightgrey')
    )
    plt.title('Proportion of Total Count for Each Class for 20 Most-Commonly Occuring Words')
    plt.legend(bbox_to_anchor= (1.03,1))
    plt.xlabel('Proportion')
    plt.ylabel('Word');
    
def plot_bar_all(word_counts):
    '''
    Takes in word_counts df with an 'All' column and produces bar chart for each category for top num_top words in all classes
    '''
    (word_counts.sort_values('All', ascending=False)
     .head(20)
     .apply(lambda row: row/row['All'], axis = 1)
     .drop(columns = 'All')
     .sort_values(by = 'JavaScript')
     .plot.barh(width=0.75)
    )
    plt.title('Proportion of Total Count for Each Class for 20 Most-Commonly Occuring Words')
    plt.legend(bbox_to_anchor= (1.03,1))
    plt.xlabel('Proportion')
    plt.ylabel('Word');

def plot_stacked_bar(word_counts, category, num_top = 20, cmap = None):
    '''
    Takes in word_counts df with an 'All' column and produces stacked bar chart for each category for top num_top words specified by category argument
    '''
    plt.figure(figsize=(16, 9))
    plt.rc('font', size=16)
    (word_counts.sort_values(by=category, ascending=False)
     .head(num_top)
     .apply(lambda row: row / row['All'], axis=1)
     .drop(columns='All')
     .sort_values(by=category)
     .plot.barh(stacked=True, width=1, ec='lightgrey', cmap = cmap, alpha = 1))
    plt.legend(bbox_to_anchor= (1.03,1))
    plt.title(f'Proportions of Most Commonly-Occuring {num_top} {category} Readme Words\n')
    plt.xlabel('Proportion')
    plt.ylabel('Word');
    # make tick labels display as percentages
    # plt.gca().xaxis.set_major_formatter(mpl.ticker.FuncFormatter('{:.0%}'.format))
    plt.show();

def plot_horizontal_bar(word_counts, category, num_top = 20, cmap = None):
    '''
    Takes in word_counts df with an 'All' column and produces bar chart for each category for top num_top words specified by category argument
    '''
    plt.figure(figsize=(16, 9))
    plt.rc('font', size=16)
    (word_counts.sort_values(by=category, ascending=False)
     .head(num_top)
     .apply(lambda row: row / row['All'], axis=1)
     .drop(columns='All')
     .sort_values(by=category)
     .plot.barh(width=0.75))
    plt.title(f'Proportions of Most Commonly-Occuring {num_top} {category} Readme Words\n')
    plt.xlabel('Proportion')
    plt.ylabel('Word')
    # make tick labels display as percentages
    # plt.gca().xaxis.set_major_formatter(mpl.ticker.FuncFormatter('{:.0%}'.format))
    plt.show();
    
