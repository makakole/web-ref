from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import IdData, References, RequestPermissions


User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(IdData)
admin.site.register(References)
admin.site.register(RequestPermissions)
