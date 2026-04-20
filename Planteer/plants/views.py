from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlantForm
from .models import Plant


def search_view(request):
	query = request.GET.get('q', '').strip()
	plants = Plant.objects.filter(name__icontains=query).order_by('-created_at') if query else Plant.objects.none()
	return render(request, 'plants/search.html', {'plants': plants, 'query': query})

# Create your views here.
def plant_detail_view(request, pk):
	plant = get_object_or_404(Plant, pk=pk)
	related = Plant.objects.filter(category=plant.category).exclude(pk=pk)[:3]
	return render(request, 'plants/plant_detail.html', {'plant': plant, 'related': related})


def all_plants_view(request):
	plants = Plant.objects.all().order_by('-created_at')
	category = request.GET.get('category', '')
	edible = request.GET.get('edible', '')
	if category:
		plants = plants.filter(category=category)
	if edible == 'true':
		plants = plants.filter(is_edible=True)
	categories = ['Fruit', 'Vegetable', 'Herb', 'Flower', 'Tree']
	return render(request, 'plants/all_plants.html', {
		'plants': plants,
		'active_category': category,
		'active_edible': edible,
		'categories': categories,
	})


def add_plant_view(request):
	if request.method == 'POST':
		form = PlantForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('plants:all_plants')
	else:
		form = PlantForm()

	return render(request, 'plants/add_plant.html', {'form': form})


def update_plant_view(request, pk):
	plant = get_object_or_404(Plant, pk=pk)
	if request.method == 'POST':
		form = PlantForm(request.POST, request.FILES, instance=plant)
		if form.is_valid():
			form.save()
			return redirect('plants:plant_detail', pk=plant.pk)
	else:
		form = PlantForm(instance=plant)

	return render(request, 'plants/update_plant.html', {'form': form, 'plant': plant})


def delete_plant_view(request, pk):
	plant = get_object_or_404(Plant, pk=pk)
	if request.method == 'POST':
		plant.delete()
		return redirect('plants:all_plants')
	return redirect('plants:plant_detail', pk=pk)
