from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.countries, name='countries'),
    path('countries/id/', views.id, name='id'),
]




