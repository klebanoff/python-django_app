

from django.db import models
from django.db.models import Avg

# Create your models here.
class Department(models.Model):
    """Department model with one field: department_name"""
    department_name = models.CharField(max_length=200)
    def __str__(self):
        return self.department_name
    def get_avarage_salaty(self):
        """returns avarage salary of related employees"""
        avarage_salary = Employee.objects.filter(department = self.id).aggregate(Avg('salary'))
        return avarage_salary.get('salary__avg')

class Employee(models.Model):
    """Employee model

    Model with 4 fields:
    employee_name
    date_of_birth
    salary
    department - related department as one to many
    """
    department = models.ForeignKey(Department, default = 1,
related_name='employees', on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=200)
    date_of_birth = models.DateField('date of birth')
    salary = models.FloatField(default=0)
    def __str__(self):
        return self.employee_name
