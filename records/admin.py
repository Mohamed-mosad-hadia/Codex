from django.contrib import admin
from django.db.models import F
from .models import Record


class GradeFilter(admin.SimpleListFilter):
    title = 'grade'
    parameter_name = 'grade_range'

    def lookups(self, request, model_admin):
        return [
            ('lt50', 'Below 50%'),
            ('50to70', '50% - 70%'),
            ('gt70', 'Above 70%'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'lt50':
            return queryset.filter(grade__lt=F('max_grade') * 0.5)
        if value == '50to70':
            return queryset.filter(
                grade__gte=F('max_grade') * 0.5,
                grade__lt=F('max_grade') * 0.7,
            )
        if value == 'gt70':
            return queryset.filter(grade__gte=F('max_grade') * 0.7)
        return queryset


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'attendance', 'grade_percentage']
    list_filter = ['attendance', 'student', GradeFilter]
    search_fields = ['student__name', 'student__phone']
