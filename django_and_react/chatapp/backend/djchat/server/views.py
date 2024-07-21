from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError ,AuthenticationFailed
# Create your views here.
from .serializer import*
from django.db.models import Count
from .schema import *
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

class ServerListViewSet(viewsets.ViewSet):
    # permission_classes=(IsAuthenticated,)
    queryset=Server.objects.all()
    # print(queryset)
    @server_list_docs
    def list(self,request):
        # in queryparam haro neshoon mide.
        # print(request.query_params)
        # in oon queryparami ro ke mikhaim migire
        category=request.query_params.get('category')
        qty=request.query_params.get("qty")
        by_user=request.query_params.get('by_user')=='true'
        by_serverid=request.query_params.get('by_serverid')
        with_num_members= request.query_params.get("with_num_members")=='true'
        # print(request.user.is_authenticated)
        # if by_user or by_serverid and not request.user.is_authenticated:
            #  raise AuthenticationFailed(detail='dddddddddddddddddddd')
            #  raise AuthenticationFailed()
            #  raise ValidationError(detail=f"Ser          fdund")

        if category:
            # dar khate pain ?category=2 yani id  ro dar nazar migire:
            # self.queryset=self.queryset.filter(category=category)
            # age bekhaim name bedim masalan category=cat1 darim:
            # serverhai ro bir ke categorishoon folan esm bashe
            self.queryset=self.queryset.filter(category__name=category)

        if by_user:
            if by_user and not request.user.is_authenticated:
                    
                user_id=request.user.id
                self.queryset=self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()
        if by_serverid:
            try:
                self.queryset=self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                return ValidationError(detail='server value error')

        if with_num_members:
        #     # in ro tavajjoh kon 
        #     # annotate ye osve jadid dar har kodoom az objecthaye liste queryset dorost mikone:
            self.queryset=self.queryset.annotate(num_members=Count("member"))
        # az tedadi ke peida kardi in meghdar namayesh bede.
        if qty:
            self.queryset=self.queryset[: int(qty)]

        serializer=ServerSerializer(self.queryset,many=True,context={"num_members":with_num_members})
        return Response(serializer.data)



# # Define a viewset class for handling server list requests
# class ServerListViewSet(viewsets.ViewSet):
#     # Define a queryset containing all Server objects
#     queryset = Server.objects.all()

#     # Define a method to handle HTTP GET requests for listing servers
#     def list(self, request):
#         # Extract query parameters from the request
#         category = request.query_params.get('category')
#         qty = request.query_params.get("qty")
#         by_user = request.query_params.get('by_user') == 'true'
#         by_serverid = request.query_params.get('by_serverid')
#         with_num_members = request.query_params.get("with_num_members") == 'true'

#         # Check if the request is filtered by user or server ID and the user is not authenticated
#         if by_user or by_serverid and not request.user.is_authenticated:
#             raise AuthenticationFailed()

#         # Filter the queryset based on the 'category' query parameter
#         if category:
#             self.queryset = self.queryset.filter(category__name=category)

#         # Filter the queryset based on the authenticated user
#         if by_user:
#             user_id = request.user.id
#             self.queryset = self.queryset.filter(member=user_id)
        
#         # Filter the queryset based on the 'by_serverid' query parameter
#         if by_serverid:
#             try:
#                 self.queryset = self.queryset.filter(id=by_serverid)
#                 if not self.queryset.exists():
#                     raise ValidationError(detail=f"Server with id {by_serverid} not found")
#             except ValueError:
#                 return ValidationError(detail='server value error')

#         # Annotate the queryset with the number of members if 'with_num_members' is True
#         if with_num_members:
#             self.queryset = self.queryset.annotate(num_members=Count("member"))

#         # Limit the queryset to the specified quantity if 'qty' is provided
#         if qty:
#             self.queryset = self.queryset[:int(qty)]

#         # Serialize the queryset and return the response
#         serializer = ServerSerializer(self.queryset, many=True, context={"num_members": with_num_members})
#         return Response(serializer.data)
    
class CategoryListViewSet(viewsets.ViewSet):
    # @extend_schema(responses=CategorySerializer)
    def list(self,request):
        queryset=Category.objects.all()
        print(queryset)
        serializer=CategorySerializer(queryset,many=True)
        # print(serializer.data)
        return Response(serializer.data)