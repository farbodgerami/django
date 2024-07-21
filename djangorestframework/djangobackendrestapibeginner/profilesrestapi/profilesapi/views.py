from rest_framework.views import APIView
from rest_framework.views import Response
# vase post darim:
from rest_framework import  status
from profilesapi import serializers 
# vase viewset:
from rest_framework import viewsets
# modelviewset:
from .models import UserProfile, profilefeeditem  
from .serializers import UserProfileserializer, profilefeeditemserializer
# vase permission authentication:
from rest_framework.authentication import TokenAuthentication
from profilesapi import permissions
# vase search:
from rest_framework import filters
# vase login va authentication:
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# to completly restrict otherf from seeng our feed:
from rest_framework.permissions import IsAuthenticated

class Hellowapiview(APIView):
    serializer_class=serializers.helloserializer
    def get(self,request,format=None):
        l=[1,55,3,4]
        return Response({'message':'hello','list':l})
    def post(self,request):
        # agha havaset bashe serializer_class _ mikhad vasatesh vagar na kar nemikone
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'message':'PUT'})
    
    def patch(self,request,pk=None):
        """handle partial of updating an object"""
        return Response({'message':'PATCH'})
    
    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'message':'DELETE'})

class Helloviewset(viewsets.ViewSet):
    serializer_class=serializers.helloserializer
    def list(self,request):
        l=[2,4,54,67]
        return Response({'message':'hello','list':l})
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""
        return Response({"httpmethod":"GET"})
    def update(self,request,pk=None):
         """handle updating an object"""
         return Response({"httpmethod":"PUT"})
    def partial_update(self,request,pk=None):
         """handle updating part of an object"""
         return Response({"httpmethod":"PATCH"})
    def destroy(self,request,pk=None):
         """handle removing an object"""
         return Response({"httpmethod":"DELETE"})

  
class UserProfileviewset(viewsets.ModelViewSet):
    serializer_class=UserProfileserializer
    queryset=UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)#, vasea bade item lazeme ke tuple beshe
    permission_classes=(permissions.updateownprofile,)
    filter_backends=(filters.SearchFilter,)#ye dialogbox vase search misaze
    search_fields=('name','email')

class userloginapiview(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES 
class userprofilefeedviewset(viewsets.ModelViewSet):
    """handles creating,reading and updating profile feed items"""
    authentication_classes=(TokenAuthentication,)
    serializer_class=profilefeeditemserializer
    queryset=profilefeeditem.objects.all()
    # permission_classes=(permissions.updateownstatus,IsAuthenticatedOrReadOnly)
    permission_classes=(permissions.updateownstatus,IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(userprofile=self.request.user)
