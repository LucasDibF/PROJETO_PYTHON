from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "done", "deadline", "created_at")
    list_filter = ("done",)
    search_fields = ("title", "description")
