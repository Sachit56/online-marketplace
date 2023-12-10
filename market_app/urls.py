from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from market_app.views import index,contact


urlpatterns = [
    path('', index),
    path('items/',include('items.urls')),
    path('contact/',contact,name='contact')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)