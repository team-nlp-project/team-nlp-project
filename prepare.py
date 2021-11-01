####### NLP PREPARATION SCRIPT #######

import pandas as pd
import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split


def basic_clean(some_string):
    '''
    Takes in a string and makes all characters lowercased, normalizes unicode characters, and removes any character that is not a letter, number, ', or space
    '''
    some_string = some_string.lower()
    some_string = unicodedata.normalize('NFKD', some_string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    some_string = re.sub(r"[^a-z0-9'\s]", '', some_string)
    return some_string

def tokenize(some_string):
    '''
    Takes in a string and tokenizes it
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    some_string = tokenizer.tokenize(some_string, return_str = True)
    return some_string

def remove_stopwords(some_string, extra_words = [], exclude_words = []):
    '''
    Takes in a string and removes stopwords in nltk stopwords list, user can also pass list of words to add or remove from default list of stopwords
    '''
    stopword_list = stopwords.words('english')
    [stopword_list.append(word) for word in extra_words]
    [stopword_list.remove(word) for word in extra_words]
    words = some_string.split()
    filtered_words = [word for word in words if word not in stopword_list]
    some_string_without_stopwords = ' '.join(filtered_words)
    return some_string_without_stopwords

def lemmatize(some_string):
    '''
    Takes in a string and returns a string with all words lemmatized
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in some_string.split()]
    some_string_lemmatized = ' '.join(lemmas)
    return some_string_lemmatized

def stem(some_string):
    '''
    Takes in a string and returns a string with all words stemmed
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in some_string.split()]
    some_string_stemmed = ' '.join(stems)
    return some_string_stemmed

def prep_nlp(df, original_text_col = 'original', extra_words = [], exclude_words = []):
    '''
    Take in df with raw content, create new columns for cleaned content, stemmed content, and lemmatized content
    '''
    df['clean'] = df[original_text_col].apply(basic_clean).apply(tokenize).apply(remove_stopwords, extra_words, exclude_words)
    df['stemmed'] = df.clean.apply(stem)
    df['lemmatized'] = df.clean.apply(lemmatize)
    df = df.dropna()
    top4 = ['JavaScript', 'Java', 'Python', 'C++']
    df.language = df.language.apply(lambda x: 'Other' if x not in top4 else x)
    df = df[df.language != 'Other']
    return df

def split_readme(df):
    '''
    This function takes in a df and splits it into train, validate, and test dfs
    final proportions will be 60/20/20 for train/validate/test
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.language)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=123, stratify=train_validate.language)
    train_prop = train.shape[0] / df.shape[0]
    val_prop = validate.shape[0] / df.shape[0]
    test_prop = test.shape[0]/df.shape[0]
    print(f'Train Proportion: {train_prop:.2f} ({train.shape[0]} rows)\nValidate Proportion: {val_prop:.2f} ({validate.shape[0]} rows)\
    \nTest Proportion: {test_prop:.2f} ({test.shape[0]} rows)')
    return train, validate, test