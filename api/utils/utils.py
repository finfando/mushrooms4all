import sys
import numpy as np
import pickle

def is_valid(payload, features):
    '''Checks for valid input for the model'''
    for i, v in payload.items():
        if i+'_'+v not in features:
            return 'Feature '+i+' or value '+v+' does not exist'
    return True

def preprocessing(payload, features):
    '''Convert variables provided in JSON into one hot encoding used for training

    Args:
        payload: payload received from request
    Returns:
        model_input: a 127 elements array
    '''
    features_values={}
    for f in features:
        features_values[f]=0
    for i, v in payload.items():
        features_values[i+'_'+v]=1
    model_input=np.array([list(features_values.values())])
    return model_input