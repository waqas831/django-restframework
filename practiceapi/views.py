from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail
from .serializers import Detailserializers
from rest_framework.renderers import JSONRenderer
# Create your views here.
def index(request):
    return HttpResponse("welcome to the practice")

def see(request):
    data=Detail.objects.all()
    data_convert=Detailserializers(data,many=True)
    data_json=JSONRenderer().render(data_convert.data)
    return HttpResponse(data_json,content_type='application/json')

def seeone(request,id):
    data=Detail.objects.get(id=id)
    data_convert=Detailserializers(data)
    data_json=JSONRenderer().render(data_convert.data)
    return HttpResponse(data_json,content_type='application/json')

