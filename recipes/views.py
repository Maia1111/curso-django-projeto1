from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': ' Rogério Maia'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': ' Rogério Maia'
    })
