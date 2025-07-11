from django.contrib import admin
from django.contrib.auth.models import User, Group as AuthGroup

# Customize admin site appearance
admin.site.site_header = 'مركز الطلاب'
admin.site.site_title = 'إدارة المركز'
admin.site.index_title = 'لوحة التحكم'

# Hide default auth models for assistants
admin.site.unregister(User)
admin.site.unregister(AuthGroup)
