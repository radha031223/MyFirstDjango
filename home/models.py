from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    desc= models.TextField()
    date= models.DateField()
    def __str__(self):
        return self.name


class GroceryList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grocery_lists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    grocery_list = models.ForeignKey(GroceryList, on_delete=models.CASCADE, related_name='items')
    
    def __str__(self):
        return self.name

   