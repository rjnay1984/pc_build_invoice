from django.db.models import fields
from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Invoice
        fields = ['email', 'owner', 'completed', 'completed_date']