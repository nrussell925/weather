from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# n


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "city",
        "city2",
        "city3",
        "city4",
        "city5",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "age",
                    "city",
                    "city2",
                    "city3",
                    "city4",
                    "city5",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "age",
                    "city",
                    "city2",
                    "city3",
                    "city4",
                    "city5",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
