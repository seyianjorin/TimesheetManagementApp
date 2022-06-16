from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Doctor
from .forms import DoctorForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'user/register.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'home.html'


class DoctorList(ListView):
    queryset = Doctor.objects.all()
    model = Doctor
    template_name = 'Doctor/doctor_list.html'
    context_object_name = 'doctor_list'


class DoctorDetail(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'Doctor/doctor_detail.html'
    context_object_name = 'doctor'


class CreateDoctor(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'Doctor/create_doctor.html'
    context_object_name = 'form'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super(CreateDoctor, self).form_valid(form)


class UpdateDoctor(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'Doctor/update_doctor.html'
    context_object_name = 'form'
    success_url = reverse_lazy('doctor_list')


