from django.http import HttpResponse


def home(request):
    return HttpResponse("Main page")

def countries(request):
    return HttpResponse("This is a list of countries of the world!")

def id(request):
    return HttpResponse('8')