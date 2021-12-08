from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Invoice(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    labor = models.IntegerField()
    budget = models.IntegerField()
    motherboard = models.CharField(max_length=100, blank=True)
    processor = models.CharField(max_length=100, blank=True)
    cooler = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=100, blank=True)
    gpu = models.CharField(max_length=100, blank=True)
    case = models.CharField(max_length=100, blank=True)
    fan = models.CharField(max_length=100, blank=True)
    hdd = models.CharField(max_length=100, blank=True)
    ssd = models.CharField(max_length=100, blank=True)
    antivirus = models.BooleanField()
    dust = models.BooleanField()
    new_parts = models.BooleanField()
    notes = models.TextField(blank=True)
    completed = models.BooleanField()
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.email

