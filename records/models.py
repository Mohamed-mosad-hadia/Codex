from django.db import models
from students.models import Student


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='records', verbose_name='الطالب')
    date = models.DateField(verbose_name='التاريخ')
    attendance = models.BooleanField(default=False, verbose_name='حضور')
    grade = models.FloatField(null=True, blank=True, verbose_name='الدرجة')
    max_grade = models.PositiveIntegerField(
        default=100, verbose_name='أقصى درجة'
    )
    notes = models.TextField(blank=True, verbose_name='ملاحظات')

    class Meta:
        verbose_name = 'سجل أسبوعي'
        verbose_name_plural = 'السجلات الأسبوعية'
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.name} - {self.date}"

    @property
    def grade_percentage(self):
        """Return the student's grade as a percentage of max_grade."""
        if self.grade is None or not self.max_grade:
            return None
        return round((self.grade / self.max_grade) * 100, 2)
