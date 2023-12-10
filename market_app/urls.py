from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from market_app.views import index,contact,SignUPView


urlpatterns = [
    path('', index),
    path('items/',include('items.urls')),
    path('contact/',contact,name='contact'),
    path('signup/',SignUPView,name='sign_up')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)