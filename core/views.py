from django.shortcuts import render

from core.models import SiteBanner, Testimonial
from portfolio.models import Project
from products.models import Product


def home(request):
    """Inicio comercial para la vitrina digital."""
    featured_projects = Project.objects.filter(status__in=['published', 'featured'])[:8]
    featured_products = Product.objects.filter(
        status__in=['published', 'featured'],
        is_featured=True,
    )[:6]
    banners = SiteBanner.objects.filter(is_active=True)[:3]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]

    context = {
        'featured_projects': featured_projects,
        'featured_products': featured_products,
        'banners': banners,
        'testimonials': testimonials,
    }
    return render(request, 'public/home.html', context)
