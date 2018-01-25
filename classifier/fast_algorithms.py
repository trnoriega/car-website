import pickle
import os

from keras.models import Sequential
from keras.layers import Dense

BASE_DIR = os.path.join(
    os.path.expanduser('~'), 'Dropbox', 'projects',
    'cars', 'data', 'InceptionV3'
    )

LOOKUP_PATH = os.path.join(
    BASE_DIR,
    'I_15_lookup_dict.pkl'
    )

TEST_LABELS = [
    'Aston_Martin-Martin_V8_Vantage_Convertible-2012',
    'Aston_Martin-Martin_Virage_Convertible-2012',
    'Aston_Martin-Martin_V8_Vantage_Coupe-2012',
    'Dodge-Ram_Pickup_3500_Quad_Cab-2009',
    'Ford-E_Series_Wagon_Van-2012',
]

def load_model():
    """
    Initializes and loads pretrained weights into keras model to be used for predictions
    """
    model = Sequential()
    model.add(Dense(2, input_shape = (2,2)))
    return model

def load_predictions(model, image_path, lookup_dicto):
    """
    Provides a static predictions dictionary to test the app
    without having to load the full keras model to memory each time the server starts
    """
    return TEST_LABELS

def load_lookup_dicto():
    """
    returns lookup_dictonary necessary to interpret keras model predictions
    """
    with open(LOOKUP_PATH, 'rb') as f:
        lookup_dicto = pickle.load(f)
    return lookup_dicto