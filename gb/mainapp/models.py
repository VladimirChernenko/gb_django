from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name= 'Name', max_length= 120, unique= True)
    description = models.TextField(verbose_name= 'Desccription')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='Short description',
    max_length=60, blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8,
    decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Quantity',
    default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"