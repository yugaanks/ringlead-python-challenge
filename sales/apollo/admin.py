from django.contrib import admin
from .models import Product, Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	fieldSets=[ 
	('First Name', {'fields': ['customer_first_name']}),
	('Last Name Initial', {'fields': ['customer_last_initial']})]
	list_display=('customer_first_name', 'customer_last_initial')

class ProductAdmin(admin.ModelAdmin):
	fieldSets=[ 
	('Product name', {'fields': ['product_name']}),
	('Product description', {'fields': ['product_description']})]
	list_display=('id', 'product_name', 'product_description')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
