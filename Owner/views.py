from django.shortcuts import render
from .serializers import OwnerSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def owner_data(request):
    serializer= OwnerSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response({"data":serializer.data,"msg":"Owner Data Created Successfully"},status=200)

