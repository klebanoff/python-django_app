"""
Tests module
"""
from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
# pylint: disable=no-member

from department_app.models import Department, Employee



#class RestTesting(TestCase):
#    def department_serializer_works(self):
#        d=Department.objectss.get(pk=1)
#        e=Employee.objectss.get(pk=1)
#        sd=DepartmentSerializer(d)
#        sd.data
class DepartmentsIndexViev(TestCase):
    """
    Tests of departments list view
    """
    def test_no_departments(self):
        """
        If no departments exist, an appropriate massage is displayed
        """
        response = self.client.get(reverse('department_app:departments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No departments available")
        self.assertQuerysetEqual(response.context['departments_list'], [])

    def test_one_department(self):
        """
        One department should be visible.
        """
        department = Department.objects.create(department_name='test depatrment 1')
        response = self.client.get(reverse('department_app:departments'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['departments_list'], [department])

    def test_two_department(self):
        """
        Two departments should be visible.
        """
        department1 = Department.objects.create(department_name='test depatrment 1')
        department2 = Department.objects.create(department_name='test depatrment 2')
        response = self.client.get(reverse('department_app:departments'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['departments_list'],
            [department2, department1],
            ordered=False
        )

    def test_post_request(self):
        """
        POST request to create department
        """
        client = Client()
        client.post('/department_app/departments/', {'department_name': 'post test department'})
        response = self.client.get(reverse('department_app:departments'))
        self.assertContains(response, "post test department")


class DepartmentViev(TestCase):
    """
    tests of detailed department view
    """
    def test_department_doesnt_exist(self):
        """
        The detail view of department that doesnt exist
        """
        response = self.client.get('1/')
        self.assertEqual(response.status_code, 404)

    def test_department_exist_with_no_empl(self):
        """
        The detail view of department with no employees
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        response = self.client.get(reverse('department_app:department', args=(testdepartment.id,)))
        self.assertEqual(response.status_code, 200)

    def test_post_request_to_rename(self):
        """
        POST request to rename department
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        client = Client()
        client.post(reverse('department_app:department',
                            args=(testdepartment.id,)),
                    {'department_name': 'post rename test department'})
        response = self.client.get(reverse('department_app:department', args=(testdepartment.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'post rename test department')

class DeleteDepartmentView(TestCase):
    """
    test of deletion of department view
    """
    def test_delete_department(self):
        """
        test of deletion of department view
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        client = Client()
        client.get(reverse('department_app:delete_department', args=(testdepartment.id,)),)
        response = self.client.get(reverse('department_app:departments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No departments available")
        self.assertQuerysetEqual(response.context['departments_list'], [])

class EmployeesView(TestCase):
    """
    test of employees list view
    """
    def test_department_exist_with_no_empl(self):
        """
        test of employees list view with no employees
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        response = self.client.get(reverse('department_app:employees', args=(testdepartment.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No employees available")

    def test_department_exist_with_one_empl(self):
        """
        test of employees list view with one employee
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        employee1 = Employee.objects.create(employee_name='employee 1',
                                            date_of_birth='2000-1-1',
                                            salary=200,
                                            department=testdepartment)
        response = self.client.get(reverse('department_app:employees', args=(testdepartment.id,)))
        self.assertQuerysetEqual(response.context['employees_list'], [employee1])
        self.assertEqual(response.status_code, 200)

    def test_department_exist_with_two_empl(self):
        """
        test of employees list view with two employees
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        employee1 = Employee.objects.create(employee_name='employee 1',
                                            date_of_birth='2000-1-1',
                                            salary=200,
                                            department=testdepartment)
        employee2 = Employee.objects.create(employee_name='employee 2',
                                            date_of_birth='2000-1-1',
                                            salary=300,
                                            department=testdepartment)
        response = self.client.get(reverse('department_app:employees', args=(testdepartment.id,)))
        self.assertQuerysetEqual(response.context['employees_list'],
                                 [employee1, employee2],
                                 ordered=False)
        self.assertEqual(response.status_code, 200)

    def test_department_exist_with_two_empl_post_sort(self):
        """
        test of employees list view with two employees with sorting between dates
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        Employee.objects.create(employee_name='employee 2001',
                                date_of_birth='2001-1-1',
                                salary=200,
                                department=testdepartment)
        employee2 = Employee.objects.create(employee_name='employee 1999',
                                            date_of_birth='1999-1-1',
                                            salary=300,
                                            department=testdepartment)
        client = Client()
        response = client.post(reverse('department_app:employees',
                                       args=(testdepartment.id,)),
                               {'date_of_birth_from': '1990-1-1', 'to': '2000-1-1'})
        self.assertQuerysetEqual(response.context['employees_list'], [employee2], ordered=False)
        self.assertEqual(response.status_code, 200)

    def test_department_exist_with_two_empl_post_search(self):
        """
        test of employees list view with two employees with sorting by date
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        employee1 = Employee.objects.create(employee_name='employee 2001',
                                            date_of_birth='2001-1-1',
                                            salary=200,
                                            department=testdepartment)
        Employee.objects.create(employee_name='employee 1999',
                                date_of_birth='1999-1-1',
                                salary=300,
                                department=testdepartment)
        client = Client()
        response = client.post(reverse('department_app:employees', args=(testdepartment.id,)), {'date_of_birth': '2001-1-1'})
        self.assertQuerysetEqual(response.context['employees_list'], [employee1], ordered=False)
        self.assertEqual(response.status_code, 200)

class NewEmployeeView(TestCase):
    """
    Creating new emplyee with new_employee view
    """
    def test_create_new_employee(self):
        """
        Creating new emplyee with new_employee view
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        client = Client()
        response = client.post(reverse('department_app:new_employee',
                                       args=(testdepartment.id,)),
                               {'employee_name': 'new employee',
                                'date_of_birth': '2001-1-1',
                                'salary': '300'})
        response = self.client.get(reverse('department_app:employees', args=(testdepartment.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'new employee')

class ModelTesting(TestCase):
    """
    model testing
    """
    def test_get_avarage_salaty(self):
        """
        get_avarage_salaty() returns avarage salary
        """
        testdepartment = Department.objects.create(department_name='test depatrment 1')
        Employee.objects.create(employee_name='employee 1',
                                date_of_birth='2000-1-1',
                                salary=200,
                                department=testdepartment)
        Employee.objects.create(employee_name='employee 2',
                                date_of_birth='2000-1-1',
                                salary=300,
                                department=testdepartment)
        avarage_salary = testdepartment.get_avarage_salaty()
        self.assertEqual(avarage_salary, 250)
