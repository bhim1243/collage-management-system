from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserMOdel(UserAdmin):
    list_display = ['username', 'user_types']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Course)
admin.site.register(Session_year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
