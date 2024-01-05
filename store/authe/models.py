from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    landmark = models.CharField(max_length = 100)
    contact_number = models.CharField(max_length = 100)
    