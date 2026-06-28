import calendar as calendar_utils
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Count, Q
from django.urls import reverse
from django.utils import timezone
from portfolio.models import Project
from products.models import Product
from blog.models import BlogPost
from inquiries.models import Inquiry
from portfolio.forms import ProjectForm
from products.forms import ProductForm
from blog.forms import BlogPostForm
from .forms import CalendarTaskForm
from .models import CalendarTask


def is_admin_user(user):
    return user.is_authenticated and user.is_staff


admin_required = user_passes_test(is_admin_user, login_url='login')


@admin_required
def dashboard_home(request):
    """Dashboard principal con estadísticas"""
    # Estadísticas
    total_projects = Project.objects.filter(status__in=['published', 'featured']).count()
    total_products = Product.objects.filter(status__in=['published', 'featured']).count()
    total_inquiries = Inquiry.objects.count()
    pending_inquiries = Inquiry.objects.filter(status='new').count()
    total_posts = BlogPost.objects.filter(status='published').count()
    
    # Últimas solicitudes
    recent_inquiries = Inquiry.objects.all()[:5]
    
    # Accesos rápidos
    recent_projects = Project.objects.all()[:5]
    recent_posts = BlogPost.objects.all()[:5]
    
    context = {
        'total_projects': total_projects,
        'total_products': total_products,
        'total_inquiries': total_inquiries,
        'total_posts': total_posts,
        'pending_inquiries': pending_inquiries,
        'recent_inquiries': recent_inquiries,
        'recent_projects': recent_projects,
        'recent_posts': recent_posts,
    }
    return render(request, 'dashboard/dashboard_home.html', context)


@admin_required
def project_list(request):
    """Lista de proyectos en dashboard"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'dashboard/project_list.html', context)


@admin_required
def project_create(request):
    """Crear nuevo proyecto"""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto creado exitosamente.')
            return redirect('dashboard_projects')
    else:
        form = ProjectForm()
    
    context = {'form': form}
    return render(request, 'dashboard/project_form.html', context)


@admin_required
def project_edit(request, pk):
    """Editar proyecto existente"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado exitosamente.')
            return redirect('dashboard_projects')
    else:
        form = ProjectForm(instance=project)
    
    context = {'form': form, 'project': project}
    return render(request, 'dashboard/project_form.html', context)


@admin_required
def project_delete(request, pk):
    """Eliminar proyecto"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
        return redirect('dashboard_projects')
    
    context = {'project': project}
    return render(request, 'dashboard/project_confirm_delete.html', context)


@admin_required
def product_list(request):
    """Lista de productos en dashboard"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'dashboard/product_list.html', context)


@admin_required
def product_create(request):
    """Crear nuevo producto"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('dashboard_products')
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'dashboard/product_form.html', context)


@admin_required
def product_edit(request, pk):
    """Editar producto existente"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('dashboard_products')
    else:
        form = ProductForm(instance=product)
    
    context = {'form': form, 'product': product}
    return render(request, 'dashboard/product_form.html', context)


@admin_required
def product_delete(request, pk):
    """Eliminar producto"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('dashboard_products')
    
    context = {'product': product}
    return render(request, 'dashboard/product_confirm_delete.html', context)


@admin_required
def post_list(request):
    """Lista de posts en dashboard"""
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'dashboard/post_list.html', context)


@admin_required
def post_create(request):
    """Crear nuevo post"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado exitosamente.')
            return redirect('dashboard_posts')
    else:
        form = BlogPostForm()
    
    context = {'form': form}
    return render(request, 'dashboard/post_form.html', context)


@admin_required
def post_edit(request, pk):
    """Editar post existente"""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post actualizado exitosamente.')
            return redirect('dashboard_posts')
    else:
        form = BlogPostForm(instance=post)
    
    context = {'form': form, 'post': post}
    return render(request, 'dashboard/post_form.html', context)


@admin_required
def post_delete(request, pk):
    """Eliminar post"""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post eliminado exitosamente.')
        return redirect('dashboard_posts')
    
    context = {'post': post}
    return render(request, 'dashboard/post_confirm_delete.html', context)


@admin_required
def inquiry_list(request):
    """Lista de solicitudes en dashboard"""
    inquiries = Inquiry.objects.all()
    context = {'inquiries': inquiries}
    return render(request, 'dashboard/inquiry_list.html', context)


@admin_required
def inquiry_update_status(request, pk):
    """Actualizar estado de solicitud"""
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['new', 'contacted', 'closed', 'cancelled']:
            inquiry.status = new_status
            inquiry.save()
            messages.success(request, 'Estado actualizado exitosamente.')
    return redirect('dashboard_inquiries')


