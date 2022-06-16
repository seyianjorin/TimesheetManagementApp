

from django.urls import path

from userapp import views
from userapp.views import DoctorList, DoctorDetail, CreateDoctor, UpdateDoctor, create_user

urlpatterns = [
    path('', DoctorList.as_view(), name='doctor_list'),
    path('<int:pk>/', DoctorDetail.as_view(), name='doctor_detail'),
    path('createdoctor/', CreateDoctor.as_view(), name='create_doctor'),
    path('<int:pk>/updatedoctor', UpdateDoctor.as_view(), name='update_doctor'),
    path('register/', views.create_user, name='register' ),
    # path('<int:pk>/deleteproduct', DeleteProduct.as_view(), name='product_delete'),
]
