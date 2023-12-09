# example/urls.py
from django.urls import path

from market_app.views import index,base,contact


urlpatterns = [
    path('', index),
    path('base/',base,name='base'),
    path('contact/',contact,name='contact')
]