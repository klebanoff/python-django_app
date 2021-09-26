from django.urls import path

from . import views

app_name = 'department_app'
urlpatterns = [
    path('',views.departments, name='departments'),
    path('<int:department_id>/', views.department, name='department'),
    path('delete/<int:department_id>/', views.delete_department, name='department_app'),
    path('<int:department_id>/employees', views.employees, name='employees'),
    path('<int:department_id>/employees/<int:employee_id>', views.employee, name='employee'),
    path('<int:department_id>/employees/<int:employee_id>/delete', views.delete_employee, name='department_app'),
    path('<int:department_id>/employees/new_employee', views.new_employee, name='new_employee'),
]
