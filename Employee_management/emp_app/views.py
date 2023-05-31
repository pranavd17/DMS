from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.


@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        Emp=Employee.objects.all()
        ser=EmployeeSer(Emp, many=True)
        return Response(ser.data)
    if request.method=='POST':
        Emp=request.data
        ser=EmployeeSer(data=Emp)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,201)
        return Response(400)





