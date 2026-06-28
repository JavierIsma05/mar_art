from django.contrib import admin

from .models import CalendarTask


@admin.register(CalendarTask)
class CalendarTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_name', 'due_date', 'priority', 'status']
    list_filter = ['status', 'priority', 'due_date']
    search_fields = ['title', 'client_name', 'notes']

# Register your models here.
