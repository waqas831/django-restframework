from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def viewdata(request):
    data=Student.objects.all()
    print(data)#it collect all the record from database
    data_serial=StudentSerializer(data,many=True)
    print(data_serial)              #collect record from serilalizers that we convert in text or any other format//convert python object
    json_data=JSONRenderer().render(data_serial.data)
    print(json_data)#jsonrendere convert serialized data to json format
    return HttpResponse(json_data,content_type='application/json')     #content_type="" it indicate that request body format is xml

def singleview(request,id):
    data=Student.objects.get(id=id)
    data_serial=StudentSerializer(data)
    json_data=JSONRenderer().render(data_serial.data)
    return HttpResponse(json_data,content_type='application/json')


