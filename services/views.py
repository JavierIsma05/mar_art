from django.shortcuts import render
from .models import ServicePlan


def services_list(request):
    """Lista de planes de servicios"""
    services = ServicePlan.objects.filter(status='active').order_by('-is_featured', 'price')
    
    context = {
        'services': services,
    }
    return render(request, 'public/services.html', context)
