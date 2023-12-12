from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from django.urls import reverse

# Create your views here.
def item_detail_view(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_item=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'items/detail.html',{
        'item':item,
        'related_item':related_item
    })

@login_required
def AddItemView(request):
    if request.POST:
        form=ItemForm(request.POST,request.FILES)

        if form.is_valid():
            try:
                item = form.save(commit=False)
                item.created_by = request.user
                item.save()
            except Exception as e:
                print(f"Exception during file upload: {e}")


            return redirect(reverse('items:items_detail',args=[item.pk]))
    else:
        form=ItemForm()
            

    

    return render(request,'items/add_item.html',{
        'form':form
    })

@login_required
def DeleteView(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect(reverse('dashboard:dashboard'))