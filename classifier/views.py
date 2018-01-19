import os

from django.shortcuts import render
from django.http import HttpResponse

from .algorithms import load_model, load_lookup_dicto, prepare_image, top3_predictions
from cars.settings import MEDIA_DIR
from .forms import InputImageForm


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
            model = load_model()
            lookup_dicto = load_lookup_dicto()
            predictions_dict = top3_predictions(model, image_path, lookup_dicto)
            
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
