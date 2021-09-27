from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from rest_framework import generics

from .models import Department, Employee
from .rest import DepartmentSerializer, EmployeeSerializer
from .forms import TwoDatesForm, OneDateForm
from django.views import generic


class DepartmentList(generics.ListCreateAPIView):
    """generic class based view of departments using Django REST framework"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """generic class based view of department using Django REST framework"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeList(generics.ListCreateAPIView):
    """generic class based view of employees using Django REST framework"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """generic class based view of employee using Django REST framework"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



def departments(request):
    """list view of all departments"""
    departments_list = Department.objects.all()
    if request.method == "POST":
        department = Department(department_name = request.POST.get("department_name"))
        department.save()
        return HttpResponseRedirect(reverse('department_app:departments') )
    else:
        return render(request, "department_app/departments.html",
    {'departments_list': departments_list})


def department(request, department_id):
    """list view of one department"""
    department= Department.objects.get(pk=department_id)
    if request.method == "POST":
        department.department_name = request.POST.get("department_name")
        department.save()
        return HttpResponseRedirect(reverse('department_app:department', args=(department_id,)) )
    else:
        return render(request, "department_app/department.html",
    {'department': department})

def delete_department(request, department_id):
    """view for deleting departments"""
    try:
        department = Department.objects.get(id=department_id)
        department.delete()
        return HttpResponseRedirect(reverse('department_app:departments'))
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Department not found</h2>")

def employees(request, department_id):
    """view of all employees"""
    context ={}
    form2dates = TwoDatesForm()
    form1date = OneDateForm()
    employees_list = Employee.objects.filter(department = department_id)
    context =  {'employees_list': employees_list, 'form1': form2dates, 'form2' : form1date}
    if request.POST:
        if request.POST.get('date_of_birth') is None:
            date_from = request.POST.get('date_of_birth_from')
            date_to = request.POST.get('to')
            employees_list = Employee.objects.filter(department = department_id).filter(date_of_birth__gte = date_from).filter(date_of_birth__lte = date_to)
            print(employees_list)
            context =  {'employees_list': employees_list, 'form1': form2dates, 'form2' : form1date}
        elif request.POST.get('date_of_birth_from') is None:
            date = request.POST.get('date_of_birth')
            employees_list = Employee.objects.filter(department = department_id).filter(date_of_birth = date)
            print(employees_list)
            context =  {'employees_list': employees_list, 'form1': form2dates, 'form2' : form1date}
    return render(request, "department_app/employees.html",context)

def new_employee(request, department_id):
    """view for creating employees"""
    depart = Department.objects.get(id = department_id)
    context = {'department': depart}
    if request.method == "POST":
        employee = Employee(department = depart)
        employee.employee_name = request.POST.get("employee_name")
        employee.date_of_birth = request.POST.get("date_of_birth")
        employee.salary = request.POST.get("salary")
        employee.save()
        return HttpResponseRedirect(reverse('department_app:employees', args=(department_id,)) )
    else:
        return render(request, "department_app/new_employee.html",context)

def delete_employee(request,department_id,employee_id):
    """view for deleting employees"""
    try:
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return HttpResponseRedirect(reverse('department_app:departments'))
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Employee not found</h2>")

def employee(request,department_id,employee_id):
    """detaided view of an employee"""
    employee = Employee.objects.get(id = employee_id)
    context = {'employee': employee}
    if request.method == "POST":
        employee.employee_name = request.POST.get("employee_name")
        employee.date_of_birth = request.POST.get("date_of_birth")
        employee.salary = request.POST.get("salary")
        employee.save()
        return HttpResponseRedirect(reverse('department_app:employee', args=(department_id,employee_id,)) )
    else:
        return render(request, "department_app/employee.html",context)
