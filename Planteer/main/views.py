from django.shortcuts import render
from plants.models import Plant
from .forms import ContactForm
from .models import Contact

# Create your views here.
def home_view(request):
    latest_plants = Plant.objects.all().order_by('-created_at')[:3]
    return render(request, 'main/home.html', {'latest_plants': latest_plants})

def contact_view(request):
    form = ContactForm()
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            form = ContactForm()
    return render(request, 'main/contact.html', {'form': form, 'submitted': submitted})

def contact_messages_view(request):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})
    