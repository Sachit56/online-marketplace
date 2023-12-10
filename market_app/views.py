# example/views.py
from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from items.models import Category,Item
from .forms import SignUp

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

def SignUPView(request):
   
    if request.POST:
        form=SignUp(request.POST)

        if form.is_valid():
            form.save()

            redirect('/contact')
    else:
         form=SignUp()        
            


    return render(request,'market_app/signup.html',{
        'form':form
    })