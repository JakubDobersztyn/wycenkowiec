from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=16)
    unit_price = models.FloatField()


class Pricing(models.Model):
    client = models.CharField(max_length=64)
    services = models.ManyToManyField(Service, through='PricingService')
    discount = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class PricingService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    quantity = models.FloatField()

