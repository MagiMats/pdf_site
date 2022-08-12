from django.db import models
from users.models import CustomUser

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    page_amount = models.IntegerField(validators = [MinValueValidator(1)])
    current_page = models.IntegerField(validators = [MaxValueValidator(page_amount), MinValueValidator(1)])
    file = models.FileField(upload_to="media/pdf/")
