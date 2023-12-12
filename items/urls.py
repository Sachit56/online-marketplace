from django.urls import path
from . import views

app_name='items'

urlpatterns = [
    path('<int:pk>/',views.item_detail_view,name='items_detail'),
    path('add/',views.AddItemView,name='add_item'),
    path('delete/<int:pk>/',views.DeleteView,name='delete_item'),
    path('edit/<int:pk>/',views.EditItemView,name='edit_item')
]
