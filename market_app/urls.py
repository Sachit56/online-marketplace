from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views as auth_views
from market_app.views import index,ContactView,SignUPView
from .forms import LogIn


# app_name='market_app'

urlpatterns = [
    path('', index),
    path('items/',include('items.urls')),
    path('contact/',ContactView,name='contact_form'),
    path('signup/',SignUPView,name='sign_up'),
    path('login/',auth_views.LoginView.as_view(template_name='market_app/login.html',authentication_form=LogIn))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)