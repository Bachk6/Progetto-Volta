from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Opera,Autore,Crossword
from .models import Achievement
from .forms import LoginForm, SignupForm
import json

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
    form_login = LoginForm()
    form_signup = SignupForm()
    return render(request, "user.html",{
        "form_login": form_login,
        "form_signup": form_signup
    })
    
def index(request):
    return render (request,'index.html')
def lista_autori(request):
    autori = Autore.objects.all()
    return render(request, 'lista_autori.html', {'autori':autori})

def dettaglio_autore(request, id):
    autore = get_object_or_404(Autore, pk=id)
    return render(request, 'dettaglio_autore.html', {'autore': autore})

def gioco(request,id):
    cross = get_object_or_404(Crossword,pk=id)
    mat = cross.matrix
    mat = json.dumps(mat)
    f = {'matrix':mat}
    return render(request,'gameFinal.html', {"cross":f})
