from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from Attendance.models import CustomUser


class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser,UserModel)