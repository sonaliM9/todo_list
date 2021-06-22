from django.db import models
from django.http import request

# Create your models here.
class TodoModel(models.Model):
    work = models.CharField(max_length=500)
