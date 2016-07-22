from django.db import models
from django.utils import timezone
from users.models import User

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    stock = models.PositiveIntegerField()
    operations = models.ManyToManyField("ManageOperation", through = "ProductStock")

    def __str__(self):
        return self.title

class ManageOperation(models.Model):
    date_opened = models.DateTimeField(auto_now_add = True, null = False)
    date_closed = models.DateTimeField( null = True)
    opened_by = models.ForeignKey(User, null = False, related_name = "operations_opened")
    closed_by = models.ForeignKey(User, null = True, related_name = "operations_closed")

    class Meta:
        ordering = ["-date_opened", "-date_closed"]

class ProductStock(models.Model):
    stock_opened = models.PositiveIntegerField( null = False)
    stock_closed = models.PositiveIntegerField(null = True)
    product = models.ForeignKey(Product)
    operation = models.ForeignKey(ManageOperation)

    class Meta:
        unique_together = ("operation", "product")
