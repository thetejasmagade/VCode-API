from rest_framework import serializers
# from .models import User, UserCode, Users
from .models import UserData, Code


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['name', 'email']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['name', 'email']


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['name', 'email', 'codetitle', 'codedescription', 'htmlcode', 'jscode']


class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['name', 'email', 'codetitle', 'codedescription', 'htmlcode', 'jscode']
