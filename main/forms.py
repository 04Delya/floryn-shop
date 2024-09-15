from django.forms import ModelForm, TextInput, ChoiceField, DecimalField
from main.models import Product

class ProductForm(ModelForm):
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

    category = ChoiceField(choices=CATEGORY_CHOICES)
    
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "rating"]

        rating = DecimalField(min_value=0.00, max_value=5.00, decimal_places=2, label='Rating')

        widgets = {
            'price': TextInput(attrs={'placeholder': 'Rp'}),
        }