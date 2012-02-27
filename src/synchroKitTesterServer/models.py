from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=200)
    birthDate   = models.DateField()

class Message(models.Model):
    user    = models.ForeignKey(User)
    text    = models.CharField(max_length=32767)
    
