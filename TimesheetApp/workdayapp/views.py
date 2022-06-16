from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WorkPeriod
from .forms import WorkPeriodForm
# Create your views here.


class WorkperiodList(ListView):
    queryset = WorkPeriod.objects.all()
    model = WorkPeriod
    template_name = 'Workperiod/workperiod_list.html'
    context_object_name = 'workperiod_list'


class WorkperiodDetail(LoginRequiredMixin, DetailView):
    model = WorkPeriod
    template_name = 'Workperiod/WorkperiodDetail.html'
    context_object_name = 'WorkperiodDetail'


class CreateWorkperiod(LoginRequiredMixin, CreateView):
    model = WorkPeriod
    form_class = WorkPeriodForm
    template_name = 'Workperiod/create_workperiod.html'
    context_object_name = 'form'
    success_url = reverse_lazy('workperiod_list')


class UpdateWorkperiod(LoginRequiredMixin, UpdateView):
    model = WorkPeriod
    fields = ["clockIn",
            "clockOut",
            "date",
            "location",
            "payroll"]
    # form_class = WorkPeriodForm
    template_name = 'Workperiod/update_workperiod.html'
    context_object_name = 'form'
    success_url = reverse_lazy('workperiod_list')


