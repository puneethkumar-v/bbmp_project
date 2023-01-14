from django.db import models

# Create your models here


class CostSummary(models.Model):

    items = models.CharField(max_length=500)
    ars = models.CharField(max_length=100)
    acrs = models.CharField(max_length=100)


class RoadCostSummary(models.Model):
    roadid = models.CharField(max_length=150, null=True, blank=True)
    rname = models.CharField(max_length=400)
    ars = models.CharField(max_length=100)
    acrs = models.CharField(max_length=100)


class BOQ(models.Model):
    desc = models.CharField(max_length=5000, null=True, blank=True)
    unit = models.CharField(max_length=100, null=True, blank=True)
    no = models.CharField(max_length=100, null=True, blank=True)
    q = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.CharField(max_length=500, null=True, blank=True)
    amount = models.CharField(max_length=2000)


class R1_1(models.Model):
    no = models.CharField(max_length=500, null=True, blank=True)
    l = models.CharField(max_length=500, null=True, blank=True)
    w = models.CharField(max_length=500, null=True, blank=True)
    d = models.CharField(max_length=500, null=True, blank=True)
    q = models.CharField(max_length=500)
