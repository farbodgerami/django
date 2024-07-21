from pkgutil import ImpImporter
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import helloserializer

class Helloapiview(APIView):
    hser=helloserializer
    def get(self,request,format=None):
        anapiview=['asdf','dfghb']
        # return 'hi'
        return Response({'message':'hello','anapiview':anapiview})

    def post(self,request):
        serializer=helloserializer(data=request.data)
        # serializer=self.hser(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response({'message':message})
            # {"name":"jammes"}
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk=None):
        Response({'method':'put'})
    
    def patch(self,requset, pk=None):
        return Response({'method':'patch'})
    
    def delete(self,requset, pk=None):
        return Response({'method':'delete'})