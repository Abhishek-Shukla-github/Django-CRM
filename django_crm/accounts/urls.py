from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="Home"),
    path("product", views.product, name="Product"),
    path("customer/<str:cust_id>", views.customer, name="Customer")
]
