# example/views.py
from datetime import datetime
from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
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

def ContactView(request):
    return render(request,'market_app/contact.html')    




def SignUPView(request):
    if request.method == 'POST':
        form = SignUp(request.POST)

        if form.is_valid():
            print(form.save())
            # Use the view name 'contact' in reverse
            return redirect(reverse('market_app:contact_form'))
        else:
            print(form.errors)
    
    else:
        form = SignUp()

    return render(request, 'market_app/signup.html', {'form': form})
