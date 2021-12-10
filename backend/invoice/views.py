from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import InvoiceSerializer

from .models import Invoice

# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows invoices to be viewed/added/updated/deleted.
    """
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
