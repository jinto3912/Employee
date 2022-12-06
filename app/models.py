from django.db import models

# Create your models here.

class myemployee(models.Model):
    ename=models.CharField(max_length=30)
    eadd=models.CharField(max_length=40)