from django.db import models
from students.models import Student


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments', verbose_name='الطالب')
    month = models.DateField(verbose_name='الشهر')
    is_paid = models.BooleanField(default=False, verbose_name='تم الدفع')

    class Meta:
        verbose_name = 'دفعة'
        verbose_name_plural = 'الدفعات'
        unique_together = ('student', 'month')
        ordering = ['-month']

    def __str__(self):
        return f"{self.student.name} - {self.month:%Y-%m}"
