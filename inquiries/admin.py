from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'whatsapp', 'service_interest', 'quantity', 'needed_date', 'status', 'created_at']
    list_filter = ['service_interest', 'status', 'created_at']
    search_fields = ['full_name', 'email', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
