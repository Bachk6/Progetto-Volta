from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def placeholder(request):
    return render(request,"placeholder.html")