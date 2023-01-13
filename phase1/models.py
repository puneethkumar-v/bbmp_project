from django.db import models

# Create your models here

class CostSummary(models.Model):
    
    items = models.CharField(max_length=500)
    ars = models.CharField(max_length=100)
    acrs = models.CharField(max_length=100)
