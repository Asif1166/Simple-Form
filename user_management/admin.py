from django.contrib import admin

from user_management.models import UserManagment

# Register your models here.
@admin.register(UserManagment)
class UserManagmentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in UserManagment._meta.fields]