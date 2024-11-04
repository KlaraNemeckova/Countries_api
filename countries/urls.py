from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.countries_list_html, name='list_of_countries'),
    path('countries/id/', views.country_detail_html, name='country_detail'),
]




