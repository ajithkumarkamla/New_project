from django.contrib import admin
from .models import StudentResult, ServerStatus

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ('register_number', 'name', 'dob', 'total', 'grade')
    search_fields = ('register_number', 'name')
    list_filter = ('grade',)

@admin.register(ServerStatus)
class ServerStatusAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'is_active')
    list_editable = ('is_active',)