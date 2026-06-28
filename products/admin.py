from django.contrib import admin
from .models import Product, ProductGallery


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    fields = ['image', 'caption']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'status', 'is_available', 'is_featured', 'created_at']
    list_filter = ['category', 'status', 'is_available', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProductGalleryInline]
