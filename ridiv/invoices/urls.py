# invoices/urls.py
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import InvoiceViewSet, InvoiceDetailViewSet
from . import views


urlpatterns = [
    path('', views.invoice,name="invoice")
]
