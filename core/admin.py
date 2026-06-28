from django.contrib import admin
from .models import SiteBanner, SiteConfiguration, Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'role', 'message']


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'whatsapp', 'email']
    search_fields = ['brand_name', 'slogan']


@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']
