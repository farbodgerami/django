from tokenize import maybe
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

@api_view(['GET','POST'])
def student_list(request):
    if request.method =='GET':
        students=Student.objects.all()
        # tabdile dataye django be json:
        serializer=Studentserializer(students,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        # tabdile json be dataye django:
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=Studentserializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=Studentserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('deleted')