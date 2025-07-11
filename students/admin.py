from django.contrib import admin
from django.db.models import Avg, F, FloatField, ExpressionWrapper
from .models import Group, Student
from records.models import Record
from payments.models import Payment


class RecordInline(admin.TabularInline):
    model = Record
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class GradeRangeFilter(admin.SimpleListFilter):
    title = 'avg grade'
    parameter_name = 'avg_grade'

    def lookups(self, request, model_admin):
        return [
            ('lt50', 'Below 50%'),
            ('50to70', '50% - 70%'),
            ('gt70', 'Above 70%'),
        ]

    def queryset(self, request, queryset):
        annotated = queryset.annotate(
            avg_grade=Avg(
                ExpressionWrapper(
                    F('records__grade') * 100.0 / F('records__max_grade'),
                    output_field=FloatField(),
                )
            )
        )
        value = self.value()
        if value == 'lt50':
            return annotated.filter(avg_grade__lt=50)
        if value == '50to70':
            return annotated.filter(avg_grade__gte=50, avg_grade__lt=70)
        if value == 'gt70':
            return annotated.filter(avg_grade__gte=70)
        return queryset


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'password',
        'group',
        'registration_date',
        'display_avg_grade',
    ]
    search_fields = ['name', 'phone']
    list_filter = ['group', GradeRangeFilter]
    inlines = [RecordInline, PaymentInline]

    @admin.display(description='Avg Grade %')
    def display_avg_grade(self, obj):
        value = obj.avg_grade_percentage
        return f"{value:.1f}%" if value is not None else '-'
