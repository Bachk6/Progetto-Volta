from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Opera,Autore,Crossword,Utente
from .models import Achievement
from .forms import LoginForm, SignupForm
import json,os
from django.shortcuts import redirect
import hashlib

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
    msg=0
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        form_signup = SignupForm(request.POST)
        if form_signup.is_valid():
            user = form_signup.data['user_S']
            psw = form_signup.data['psw_S']
            hash = hashlib.sha256(psw.encode()).hexdigest()
            print(hash)
            lista = Utente.objects.filter(username=user)
            if len(lista) == 0:
                insert_list = [
                    Utente(username=user,hash=hash)
                ]
                Utente.objects.bulk_create(insert_list)
                msg=1
            else: msg=2
        if form_login.is_valid():
            user = form_signup.data['user_L']
            psw = form_signup.data['psw_L']
            hash = hashlib.sha256(psw.encode()).hexdigest()
            print(hash)
            lista = Utente.objects.filter(username=user)
            if len(lista) == 1:
                utente = lista[0]
                if hash == utente.hash:
                    msg=3
                else: msg=4
            else:msg=4
            
    form_login = LoginForm()
    form_signup = SignupForm()
    return render(request, "user.html",{
        "form_login": form_login,
        "form_signup": form_signup,
        "msg":msg
    })
    
def index(request):
    return render (request,'index.html')
def lista_autori(request):
    autori = Autore.objects.all()
    return render(request, 'lista_autori.html', {'autori':autori})

def dettaglio_autore(request, id):
    autore = get_object_or_404(Autore, pk=id)
    opere = Opera.objects.filter(author=id)
    return render(request, 'dettaglio_autore.html', {'autore': autore, "opere":opere})

def gioco(request,id):
    cross = get_object_or_404(Crossword,pk=id)
    mat = cross.matrix
    mat = json.dumps(mat)
    f = {'matrix':mat}
    return render(request,'gameFinal.html', {"cross":f})

def favicon(request):
    f= open("./media/media/imgsrc/icon.png","rb");
    r = f.read()
    f.close()
    return HttpResponse(r,content_type="image/png");
