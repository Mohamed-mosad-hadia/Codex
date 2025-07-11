from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'month', 'is_paid']
    list_filter = ['is_paid', 'month']
    search_fields = ['student__name', 'student__phone']
