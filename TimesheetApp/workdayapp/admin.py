from django.contrib import admin
from .models import Payroll, WorkPeriod, Sector, Location
admin.site.register(Payroll)
admin.site.register(WorkPeriod)
admin.site.register(Sector)
admin.site.register(Location)
# Register your models here.
