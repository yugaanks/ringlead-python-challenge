import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template.loader import get_template
# Create your views here.

from .models import Product, Customer

class IndexView(generic.ListView):
    template_name='apollo/index.html'
    context_object_name='customer_list'
    def get_queryset(self):
        return Customer.objects.all()

@csrf_exempt
def welcome(request):
    template_name='apollo/welcome.html'
    template=get_template(template_name)
    html=template.render()
    return HttpResponse(html)
    

@csrf_exempt
def add_customer(request):
    if request.method=='POST':
        received_json_data=json.loads(request.body.decode("utf-8"))
        new_customer=Customer()
        new_customer.customer_first_name=received_json_data['customer_first_name']
        new_customer.customer_last_initial=received_json_data['customer_last_initial']
        new_customer.save()
        return HttpResponse("Customer Added to Database")
    return HttpResponse("Expected POST Request")
        
@csrf_exempt
def add_product(request):
    if request.method=='POST':
        received_json_data=json.loads(request.body.decode("utf-8"))
        new_product=Product()
        new_product.product_name=received_json_data['product_name']
        new_product.product_description=received_json_data['product_description']
        new_product.save()
        return HttpResponse("Product Added to Database")
    return HttpResponse("Expected POST Request")

@csrf_exempt
def delete_customer(request, customer_id):
    if request.method=='DELETE':
        try:
            Customer.objects.get(pk=customer_id).delete()
        except (KeyError, Customer.DoesNotExist):
            return HttpResponse("Customer doesn't exist")
        else:
            return HttpResponse("Customer Deleted from Database")
    return HttpResponse("Expected DELETE Request")

@csrf_exempt
def delete_product(request, product_id):
    if request.method=='DELETE':
        try:
            Product.objects.get(pk=product_id).delete()
        except (KeyError, Product.DoesNotExist):
            return HttpResponse("Product doesn't exist")
        else:
            return HttpResponse("Product Deleted from Database")
    return HttpResponse("Expected DELETE Request")

@csrf_exempt
def add_product_to_customer_cart(request, customer_id, product_id):
    if request.method=='PUT':
        try:
            product=Product.objects.get(pk=product_id)
            customer=Customer.objects.get(pk=customer_id)
        except (KeyError, Product.DoesNotExist):
            return HttpResponse("Product doesn't exist")
        except (KeyError, Customer.DoesNotExist):
            return HttpResponse("Customer doesn't exist")
        else:
            customer.products.add(product)
            return HttpResponse("Product added to cart")
    return HttpResponse("Expected PUT Request")

@csrf_exempt
def delete_product_from_customer_cart(request, customer_id, product_id):
    if request.method=='DELETE':
        try:
            product=Product.objects.get(pk=product_id)
            customer=Customer.objects.get(pk=customer_id)
        except (KeyError, Product.DoesNotExist):
            return HttpResponse("Product doesn't exist")
        except (KeyError, Customer.DoesNotExist):
            return HttpResponse("Customer doesn't exist")
        else:
            customer.products.remove(product)
            return HttpResponse("Product removed from cart")
    return HttpResponse("Expected DELETE Request")

def error(request):
    return HttpResponse("Something's not right, Why don't you go back to the start: <a href= '/apollo'>Apollo</a>")
    
        
        
    
