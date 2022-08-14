from django.db import models
from users.models import CustomUser

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #Make a foreignkey to the user so that they are linked to this book and can only acces it

    name = models.CharField(max_length=50)
    #Name to be displayed of the book

    page_amount = models.IntegerField(validators = [MinValueValidator(1)],null=True)
    #Total amount of pages

    current_page = models.IntegerField(validators = [MaxValueValidator(page_amount), MinValueValidator(1)], default=1)
    #The page which the user last opened

    file = models.FileField(upload_to="media/pdf/")
    #The link to the actual field where the file is located

    

