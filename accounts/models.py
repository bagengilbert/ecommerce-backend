from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#custom user model that extends the built-in abstract user model 
class customUser(AbstractUser):
    phone_Number = models.CharField(max_length=15,blank=True,null=True)
    address = models.TextField(blank=True,null=True)


def __str__(self):
    return self.username




