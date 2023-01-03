from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usercus(AbstractUser):
    # Add additional fields here
    # username, password, email, first_name, last_name those are already there you dont need them to re declare
    # username = models.TextField(null=True, blank=True, unique=True)
    # password = models.TextField(null=True, blank=True)
    # email = models.TextField(null=True, blank=True)
    phonenumber = models.TextField(null=True, blank=True)
