from django.db import models
from django.db.models import Model, CharField, FloatField


# Create your models here.
class Product(Model):
    description = CharField(max_length=255,null=True,blank=True)


class User(Model):
    name = CharField(max_length=255)
    password = CharField(max_length=255)