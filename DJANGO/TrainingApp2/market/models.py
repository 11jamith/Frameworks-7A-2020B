from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
    status= models.BooleanField(default=True)
    description=models.TextField(default='Description here')

    def __str__(self):
        return self.name


class Vendor(models.Model):
    code = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)
    status= models.BooleanField(default=True)
    description=models.TextField(default='Description here')

    def __str__(self):
        return self.name

    
class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    unit_price = models.IntegerField()
    quantity =models.IntegerField()
    id_category= models.ForeignKey(Category, on_delete= models.CASCADE)
    id_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

    def __str__(self):
        return self.name

class Client(models.Model):
    code = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    code = models.CharField(max_length=100)  
    name = models.CharField(max_length=150)
    abrev= models.CharField(max_length=100)

    def __str__(self):
        return self.name

