from django.db import models


# Create your models here.
class User(models.Model):
    Book_name=models.CharField(max_length=100)
    available_stock=models.CharField(max_length=100);
    writter=models.CharField(max_length=110)
    
