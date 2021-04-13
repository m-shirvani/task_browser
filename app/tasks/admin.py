from django.contrib import admin

# Register your models here.
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'created_at', 'last_modified', 'start_date', 'end_date', 'get_task_status', "parent", "is_node"]


admin.site.register(Tasks, TasksAdmin)
