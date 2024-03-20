# In storetech/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.contrib.auth.models import User

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Electronic products')
        self.product = Product.objects.create(name='Laptop', description='A powerful laptop', price=1000, quantity=10, category=self.category)

    def test_product_creation(self):
        laptop = Product.objects.get(name='Laptop')
        self.assertEqual(laptop.quantity, 10)
        self.assertEqual(laptop.category.name, 'Electronics')

class ViewTestCase(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
