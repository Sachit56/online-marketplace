from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200,null=True,blank=True)
    price=models.IntegerField()
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return self.name
