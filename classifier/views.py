from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Classifying cars is awesome!'}
    return render(request, 'classifier/index.html', context=context_dict)
