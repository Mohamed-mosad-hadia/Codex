from django.db import models
from students.models import Student


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='records', verbose_name='الطالب')
    date = models.DateField(verbose_name='التاريخ')
    attendance = models.BooleanField(default=False, verbose_name='حضور')
    grade = models.FloatField(null=True, blank=True, verbose_name='الدرجة')
    notes = models.TextField(blank=True, verbose_name='ملاحظات')

    class Meta:
        verbose_name = 'سجل أسبوعي'
        verbose_name_plural = 'السجلات الأسبوعية'
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.name} - {self.date}"
