from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Opera

def home(request):
    opere = Opera.objects.all()
    return render(request, 'sitomuseo/home.html', {'opere': opere})

def detail(request, opera_id):
    opera = get_object_or_404(Opera, id=opera_id)
    return render(request, 'sitomuseo/dettaglio_opera.html', {'opera': opera})
    
def placeholder(request):
    return render(request,"placeholder.html")