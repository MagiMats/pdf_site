from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField()