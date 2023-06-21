from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    quantity=models.IntegerField()
    price=models.FloatField()
    
















class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField()
    contact_number=models.IntegerField()