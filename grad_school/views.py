from django.shortcuts import render


def index(request):
    return render(request, 'grad_school/index.html')


def about(request):
    return render(request, 'grad_school/about.html')


def main_project(request):
    return render(request, 'grad_school/main_project.html')