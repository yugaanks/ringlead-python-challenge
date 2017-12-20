from django.db import models

# Create your models here.

class Product(models.Model):
	product_name=models.CharField(max_length=200)
	product_description=models.CharField(max_length=200)
	def __str__(self):
		return self.product_name
	search_fields=['product_name']
	

class Customer(models.Model):
	products=models.ManyToManyField(Product)
	customer_first_name=models.CharField(max_length=200)
	customer_last_initial=models.CharField(max_length=1)
	def __str__(self):
		return self.customer_first_name
