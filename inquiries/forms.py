from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'full_name',
            'whatsapp',
            'email',
            'service_interest',
            'quantity',
            'needed_date',
            'message',
            'reference_image',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu numero de WhatsApp'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com (opcional)'}),
            'service_interest': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'needed_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Cuentanos producto, idea, colores, frase, logo o referencia.',
            }),
            'reference_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_needed_date(self):
        needed_date = self.cleaned_data.get('needed_date')
        if needed_date:
            minimum_date = timezone.localdate() + timedelta(days=2)
            if needed_date < minimum_date:
                raise forms.ValidationError('Recomendamos solicitar pedidos con al menos 48 horas de anticipacion.')
        return needed_date
