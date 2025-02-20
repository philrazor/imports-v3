from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

class Make(models.Model):
    make_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.make_name

class Model(models.Model):
    model_name = models.CharField(max_length=100)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)


    def __str__(self):
        return self.model_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.product_name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.product_name}"