from django.db import models
from django.contrib.auth.models import User
from workdayapp.models import WorkPeriod, Sector
# Create your models here.


class Doctor(models.Model):
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    specialization = models.CharField(max_length=50, null=False)
    departmentId = models.IntegerField(null=False)
    workPeriod = models.OneToOneField(WorkPeriod, on_delete=models.CASCADE)
    sector = models.OneToOneField(Sector, on_delete=models.CASCADE)
