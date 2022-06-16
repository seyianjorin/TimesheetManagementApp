from django.db import models
from userapp.models import Doctor
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=1024, null=False)
    from_hour = models.TimeField(null=True)
    to_hour = models.TimeField(null=True)
    office_number = models.IntegerField()

    def __str__(self):
        return self.name


class Payroll(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class WorkPeriod(models.Model):
    clockIn = models.TimeField()
    clockOut = models.TimeField()
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.firstname + " " + self.doctor.lastname


class Sector(models.Model):
    name = models.CharField(max_length=10, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name







