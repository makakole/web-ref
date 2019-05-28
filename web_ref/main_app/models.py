from django.db import models

# Create your models here.


from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save()
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 255, blank = True, null = True)
    last_name = models.CharField(max_length = 255, blank = True, null = True)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


    def has_perm(self, perm, obj=None):
        if self.staff and self.admin:
            return True
        else:
            return False

    def has_module_perms(self, app_label):
        if self.staff and self.admin:
            return True
        else:
            return False




class IdData(models.Model):

    first_name = models.CharField(max_length = 100, blank = False, null = True)
    second_name = models.CharField(max_length = 100, blank = False, null = True)
    surname = models.CharField(max_length = 100, blank = True, null = True)
    id_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)



class References(models.Model):
    data = models.ForeignKey(IdData, on_delete=models.CASCADE)
    reference = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    generated_for = models.CharField(max_length=50)
    reason = models.CharField(max_length=250)
    requested = models.BooleanField(default=False)
    requests = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class RequestPermissions(models.Model):
    names = models.BooleanField(default=False)
    date_of_birth = models.BooleanField(default=False)
    race = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    nationality = models.BooleanField(default=False)
    reference = models.ForeignKey(References, on_delete=models.CASCADE)