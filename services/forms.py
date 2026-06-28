from django import forms
from .models import ServicePlan


class ServicePlanForm(forms.ModelForm):
    class Meta:
        model = ServicePlan
        fields = ['name', 'slug', 'description', 'price', 'includes', 
                  'is_featured', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'includes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 
                                               'help_text': 'Separar cada característica con una coma'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
