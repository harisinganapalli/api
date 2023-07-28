from django.shortcuts import render
from .models import *
from  .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
# Create your views here.

@api_view(['GET','POST'])  #api_view`, which is used for writing function-based views with REST framework
def Fruits_list(request,format=None):

    if request.method=="GET":

      data=Fruits.objects.all()
      apidata=Fruits_Serializer(data,many=True)
      return Response({'Fruits':apidata.data}) 
    
    #data=Fruits.objects.all()
    #apidata=Fruits_Serializer(data,many=True)
    #return JsonResponse(apidata.data)
    #when we use this lines we getting a output in json format with getting rest-framework
    
    if request.method=='POST':
       apidata= Fruits_Serializer(data=request.data)
       if apidata .is_valid():
          apidata.save()
          return Response(apidata.data,status.HTTP_201_CREATED )
       

@api_view(['GET','PUT','DELETE'])
def Fruits_detail(request,id,format=None):
  
   try:
       fruit=Fruits.objects.get(pk=id)
   except Fruits.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND )
       

   if request.method=='GET':
       fruitdata=Fruits_Serializer(fruit) 
       return Response(fruitdata.data)
   
   elif request.method=='PUT':
      fruitdata=Fruits_Serializer(fruit, data=request.data)
      if fruitdata .is_valid():
         fruitdata.save()
         return Response(fruitdata.data)
      return Response(fruitdata.errors,status=status.HTTP_400_BAD_REQUEST)
   elif request.method=='DELETE':
      
      fruit.delete()
      return Response(status=status.HTTP_204_NO_CONTENT  )     
            