from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='اسم المجموعة')

    class Meta:
        verbose_name = 'مجموعة'
        verbose_name_plural = 'المجموعات'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم الكامل')
    phone = models.CharField(max_length=20, unique=True, verbose_name='رقم الهاتف')
    password = models.CharField(max_length=128, verbose_name='كلمة المرور')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='المجموعة')
    registration_date = models.DateField(auto_now_add=True, verbose_name='تاريخ التسجيل')

    class Meta:
        verbose_name = 'طالب'
        verbose_name_plural = 'الطلاب'

    def __str__(self):
        return self.name
