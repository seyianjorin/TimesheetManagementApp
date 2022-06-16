

from django.urls import path

from workdayapp.views import WorkperiodList, WorkperiodDetail, CreateWorkperiod, UpdateWorkperiod

urlpatterns = [
    path('', WorkperiodList.as_view(), name='workperiod_list'),
    path('<int:pk>/', WorkperiodDetail.as_view(), name='WorkperiodDetail'),
    path('createworkperiod/', CreateWorkperiod.as_view(), name='create_workperiod'),
    path('<int:pk>/updateworkperiod', UpdateWorkperiod.as_view(), name='update_workperiod'),
    # path('<int:pk>/deleteproduct', DeleteProduct.as_view(), name='product_delete'),
]