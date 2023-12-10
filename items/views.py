from django.shortcuts import render,get_object_or_404
from .models import Item

# Create your views here.
def item_detail_view(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_item=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    # print(items.name)
    return render(request,'items/detail.html',{
        'item':item,
        'related_item':related_item
    })