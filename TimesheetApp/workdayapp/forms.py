from django import forms
from .models import WorkPeriod


class WorkPeriodForm(forms.ModelForm):

    class Meta:

        model = WorkPeriod

        fields = [
            "doctor",
            "clockIn",
            "clockOut",
            "date",
            "location",
            "payroll",
        ]
