# from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status 
# from rest_framework import viewsets 
from rest_framework.decorators import  api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
# Create your views here.

@api_view(['GET'])
@authentication_classes ([SessionAuthentication])
@permission_classes([IsAdminUser])
def Employeeviewset(request):
    if request.method=='GET':
     query=Employee.objects.all()
     employeeserializer=Employeeserializer(query,many=True)
     return Response({'Employee':employeeserializer.data},status=status.HTTP_200_OK)
    