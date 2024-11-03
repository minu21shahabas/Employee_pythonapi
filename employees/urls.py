from django.urls import path
# from .migrations import EmployeeListCreate, EmployeeDetail
from . import views
from .views import EmployeeListCreate, EmployeeDetail


urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]
