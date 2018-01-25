import os

from django.shortcuts import render
from django.http import HttpResponse

from .algorithms import load_predictions # for production
# from .fast_algorithms import load_predictions # for fast testing
from .apps import prediction_model, lookup_dicto, graph
from .forms import InputImageForm
from cars.settings import MEDIA_DIR
from .models import Car



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
            with graph.as_default():
                prediction_labels = load_predictions(prediction_model, image_path, lookup_dicto)
            
            predictions_dict = {
                'image': image._name,
                'predictions' : [],
            }
            for label in prediction_labels:
                try:
                    c = Car.objects.get(label=label)
                except Exception as e:
                    print(e)
                prediction_items = {}
                prediction_items['path'] = 'predictions/' + label + '_0.jpg'
                prediction_items['make'] = c.make
                prediction_items['model'] = c.model
                prediction_items['year'] = c.year
                prediction_items['body'] = c.body_style
                prediction_items['url'] = c.url
                predictions_dict['predictions'].append(prediction_items)

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
