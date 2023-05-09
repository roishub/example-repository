from django.db import models
from django.test import TestCase
from mywork.models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Test", description="This is a test")

    def test_my_model_has_name(self):
        test = MyModel.objects.get(name="Test")
        self.assertEqual(test.name, "Test")

    def test_my_model_has_description(self):
        test = MyModel.objects.get(name="Test")
        self.assertEqual(test.description, "This is a test")

# Create your models here.
