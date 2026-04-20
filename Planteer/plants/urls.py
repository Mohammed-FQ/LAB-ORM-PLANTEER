from django.urls import path
from . import views


app_name = 'plants'
urlpatterns = [
	path('all/', views.all_plants_view, name='all_plants'),
	path('new/', views.add_plant_view, name='add_plant'),
	path('search/', views.search_view, name='search'),
	path('<int:pk>/detail/', views.plant_detail_view, name='plant_detail'),
	path('<int:pk>/update/', views.update_plant_view, name='update_plant'),
	path('<int:pk>/delete/', views.delete_plant_view, name='delete_plant'),
]