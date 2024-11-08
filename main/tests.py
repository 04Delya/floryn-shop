from django.test import TestCase, Client
from .models import Product

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/nonexistant/')
        self.assertEqual(response.status_code, 404)

    def test_create_product(self):
        product = Product.objects.create(
            name="Red Rose Bouquet",
            price=300000,
            description="Express your love with this elegant bouquet of 12 fresh red roses, symbolizing beauty and passion.",
            category="Flower Bouquet",
            rating=4
        )
        self.assertEqual(product.name, "Red Rose Bouquet")
        self.assertEqual(product.price, 300000)

    def test_product_list(self):
        Product.objects.create(name="Product 1", price=50000, description="Desc 1", category="Cat 1", rating=4)
        Product.objects.create(name="Product 2", price=150000, description="Desc 2", category="Cat 2", rating=4)
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)

        self.assertEqual(products[0].name, "Product 1")
        self.assertEqual(products[0].price, 50000)

        self.assertEqual(products[1].name, "Product 2")
        self.assertEqual(products[1].price, 150000)
