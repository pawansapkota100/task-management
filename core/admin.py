from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'status')
    search_fields = ('name',)
    list_filter=('priority', 'status')
    readonly_fields = ('created_at', 'updated_at') 

   
    fieldsets = (
        (None, {'fields': ('name', 'description', 'created_by', 'priority', 'status')}),
        ('Timestamp', {'fields': ('created_at', 'updated_at')}),
    )



admin.site.register(Task,TaskAdmin)