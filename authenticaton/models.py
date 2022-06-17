from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models 
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Users should habe a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should no t be none')

        user = self.create_user(username, email, password)
        user.is_superuser =True
        user.is_staff = True
        user.save()
        return user

    