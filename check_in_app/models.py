from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.core.validators import MinValueValidator


class Resident(AbstractUser):
    registration_num = models.IntegerField(default=100, blank=True, null=True, validators=[MinValueValidator(0)])
    full_name = models.CharField(max_length=100, default="full_name")
    passport = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['full_name', 'phone']


class TransportType(models.Model):
    type_name = models.TextField(blank=False)
    load_capacity = models.FloatField(validators=[MinValueValidator(0)])
    min_length = models.FloatField(validators=[MinValueValidator(0)])
    max_length = models.FloatField(validators=[MinValueValidator(0)])
    min_width = models.FloatField(validators=[MinValueValidator(0)])
    max_width = models.FloatField(validators=[MinValueValidator(0)])
    high_min = models.FloatField(validators=[MinValueValidator(0)])
    high_max = models.FloatField(validators=[MinValueValidator(0)])
    logo = models.TextField(blank=True)


class Transport(models.Model):
    model_name = models.TextField(blank=False)
    type = models.ForeignKey(TransportType, on_delete=models.CASCADE)
    rent_cost = models.IntegerField(validators=[MinValueValidator(0)])
    length = models.FloatField(validators=[MinValueValidator(0)])
    width = models.FloatField(validators=[MinValueValidator(0)])
    high = models.FloatField(validators=[MinValueValidator(0)])


class Order(models.Model):
    order_name = models.TextField(blank=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transport_id = models.ForeignKey(Transport, on_delete=models.CASCADE)
    time_start = models.IntegerField(blank=False)
    time_end = models.IntegerField(blank=False)

