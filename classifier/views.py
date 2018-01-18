from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Classifying cars is awesome!'}
    return render(request, 'classifier/index.html', context=context_dict)

def results(request):
    return HttpResponse('This is the results page', )

def about(request):
    return HttpResponse('This is the About page')
