from urllib import request

from django.shortcuts import render
from plants.models import Plant

# Create your views here.
def home_view(request):
    latest_plants = Plant.objects.all().order_by('-created_at')[:3]
    return render(request, 'main/home.html', {'latest_plants': latest_plants})
def base_view(request):
    return render(request, 'main/base.html')
    