from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'department_app'
urlpatterns = [
    path('departmentrest/', views.DepartmentList.as_view()),
    path('departmentrest/<int:pk>/', views.DepartmentDetail.as_view()),
    path('employeerest/', views.EmployeeList.as_view()),
    path('employeerest/<int:pk>/', views.EmployeeDetail.as_view()),
    path('',views.departments),
    path('departments/',views.departments, name='departments'),
    path('<int:department_id>/', views.department, name='department'),
    path('delete/<int:department_id>/', views.delete_department, name='delete_department'),
    path('<int:department_id>/employees', views.employees, name='employees'),
    path('<int:department_id>/employees/<int:employee_id>', views.employee, name='employee'),
    path('<int:department_id>/employees/<int:employee_id>/delete', views.delete_employee, name='department_app'),
    path('<int:department_id>/employees/new_employee', views.new_employee, name='new_employee'),
]
