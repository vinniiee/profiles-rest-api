from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manger for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) # makes 2nd half of the email address all lower case
        user = self.model(email=email, name=name)  # to make a model for name and email

        user.set_password(password)  # for properly saving password with hashing
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """CREATE AND SAVE A SUPERUSER WITH GIVEN DETAILS"""
        user=self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #to provide django admin access

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'    #to work with django-admin, django-authentication system
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
