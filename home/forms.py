from django import forms
from .models import GroceryList, Item

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = ['name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity']
