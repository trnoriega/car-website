from django.apps import AppConfig
from keras import backend as K

from .algorithms import load_model, load_lookup_dicto


class ClassifierConfig(AppConfig):
    name = 'classifier'
    # def ready(self):
    #     global prediction_model
    #     global lookup_dicto
    #     global graph
    #     prediction_model = load_model()
    #     prediction_model._make_predict_function()
    #     graph = K.get_session().graph
    #     lookup_dicto = load_lookup_dicto()
