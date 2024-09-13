from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # List of fields to be displayed in the user list view
    list_display = ('username', 'email', 'phone_number', 'address', 'is_staff', 'is_active')
    # Fields to be displayed in the user detail view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    # Fields to be displayed in the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    # List of fields to be searchable
    search_fields = ('username', 'email', 'phone_number')
    # List of fields to filter the user list view
    list_filter = ('is_staff', 'is_active')

# Register the CustomUser model with the customized UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
