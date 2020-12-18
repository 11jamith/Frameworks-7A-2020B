from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
    status= models.BooleanField(default=True)
    description=models.TextField(default='Description here')