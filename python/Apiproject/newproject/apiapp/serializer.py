from rest_framework import serializers
from .models import EmployeeUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= EmployeeUser
        fields= '__all__'