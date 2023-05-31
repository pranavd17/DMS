from rest_framework import serializers
from .models import *

class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = '__all__'

class DepartmentSer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields = '__all__'

class RoleSer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields = '__all__'
