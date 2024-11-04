from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html") 

def countries(request):
    pass

def id(request):
    return render(request, "country_detail.html") 