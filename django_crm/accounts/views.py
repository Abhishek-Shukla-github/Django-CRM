from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = Customer.objects.all().count()
    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status="Delivered").count()
    pending = Order.objects.filter(status="Pending").count()
    context = {'orders': orders, 'customers': customers,
               'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, "accounts/dashboard.html", context)


def product(request):
    products = Product.objects.all()
    return render(request, "accounts/product.html", {'products': products})


def customer(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders,
               'orders_count': orders_count}
    return render(request, "accounts/customer.html", context)
