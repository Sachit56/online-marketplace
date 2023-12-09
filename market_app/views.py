# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from items.models import Category,Item

def index(request):
    categories=Category.objects.all()
    items=Item.objects.filter(is_sold=False).all()

    context={
        'categories':categories,
        'items':items
    }

    return render(request,'market_app/index.html',context=context)

def contact(request):
    return render(request,'market_app/contact.html')    