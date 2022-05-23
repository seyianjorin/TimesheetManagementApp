from django.db import models
from userapp.models import Doctor
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=1024, null=False)
    office_hours = models.DurationField()
    office_number = models.IntegerField(max_length=10, null=False)


class WorkPeriod(models.Model):
    clockIn = models.DateTimeField()
    clockOut = models.DateTimeField()
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Payroll(models.Model):
    salary = models.IntegerField(null=False)
    total_work_hours = models.IntegerField(null=False)
    workPeriod = models.ForeignKey(WorkPeriod,on_delete=models.CASCADE)


class Sector(models.Model):
    name = models.CharField(max_length=10, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)








