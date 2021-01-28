from rest_framework import serializers    #  serializer it conver the complex data into text or any other format
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    fname = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()
    semester = serializers.IntegerField()
    city = serializers.CharField(max_length=40)