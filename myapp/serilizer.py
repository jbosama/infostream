from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notifications,News


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class CreateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id",'username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        if email not in User.objects.all():
            user=User.objects.create_user(username,email,password)
        return user

class NotificationSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields="__all__"


class NewsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields="__all__"