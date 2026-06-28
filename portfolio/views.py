from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Project


def portfolio_list(request):
    """Lista de trabajos recientes."""
    category_filter = request.GET.get('category', '')
    query = request.GET.get('q', '')
    projects = Project.objects.filter(status__in=['published', 'featured'])

    if category_filter:
        projects = projects.filter(category=category_filter)

    if query:
        projects = projects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(client_name__icontains=query)
            | Q(tags__icontains=query)
        )

    context = {
        'projects': projects,
        'categories': Project.CATEGORY_CHOICES,
        'category_filter': category_filter,
        'query': query,
    }
    return render(request, 'public/portfolio.html', context)


def project_detail(request, slug):
    """Detalle de un trabajo publicado."""
    project = get_object_or_404(Project, slug=slug, status__in=['published', 'featured'])
    related_projects = Project.objects.filter(
        category=project.category,
        status__in=['published', 'featured'],
    ).exclude(id=project.id)[:3]

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'public/project_detail.html', context)
