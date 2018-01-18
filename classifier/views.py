from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputImageForm

def index(request):
    form = InputImageForm()
    if request.method == 'POST':
        form = InputImageForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            return predictions(request)
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'classifier/index.html', context=context_dict)

def predictions(request):
    context_dict = {
        'prediction1_path': 'predictions/Acura-Integra_Type_R-2001_0.jpg',
        'prediction1_label': 'Top prediction',
        'prediction1_link': 'https://www.cars.com',

        'prediction2_path': 'predictions/Acura-Integra_Type_R-2001_1.jpg',
        'prediction2_label': 'Second prediction',
        'prediction2_link': 'https://www.autotrader.com', # This one seems to have an easy search url

        'prediction3_path': 'predictions/Acura-Integra_Type_R-2001_3.jpg',
        'prediction3_label': 'Third prediction',
        'prediction3_link': 'https://www.carvana.com',
        }
    return render(request, 'classifier/predictions.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'classifier/about.html', context=context_dict)
