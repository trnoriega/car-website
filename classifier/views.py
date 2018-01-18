from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'classifier/index.html', context=context_dict)

def results(request):
    context_dict = {
        'result1_path': 'results/Acura-Integra_Type_R-2001_0.jpg',
        'result1_label': 'Top result',
        'result1_link': 'https://www.cars.com',

        'result2_path': 'results/Acura-Integra_Type_R-2001_1.jpg',
        'result2_label': 'Second result',
        'result2_link': 'https://www.cars.com',

        'result3_path': 'results/Acura-Integra_Type_R-2001_3.jpg',
        'result3_label': 'Third result',
        'result3_link': 'https://www.cars.com',
        }
    return render(request, 'classifier/results.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'classifier/about.html', context=context_dict)
