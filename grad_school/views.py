from django.shortcuts import render


def index(request):
    return render(request, 'grad_school/index.html')


def about(request):
    return render(request, 'grad_school/about.html')


def main_project(request):
    return render(request, 'grad_school/main_project.html')


def static_dynamic(request):
    return render(request, 'grad_school/static_dynamic.html')


def dynamic_dynamic(request):
    return render(request, 'grad_school/dynamic_dynamic.html')


def simulation(request):
    return render(request, 'grad_school/simulation.html')

def mitos(request):
    return render(request, 'grad_school/mitos.html')
