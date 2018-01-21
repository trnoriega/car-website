import os

from django.shortcuts import render
from django.http import HttpResponse

from .algorithms import top3_predictions, load_test_predictions_dict
# from .apps import prediction_model, lookup_dicto, graph #Comment out when testing memory light model
from .forms import InputImageForm
from cars.settings import MEDIA_DIR



def index(request):
    form = InputImageForm()
    if request.method == 'POST':
        form = InputImageForm(request.POST, request.FILES)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            image = form.cleaned_data['image']
            image_path = os.path.join(MEDIA_DIR, 'uploads', image._name)

            ###########################
            # PREDICTION HAPPENS HERE #
            ###########################
            # with graph.as_default():
            #     predictions_dict = top3_predictions(prediction_model, image_path, lookup_dicto)
            
            predictions_dict = load_test_predictions_dict()

            return predictions(request, predictions_dict)
        
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'classifier/index.html', context=context_dict)

def predictions(request, predictions_dict):
    return render(request, 'classifier/predictions.html', context=predictions_dict)

def about(request):
    context_dict = {}
    return render(request, 'classifier/about.html', context=context_dict)
