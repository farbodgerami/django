from ast import Delete
from tokenize import maybe
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny,DjangoModelPermissionsOrAnonReadOnly
# class Studentpagination(PageNumberPagination):
#     # this changes the number of contents from here instead of settings.py
#     page_size=2

# class Studentviewset(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer
#     # to add page number to drf page:
#     # pagination_class=PageNumberPagination
#     # to use the custom class:
#     # pagination_class=Studentpagination
    # pagination_class=LimitOffsetPagination





################################################################################
# class student_list(generics.ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer

# class student_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer

################################################################################
# class student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)


# class student_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk) 
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


################################################################################
#  yek crude kamel be raveshe sonnati va classbase:
class student_list(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=Studentserializer(students,many=True)
        return Response(serializer.data)
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
class student_detail(APIView):
    # refactor the code:
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # return Response(status=status.HTTP_404_NOT_FOUND)
            return Http404

    def get(self,request,pk):
        print(request)
        student=self.get_object(pk)
        serializer=Studentserializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student=self.get_object(pk)
        serializer=Studentserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('deleted')


# ?????????????????????????????????????????????
# viewset

class Userviewset(viewsets.ModelViewSet):
         queryset=User.objects.all()
         serializer_class=Userserializer
        #  dar tamame viewset ha hardo bayad bashan
         authentication_classes=[TokenAuthentication]
         permission_classes=[AllowAny]
from rest_framework.authtoken.views import ObtainAuthToken

class Customobtainauthtoken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        # agha inja mitoonim email ro biarim ba trycatch email ro be username tabdil konim
         
        response=super().post(request,*args,**kwargs)
        # return Response( response.data )
        token=Token.objects.get(key=response.data['token'])
        user=User.objects.get(id=token.user_id)
        userserializer=Userserializer(user,many=False)
        return Response({'token':token.key,'user':userserializer.data})
    # permission_classes=[IsAuthenticated]