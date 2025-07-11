from django.contrib import admin
from .models import Group, Student
from records.models import Record
from payments.models import Payment


class RecordInline(admin.TabularInline):
    model = Record
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'password', 'group', 'registration_date']
    search_fields = ['name', 'phone']
    list_filter = ['group']
    inlines = [RecordInline, PaymentInline]
