import uuid 
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

CATEGORY_CHOICES = [
    ('Single Flower', 'Single Flower'),
    ('Mixed Flower Arrangement', 'Mixed Flower Arrangement'),
    ('Flower Bouquet', 'Flower Bouquet'),
    ('Wedding Bouquet', 'Wedding Bouquet'),
    ('Seasonal Bouquet', 'Seasonal Bouquet'),
    ('Birthday Bouquet', 'Birthday Bouquet'),
    ('Anniversary Bouquet', 'Anniversary Bouquet'),
    ('Custom Design Bouquet', 'Custom Design Bouquet'),
]

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    amount = models.IntegerField(validators=[MinValueValidator(1)], default=1)  
    price = models.IntegerField(validators=[MinValueValidator(0)]) 
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  