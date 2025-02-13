from django.contrib import admin
from django.urls import path
from Employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_details/<int:id>', views.EmployeeDetail, name="employee_details"),
    path('employee_list/', views.EmployeeList, name="employee_list"),
    path('employee_create/', views.EmployeeCreate, name="employee_create"),
]
