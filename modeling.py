####### NLP MODELING MODULE #######

import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

###################### Model Metrics Function ######################
def model_metrics(X, y, model, data_set = 'data_set'):
    """
    
    Takes in X , target as y, the model for testing, and the data_set(i.e. train, validate, test)\n
    Outputs a print list with the confusion matrix, classification report, confusion matrix, and the T/F +/- rate
   
   """
    score = model.score(X, y)
    matrix = confusion_matrix(y, model.predict(X))
    tpr = matrix[1,1] / (matrix[1,1] + matrix[1,0])
    fpr = matrix[0,1] / (matrix[0,1] + matrix[0,0])
    tnr = matrix[0,0] / (matrix[0,0] + matrix[0,1])
    fnr = matrix[1,0] / (matrix[1,1] + matrix[1,0])
    prc = matrix[1,1] / (matrix[1,1] + matrix[0,1])
    
    print(f'{data_set} accuracy score: {score:.2%}')
    print(f'{data_set} precision score {prc:.2%}')
    print(f'{data_set} recall score: {tpr:.2%}\n')
    class_report = classification_report(y, model.predict(X), zero_division=True)
    print('-------------------------------')
    print(f'classification report')
    print(class_report)
    print ('-------------------------------\n')
    print('confusion matrix')
    print(f'{matrix}\n')
    print(f'{data_set} model metrics')
    print('---------------------------------')
    print(f'True positive rate for the model is {tpr:.2%}')
    print(f'False positive rate for the model is  {fpr:.2%}')
    print(f'True negative rate for the model is {tnr:.2%}')
    print(f'False negative rate for the model is {fnr:.2%}\n')