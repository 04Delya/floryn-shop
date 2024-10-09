from django.forms import ModelForm, TextInput, ChoiceField, DecimalField
from main.models import Product
from django.utils.html import strip_tags

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

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get("description")
        return strip_tags(description)

    def clean_category(self):
        category = self.cleaned_data.get("category")
        return strip_tags(category)

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        return strip_tags(rating)