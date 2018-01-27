from django.apps import AppConfig

import os
import pickle

from keras import backend as K
from keras.models import model_from_json


FAST_TEST = True

BASE_DIR = os.path.join(
    os.path.expanduser('~'), 'Dropbox', 'projects',
    'cars', 'data', 'InceptionV3'
    )

WEIGHT_PATH = os.path.join(
    BASE_DIR,
    'InceptionV3_21_FT3_30_40.h5'
    )

JSON_PATH = os.path.join(
    BASE_DIR,
    'InceptionV3_21_FT3_30_40.json'
    )

LOOKUP_PATH = os.path.join(
    BASE_DIR,
    'I_15_lookup_dict.pkl'
    )

def load_model():
    """
    Initializes and loads pretrained weights into keras model to be used for predictions
    """
    with open(JSON_PATH, 'r') as json_file:
        loaded_model_json = json_file.read()
    json_model = model_from_json(loaded_model_json)
    json_model.load_weights(WEIGHT_PATH)

    return json_model

def load_lookup_dicto():
    """
    returns lookup_dictonary necessary to interpret keras model predictions
    """
    with open(LOOKUP_PATH, 'rb') as f:
        lookup_dicto = pickle.load(f)
    return lookup_dicto

class ClassifierConfig(AppConfig):
    name = 'classifier'
    def ready(self):
        
        global prediction_model
        global lookup_dicto
        global graph

        lookup_dicto = load_lookup_dicto()        
        if FAST_TEST:
            prediction_model = []
            graph = []
        else:
            prediction_model = load_model()
            prediction_model._make_predict_function()
            graph = K.get_session().graph
        