@admin_required
def calendar(request):
    """Calendario de publicaciones"""
    today = timezone.localdate()
    event_filter = request.GET.get('tipo', 'todo')
    if event_filter not in ['todo', 'entregas', 'publicaciones']:
        event_filter = 'todo'

    try:
        year = int(request.GET.get('year', today.year))
        month = int(request.GET.get('month', today.month))
        current_month = date(year, month, 1)
    except ValueError:
        year = today.year
        month = today.month
        current_month = date(year, month, 1)
    
    # Obtener publicaciones del mes
    projects = Project.objects.filter(
        publication_date__year=year,
        publication_date__month=month
    ).order_by('publication_date', 'title')
    posts = BlogPost.objects.filter(
        publication_date__year=year,
        publication_date__month=month
    ).order_by('publication_date', 'title')
    tasks = CalendarTask.objects.filter(
        due_date__year=year,
        due_date__month=month
    ).order_by('due_date', 'title')

    events_by_day = {}
    if event_filter in ['todo', 'publicaciones']:
        for project in projects:
            events_by_day.setdefault(project.publication_date, []).append({
                'title': project.title,
                'type': 'Publicacion',
                'icon': 'bi-folder',
                'class': 'calendar-event-project',
                'status': project.get_status_display(),
                'url': reverse('project_edit', kwargs={'pk': project.pk}),
            })

        for post in posts:
            events_by_day.setdefault(post.publication_date, []).append({
                'title': post.title,
                'type': 'Blog',
                'icon': 'bi-journal-text',
                'class': 'calendar-event-post',
                'status': post.get_status_display(),
                'url': reverse('post_edit', kwargs={'pk': post.pk}),
            })

    if event_filter in ['todo', 'entregas']:
        for task in tasks:
            events_by_day.setdefault(task.due_date, []).append({
                'title': task.title,
                'type': 'Entrega',
                'icon': 'bi-bell',
                'class': f'calendar-event-task calendar-event-task-{task.priority}',
                'status': task.get_status_display(),
                'url': reverse('calendar_task_edit', kwargs={'pk': task.pk}),
                'client_name': task.client_name,
            })

    month_calendar = calendar_utils.Calendar(firstweekday=0)
    weeks = []
    for week in month_calendar.monthdatescalendar(year, month):
        week_days = []
        for day_date in week:
            week_days.append({
                'date': day_date,
                'number': day_date.day,
                'is_current_month': day_date.month == month,
                'is_today': day_date == today,
                'events': events_by_day.get(day_date, []),
            })
        weeks.append(week_days)

    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)

    if month == 1:
        previous_month = date(year - 1, 12, 1)
    else:
        previous_month = date(year, month - 1, 1)

    month_names = [
        '', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    month_name = month_names[month]
    total_events = sum(len(events) for events in events_by_day.values())
    pending_events = sum(len(events) for event_date, events in events_by_day.items() if event_date >= today)
    
    context = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'weeks': weeks,
        'weekdays': ['LU', 'MA', 'MI', 'JU', 'VI', 'SA', 'DO'],
        'today': today,
        'previous_month': previous_month,
        'next_month': next_month,
        'total_events': total_events,
        'pending_events': pending_events,
        'task_count': tasks.count(),
        'event_filter': event_filter,
    }
    return render(request, 'dashboard/calendar.html', context)


@admin_required
def calendar_task_create(request):
    """Crear un trabajo interno para el calendario."""
    initial = {}
    due_date = request.GET.get('date')
    if due_date:
        initial['due_date'] = due_date

    if request.method == 'POST':
        form = CalendarTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Trabajo agendado exitosamente.')
            return redirect(f"{reverse('dashboard_calendar')}?month={task.due_date.month}&year={task.due_date.year}&tipo=entregas")
    else:
        form = CalendarTaskForm(initial=initial)

    context = {'form': form}
    return render(request, 'dashboard/calendar_task_form.html', context)


@admin_required
def calendar_task_edit(request, pk):
    """Editar un trabajo interno del calendario."""
    task = get_object_or_404(CalendarTask, pk=pk)

    if request.method == 'POST':
        form = CalendarTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Trabajo agendado actualizado.')
            return redirect(f"{reverse('dashboard_calendar')}?month={task.due_date.month}&year={task.due_date.year}&tipo=entregas")
    else:
        form = CalendarTaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'dashboard/calendar_task_form.html', context)


@admin_required
def calendar_task_delete(request, pk):
    """Eliminar un trabajo interno del calendario."""
    task = get_object_or_404(CalendarTask, pk=pk)
    if request.method == 'POST':
        due_date = task.due_date
        task.delete()
        messages.success(request, 'Trabajo agendado eliminado.')
        return redirect(f"{reverse('dashboard_calendar')}?month={due_date.month}&year={due_date.year}&tipo=entregas")

    context = {'task': task}
    return render(request, 'dashboard/calendar_task_confirm_delete.html', context)
