from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CandidateRegistrationModel, CustomUser


class CandidateRegistrationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("First name", {'fields':['first_name']}),
        ("Last name", {'fields':['last_name']}),
    ]
    list_display = ('first_name', 'last_name')
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

#Tell the admin that CandidateRegistrationModel objects have an admin interface
admin.site.register(CandidateRegistrationModel, CandidateRegistrationAdmin)

# Tell Django to use CustomUser for the admin site
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)