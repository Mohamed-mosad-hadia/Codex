from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'attendance', 'grade']
    list_filter = ['attendance', 'student']
    search_fields = ['student__name', 'student__phone']
