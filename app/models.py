from django.db import models

# Create your models here.


class Unit(models.Model):
	name = models.CharField(max_length=200)