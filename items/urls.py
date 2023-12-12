from django.urls import path
from . import views

app_name='items'

urlpatterns = [
    path('<int:pk>/',views.item_detail_view,name='items_detail'),
    path('add/',views.AddItemView,name='add_item')
]
