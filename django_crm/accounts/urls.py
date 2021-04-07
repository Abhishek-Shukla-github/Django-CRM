from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("product", views.product, name="product"),
    path("customer/<str:cust_id>", views.customer, name="customer")
]
