from django.test import TestCase

# Create your tests here.

from department_app.models import Department, Employee
from department_app.rest import DepartmentSerializer, EmployeeSerializer

class RestTesting(TestCase):
    def department_serializer_works(self):
        d = Department.objects.get(pk=1)
        e = Employee.objects.get(pk=1)
        sd = DepartmentSerializer(d)
        sd.data
        
