from django.db import models
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    #category =
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category
