from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer, CountryCreateSerializer



def home(request):
    return render(request, "home.html") 
        

@api_view(['GET', 'POST'])
def countries_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        if request.accepted_renderer.format == 'html':
            return render(request, 'countries_list.html', {'countries': countries})

        # Jinak se vrátí JSON odpověď
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if isinstance(request.data, list): # zjistí, zda jsou vkládaná data seznam 
            serializer = CountryCreateSerializer(data=request.data, many=True)
        else:
            serializer = CountryCreateSerializer(data=request.data)
                                                                                                                          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, id):
    try:                                       # country = get_object_or_404(Country, pk=id) místo try except
        country = Country.objects.get(pk=id)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if request.accepted_renderer.format == 'html':
            return render(request, 'country_detail.html', {'country': country})

        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    





