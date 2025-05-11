from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Opera,Autore
from .models import Achievement

def home(request):
    opere = Opera.objects.all()
    return render(request, 'home.html', {'opere': opere})

def detail(request, opera_id):
    opera = get_object_or_404(Opera, id=opera_id)
    return render(request, 'detail.html', {'opera': opera})
    
def placeholder(request):
    return render(request,"placeholder.html")

def achievement(request):
    achievements = Achievement.objects.all()
    return render(request, 'achievement.html', {'achievement': achievements})

def detail_achiv(request, achievement_id):
    achievement = get_object_or_404(Achievement, id=achievement_id)
    return render(request, 'detail_achiv.html', {'achievement': achievement})

def user(request):
    return render(request,"user.html")
def index(request):
    return render (request,'index.html')
def lista_autori(request):
    autori = Autore.objects.all()
    return render(request, 'lista_autori.html', {'autori':autori})

def dettaglio_autore(request, pk):
    autore = get_object_or_404(Autore, pk=pk)
    return render(request, 'dettaglio_autore.html', {'autore': autore})
