from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile
from contact.models import Contact

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'custom_group', 'is_superuser',]

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''





admin.site.register(CustomUser, CustomUserAdmin)



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','email_address', 'profile_image', 'colour']

admin.site.register(UserProfile, UserProfileAdmin)