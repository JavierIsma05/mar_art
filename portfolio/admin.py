from django.contrib import admin
from .models import Project, ProjectGallery


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1
    fields = ['image', 'caption']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'publication_date', 'created_at']
    list_filter = ['category', 'status', 'is_featured', 'publication_date']
    search_fields = ['title', 'description', 'client_name', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectGalleryInline]
    date_hierarchy = 'publication_date'
