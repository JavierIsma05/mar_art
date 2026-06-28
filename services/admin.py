from django.contrib import admin
from .models import ServicePlan


@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_featured', 'status', 'created_at']
    list_filter = ['is_featured', 'status', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
