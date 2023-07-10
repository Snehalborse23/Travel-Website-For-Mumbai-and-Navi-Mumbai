from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,  Review, Location

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom fields", {"fields": ("phone_number",)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Review)
admin.site.register(Location)

