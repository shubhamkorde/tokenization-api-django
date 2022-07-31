from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class Transcription(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    tokens = models.JSONField()
    def __str__(self):
        return self.name