from django.contrib import admin

from .models import task


class Taskadmin(admin.ModelAdmin):
    list_display=("task","is_completed","updated_at")
    search_fields=('task',)
# Register your models here.
admin.site.register(task,Taskadmin)