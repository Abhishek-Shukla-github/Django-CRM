from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
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


def createOrder(request):
    form = OrderForm()
    if(request.method == "POST"):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    print(order.customer.name)
    form = OrderForm(instance=order)
    if(request.method == "POST"):
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    print(order)
    if request.method == "POST":
        order.delete()
        return redirect("/")
    context = {'order': order}
    return render(request, "accounts/delete.html", context)
