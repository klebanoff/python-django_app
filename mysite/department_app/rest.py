from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['department_name','employees']

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
    class Meta:
        model = Employee
        fields = ['employee_name', 'date_of_birth', 'salary','department']
