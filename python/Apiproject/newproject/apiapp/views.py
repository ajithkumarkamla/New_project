from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
from .models import EmployeeUser
from .serializer import UserSerializers

@api_view(['GET'])
def get_Emplooye(request):
    emUser=EmployeeUser.objects.all()
    serializer=(UserSerializers(emUser,many=True))
    # return Response(UserSerializers({"name":"almas","age":20,"email":"almas@gmail.com"}).data)
    return Response(serializer.data)


@api_view(['POST'])
def create_Emp(request):
    serializer= UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    