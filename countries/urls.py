from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.countries, name='list_of_countries'),
    path('countries/id/', views.id, name='country_detail'),
]




