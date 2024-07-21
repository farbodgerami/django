from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
def employeeview(request):
    emp={'id':123,'name':'james','salary':1000,}
    data=Employee.objects.all()
    # data queryset hast va bayad be soorate json dar biad:
    # print(list(data.values()))
    response={'employees':list(data.values('name','sal'))}
    # return Response({'emp':emp})
    return JsonResponse(response)
    # nokte in ke farghe filter ba get ine ke filter array bar migardoone.