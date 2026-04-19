from django.shortcuts import redirect, render

from .forms import PlantForm
from .models import Plant

# Create your views here.
def all_plants_view(request):
	plants = Plant.objects.all().order_by('-created_at')
	return render(request, 'plants/all_plants.html', {'plants': plants})


def add_plant_view(request):
	if request.method == 'POST':
		form = PlantForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('plants:all_plants')
	else:
		form = PlantForm()

	return render(request, 'plants/add_plant.html', {'form': form})
