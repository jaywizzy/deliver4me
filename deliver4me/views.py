import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calc():
    x= 1
    b =2 
    return x

def index(request):

    a = calc()
    return render(request, 'index.html')
