from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'created_at', 'author')
    search_fields = ('title', 'company', 'location', 'description')
    list_filter = ('created_at',)
