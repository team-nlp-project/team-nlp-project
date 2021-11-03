####### NLP MODELING MODULE #######

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

def X_and_y(train, validate, test, data_col, target):
    '''
    Takes in splits, column name for cleaned text, and column name for target and returns X and y for each split
    '''
    X_train = train[data_col]
    X_validate = validate[data_col]
    X_test = test[data_col]
    y_train = train[target]
    y_validate = validate[target]
    y_test = test[target]
    return X_train, X_validate, X_test, y_train, y_validate, y_test

def vectorize(vectorizer, X_train, X_validate, X_test, grams = (1,1)):
    '''
    Takes in vectorizer, X for each split, and n_grams argument for vectorizer and returns vectorized version of each split
    '''
    v = vectorizer(ngram_range=grams)
    X_bow_train = v.fit_transform(X_train)
    X_bow_validate = v.transform(X_validate)
    X_bow_test= v.transform(X_test)
    return X_bow_train, X_bow_validate, X_bow_test

def vectorize_best_words(vectorizer, X_train, X_validate, X_test, best_words, grams = (1,1)):
    '''
    Takes in vectorizer, X for each split, and n_grams and best_words argument for vectorizer and returns vectorized version of each split
    '''
    v = vectorizer(ngram_range=grams, vocabulary=best_words)
    X_bow_train = v.fit_transform(X_train)
    X_bow_validate = v.transform(X_validate)
    X_bow_test= v.transform(X_test)
    return X_bow_train, X_bow_validate, X_bow_test

def append_scores(X_bow_train, y_train, X_bow_validate, y_validate, model, model_name, metric_df):
    '''
    Take in X_bow and y for train and validate, model object, model name and metric df and append scores for that model
    '''
    model.fit(X_bow_train, y_train)
    train_score = model.score(X_bow_train, y_train)
    validate_score = model.score(X_bow_validate, y_validate)
    diff = validate_score - train_score
    model_dict = {'Model Name': model_name, 
                  'Train Accuracy': train_score, 
                  'Validate Accuracy':validate_score,
                  'Difference' : diff 
                 }
    metric_df = metric_df.append(model_dict, ignore_index = True)
    return metric_df