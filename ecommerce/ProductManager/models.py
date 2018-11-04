from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    upperCategory = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)# short description of product
    thumbnail = models.ImageField()
    price = models.FloatField()
    avaialableAmt = models.FloatField()
    body = models.TextField(max_length=5000)# actual text appearing on product detail site
    
    def __str__(self):
        return self.name

class Image(models.Model):
    img = models.ImageField()
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.__str__() + ' img'

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)