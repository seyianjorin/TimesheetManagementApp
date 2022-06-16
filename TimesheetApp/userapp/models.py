from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    specialization = models.CharField(max_length=50, null=False)
    departmentId = models.IntegerField(null=False)
    is_Admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

