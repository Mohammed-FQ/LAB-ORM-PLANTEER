from django.urls import path
from . import views


app_name = 'plants'
urlpatterns = [
	path('', views.all_plants_view, name='all_plants'),
	path('add/', views.add_plant_view, name='add_plant'),
]