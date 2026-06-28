from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    
    # Projects
    path('proyectos/', views.project_list, name='dashboard_projects'),
    path('proyectos/crear/', views.project_create, name='project_create'),
    path('proyectos/<int:pk>/editar/', views.project_edit, name='project_edit'),
    path('proyectos/<int:pk>/eliminar/', views.project_delete, name='project_delete'),
    
    # Products
    path('productos/', views.product_list, name='dashboard_products'),
    path('productos/crear/', views.product_create, name='product_create'),
    path('productos/<int:pk>/editar/', views.product_edit, name='product_edit'),
    path('productos/<int:pk>/eliminar/', views.product_delete, name='product_delete'),
    
    # Posts
    path('blog/', views.post_list, name='dashboard_posts'),
    path('blog/crear/', views.post_create, name='post_create'),
    path('blog/<int:pk>/editar/', views.post_edit, name='post_edit'),
    path('blog/<int:pk>/eliminar/', views.post_delete, name='post_delete'),
    
    # Inquiries
    path('solicitudes/', views.inquiry_list, name='dashboard_inquiries'),
    path('solicitudes/<int:pk>/estado/', views.inquiry_update_status, name='inquiry_update_status'),
    
    # Calendar
    path('calendario/', views.calendar, name='dashboard_calendar'),
    path('calendario/trabajo/crear/', views.calendar_task_create, name='calendar_task_create'),
    path('calendario/trabajo/<int:pk>/editar/', views.calendar_task_edit, name='calendar_task_edit'),
    path('calendario/trabajo/<int:pk>/eliminar/', views.calendar_task_delete, name='calendar_task_delete'),
]
