from django.db import models
from datetime import datetime

class User(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=255)
    name = models.CharField(blank=False, max_length=30)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

class Shipper(User):
    address = models.TextField(blank=False)

class Transporter(User):
    rating = models.IntegerField(default=0)

class Job(models.Model):
    shipper_id = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING)
    origin = models.CharField(blank=False, max_length=30)
    destination = models.CharField(blank=False, max_length=30)
    description = models.TextField()
    budget = models.IntegerField(blank=False)
    status = models.IntegerField(default=0)
    shipment_date = models.DateField(blank=False)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

class Bid(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
    transporter_id = models.ForeignKey(Transporter, on_delete=models.DO_NOTHING)
    vehicle = models.CharField(blank=False, max_length=30)
    price = models.IntegerField(blank=False)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)