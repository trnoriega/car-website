from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'classifier/index.html', context=context_dict)

def results(request):
    context_dict = {
        'label1': 'Top result',
        'label2': 'Second result',
        'label3': 'third result',
        }
    return render(request, 'classifier/results.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'classifier/about.html', context=context_dict)
