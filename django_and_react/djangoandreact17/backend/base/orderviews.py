from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view, permission_classes
# is admin az is_staff=true miad
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status