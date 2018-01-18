from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'classifier/index.html', context=context_dict)

def predictions(request):
    context_dict = {
        'prediction1_path': 'predictions/Acura-Integra_Type_R-2001_0.jpg',
        'prediction1_label': 'Top prediction',
        'prediction1_link': 'https://www.cars.com',

        'prediction2_path': 'predictions/Acura-Integra_Type_R-2001_1.jpg',
        'prediction2_label': 'Second prediction',
        'prediction2_link': 'https://www.cars.com',

        'prediction3_path': 'predictions/Acura-Integra_Type_R-2001_3.jpg',
        'prediction3_label': 'Third prediction',
        'prediction3_link': 'https://www.cars.com',
        }
    return render(request, 'classifier/predictions.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'classifier/about.html', context=context_dict)
