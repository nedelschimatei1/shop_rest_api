from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
#         }),
#     )
#     list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
#     ordering = ['username']
#     search_fields = ['username', 'first_name', 'last_name', 'email']
