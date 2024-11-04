from django.http import HttpResponse
from django.shortcuts import render
from . models import Country


def home(request):
    return render(request, "home.html") 


def countries_list_html(request):
    countries = Country.objects.all()
    return render(request, 'countries_list.html')

def country_detail_html(request, id):
    return render(request, 'country_detail.html')
