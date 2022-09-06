from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)