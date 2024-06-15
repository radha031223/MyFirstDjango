from django.contrib import admin

# Register your models here.
from home.models import Contact

admin.site.register(Contact)

from home.models import GroceryList, Item
admin.site.register(GroceryList)
admin.site.register(Item)