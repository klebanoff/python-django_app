from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

from department_app.models import Department, Employee
from department_app.rest import DepartmentSerializer, EmployeeSerializer



#class RestTesting(TestCase):
#    def department_serializer_works(self):
#        d = Department.objects.get(pk=1)
#        e = Employee.objects.get(pk=1)
#        sd = DepartmentSerializer(d)
#        sd.data
class DepartmentsIndexViev(TestCase):
    def test_no_departments(self):
        """
        If no departments exist, an appropriate massage is displayed
        """
        response = self.client.get(reverse('department_app:departments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No departments available")
        self.assertQuerysetEqual(response.context['departments_list'], [])

class ModelTesting(TestCase):
    def test_get_avarage_salaty(self):
        """
        get_avarage_salaty() returns avarage salary
        """
