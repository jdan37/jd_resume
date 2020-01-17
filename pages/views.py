from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')    

def about(request):
    return render(request, 'pages/about.html')

def res(request):
    return render(request, 'pages/res.html')