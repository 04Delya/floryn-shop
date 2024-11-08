from django.forms import ModelForm, TextInput, ChoiceField, IntegerField
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
    amount = IntegerField(min_value=1, label='Amount')
    price = IntegerField(min_value=0, label='Price (Rp)')
    rating = IntegerField(min_value=1, max_value=5, label='Rating')

    class Meta:
        model = Product
        fields = ["name", "description", "category", "amount", "price", "rating"]

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

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount is not None and amount < 1:
            self.add_error('amount', "Amount must be at least 1.")
        return amount

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            self.add_error('price', "Price cannot be negative.")
        return price