from rest_framework.decorators import api_view, permission_classes
# is admin az is_staff=true miad
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from base.serializers import *
from base.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password 
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getuser(request):
    users=User.objects.all()
    serializer=Userserializer(users,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuserprofile(request):
    user=request.user
    serializer=Userserializer(user,many=False) 
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getuserbyid(request,id):
    try:
        users=User.objects.get(id=id)
        serializer=Userserializer(users,many=False)
        print(serializer.data)
        # return Response(serializer.data)
        return Response( serializer.data)
    except:
        message={'detail':'not found'}
        return Response(message,status=status.HTTP_404_NOT_FOUND)

        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateuserprofile(request):
    user=request.user
    # chon mikhaim ke tokene jadid ro ham besaze darim:
    serializer=Userserializerwithtoken(user,many=False) 
    data=request.data
    user.first_name=data['name']
    user.username=data['email']
    user.email=data['email']
    if data['password']!='':
        user.password=make_password(data['password'])
    user.save()

    return Response(serializer.data)


@api_view(['POST'])
def registeruser(request):
    data=request.data  
    try:
        user=User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password']))
        serializer=Userserializerwithtoken(user,many=False)
        return Response(serializer.data)
    except:
        message={'detail':'user with this detail already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginman(request):
    from django.contrib.auth import authenticate
    data=request.data
    try:
        user = authenticate(request,username=User.objects.filter(email=data["username"]).values()[0]['username']
        ,password=data["password"])
        serializer=Userserializerwithtoken(user,many=False)
        return Response(serializer.data)
    except:
        user = authenticate(request, username=data["username"], password=data["password"])
        serializer=Userserializerwithtoken(user,many=False)
        return Response(serializer.data)
        
    # return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteuser(request,id):
    userfordeletation=User.objects.get(id=id)
    userfordeletation.delete()
    return Response('user deleted')



        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateuser(request,id):
    user=User.objects.get(id=id)
    data=request.data
    user.first_name=data['name']
    user.username=data['email']
    user.email=data['email']
    user.is_staff=data['isadmin']
    print(user.is_staff)
    user.save()
    serializer=Userserializer(user,many=False) 

    return Response(serializer.data)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
        # print(user.is_staff)
        # token['username'] = user.username
        # token['message'] = 'sesto elemento!!!'
     
        # return token
    def validate(self, attrs):
        data = super().validate(attrs)
        # data['username']=self.user.username
        # data['useremail']=self.user.email
        serializer=Userserializerwithtoken(self.user).data
        # from django.forms.models import model_to_dict
        # print(f'aaaaaaaaaaaaaa{data}')
        # print('ffffffffffffff')
        # print(model_to_dict(self.user))
        # print('ffffffffffffff')
        # print(serializer)
      
        for k,v in serializer.items():
            data[k]=v
        return data
        # return serializer
        # return serializer.items()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
