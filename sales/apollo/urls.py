from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name='apollo'
urlpatterns=[
            url(r'^$', views.welcome, name='welcome'),
            url(r'^list-all-customers/$', views.IndexView.as_view(), name='index'),
            url(r'^add-customer/$', views.add_customer, name='add_customer'),
            url(r'^add-product/$', views.add_product, name='add_product'),
            url(r'^delete-customer/(?P<customer_id>[0-9]+)/$', views.delete_customer, name='delete_customer'),
            url(r'^delete-product/(?P<product_id>[0-9]+)/$', views.delete_product, name='delete_product'),
            url(r'^add/customer/(?P<customer_id>[0-9]+)/product/(?P<product_id>[0-9]+)/$', views.add_product_to_customer_cart, name="add_to_cart"),
            url(r'^remove/customer/(?P<customer_id>[0-9]+)/product/(?P<product_id>[0-9]+)/$', views.delete_product_from_customer_cart, name="delete from cart"),
             ]
