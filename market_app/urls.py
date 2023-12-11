from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from market_app.views import index,ContactView,SignUPView

app_name='market_app'

urlpatterns = [
    path('', index),
    path('items/',include('items.urls')),
    path('contact/',ContactView,name='contact_form'),
    path('signup/',SignUPView,name='sign_up')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)