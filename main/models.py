from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desription = models.TextField()
    category = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)