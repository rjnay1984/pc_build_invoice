from django.contrib import admin
from django.db.models import fields

from .models import Invoice

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['email', 'owner', 'completed', 'completed_date']

admin.site.register(Invoice, InvoiceAdmin)