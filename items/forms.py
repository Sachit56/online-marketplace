from django import forms
from .models import Item

INPUT = 'w-full py-4 px-6 rounded-xl border'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            'category': forms.Select(attrs={'class': INPUT}),
            'name': forms.TextInput(attrs={'class': INPUT}),
            'description': forms.Textarea(attrs={'class': INPUT}),
            'price': forms.NumberInput(attrs={'class': INPUT}),
            'is_sold': forms.CheckboxInput(attrs={'class': INPUT}),
            'created_by': forms.Select(attrs={'class': INPUT}),
            'image': forms.FileInput(attrs={'class': INPUT})
        }
