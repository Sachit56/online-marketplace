from django.shortcuts import render,get_object_or_404
from .models import Item

# Create your views here.
def item_detail_view(request,pk):
    item=get_object_or_404(Item,pk=pk)
    # print(items.name)
    return render(request,'items/detail.html',{
        'item':item
    })