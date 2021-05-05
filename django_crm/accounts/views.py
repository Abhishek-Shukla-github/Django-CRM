from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    total_pending = orders.filter(status="Pending").count()
    print(total_pending)
    total_delivered = orders.filter(status="Delivered").count()
    context = {'customers': customers, 'orders': orders,
               'total_customers': total_customers, 'total_orders': total_orders, 'total_delivered': total_delivered,
               'total_pending': total_pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders,
               'orders_count': orders_count}
    return render(request, 'accounts/customers.html', context)


def createOrder(request):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, "accounts/order_form.html", context)
