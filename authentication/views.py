from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def create_user(request):
        data=request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({"msg":"User Created Successfully"},status=200)
