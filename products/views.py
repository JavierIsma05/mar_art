from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    category_filter = request.GET.get('category', '')
    query = request.GET.get('q', '')
    products = Product.objects.filter(status__in=['published', 'featured'])

    if category_filter:
        products = products.filter(category=category_filter)

    if query:
        products = products.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(category__icontains=query)
        )

    context = {
        'products': products,
        'categories': Product.CATEGORY_CHOICES,
        'category_filter': category_filter,
        'query': query,
    }
    return render(request, 'public/products.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, status__in=['published', 'featured'])
    related_products = Product.objects.filter(
        category=product.category,
        status__in=['published', 'featured'],
    ).exclude(pk=product.pk)[:3]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'public/product_detail.html', context)
