from django.http import JsonResponse
from base.products import products
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
def getRouts(request):
    return JsonResponse('hi',safe=False)