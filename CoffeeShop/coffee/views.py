from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee, Dessert


def home(request):
    coffee = Coffee.objects.all()
    return render (request, 'home.html')

def coffee(request):
    coffee = Coffee.objects.all()
    return render (request, 'coffee.html',{'coffee':coffee})


def dessert(request):
    dessert = Dessert.objects.all()
    return render (request, 'dessert.html',{'dessert':dessert})