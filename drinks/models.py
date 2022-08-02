from unicodedata import decimal
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class Transcription(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    dilatation = models.IntegerField(default=-1)
    temperature = models.DecimalField(max_digits=3, decimal_places=1, default=-1)
    fhr = models.IntegerField(default=-1)
    effacement = models.IntegerField(default=-1)
    drugs = models.CharField(max_length=100, default='n/a')
    bp_systolic = models.IntegerField(default=-1)
    bp_diastolic = models.IntegerField(default=-1)
    discharge = models.CharField(max_length=100, default='n/a')
    pulse = models.IntegerField(default=-1)
    
    def __str__(self):
        return self.name