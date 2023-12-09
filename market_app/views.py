# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'market_app/index.html')

def base(request):
    return render(request,'market_app/base.html')

def contact(request):
    return render(request,'market_app/contact.html')    