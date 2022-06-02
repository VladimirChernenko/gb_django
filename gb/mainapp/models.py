from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='Name', unique=True)
    description = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=60)
    image = models.ImageField(upload_to='media', blank=True)
    short_desc = models.CharField(verbose_name='Short description', max_length=240, blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, quantity in stock: {self.quantity}.'