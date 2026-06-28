from django import forms

from .models import CalendarTask


class CalendarTaskForm(forms.ModelForm):
    class Meta:
        model = CalendarTask
        fields = ['title', 'client_name', 'due_date', 'priority', 'status', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Entregar camisetas personalizadas'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente (opcional)'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Detalles, cantidades, colores, pendientes o recordatorios.',
            }),
        }
