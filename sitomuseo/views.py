from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Opera
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