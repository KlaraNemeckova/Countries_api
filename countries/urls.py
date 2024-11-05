from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.countries_list, name='list_of_countries'),
    path('countries/<int:id>/', views.country_detail, name='country_detail'),
]



