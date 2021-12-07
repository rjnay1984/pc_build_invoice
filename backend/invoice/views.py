from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer

from .models import Invoice

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows invoices to be viewed.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
