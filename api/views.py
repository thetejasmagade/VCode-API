from django.shortcuts import render
from rest_framework import generics
# from .models import User, UserCode,  Users
# from .serializers import UserSerializer, UserCodeSerializer, UsersSerializer
from .models import UserData, Code
from .serializers import UserSerializer, UsersSerializer, CodeSerializer, CodesSerializer


# Create your views here.

class User(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    # queryset = UserData.objects.all()

    def get_queryset(self):
        email = self.kwargs['email']
        return UserData.objects.filter(email=email)


class Users(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UsersSerializer


class UserCode(generics.ListCreateAPIView):
    # queryset = Code.objects.all()
    serializer_class = CodeSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        codetitle = self.kwargs['codetitle']
        return Code.objects.filter(email=email, codetitle=codetitle)


class Codes(generics.ListCreateAPIView):
    # queryset = Codes.objects.all()
    serializer_class = CodesSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return Code.objects.filter(email=email)
