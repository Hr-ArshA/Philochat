from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', "email", "is_staff", "is_active", 'user_id')
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "username","password", "user_id", "profile_picture", 'user_bio')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", 'username',"password1", "password2",
            )}
        ),
    )
    search_fields = ("email", 'username')
    ordering = ("email", 'username')


admin.site.register(User, CustomUserAdmin)