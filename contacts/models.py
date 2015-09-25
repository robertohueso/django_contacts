from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 50)
    user_id = models.ForeignKey(User, verbose_name = "user_id")

     def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
