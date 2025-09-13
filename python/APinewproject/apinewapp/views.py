from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializers
from .models import Userdata

# Create your views here.

@api_view(['GET'])
def getUser(request):
    return Response(UserSerializers({"name":"almas","age":22}).data)
