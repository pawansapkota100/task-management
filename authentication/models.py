from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
# Create your views here.
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=CustomUserManager()
    permission=models.ManyToManyField("auth.Permission", blank=True)
    groups=models.ManyToManyField("auth.Group", blank=True)

    def __str__(self):
        return self.email
