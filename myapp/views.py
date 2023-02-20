from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serilizer import*
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import APIView,api_view
from rest_framework .response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Notifications': reverse('Notifications', request=request, format=format),
        'news': reverse('news', request=request, format=format),
        'world': reverse('world', request=request, format=format),
        'economy': reverse('economy', request=request, format=format),
        'sports': reverse('sports', request=request, format=format),
        'weather': reverse('weather', request=request, format=format),
        'entertainment': reverse('entertainment', request=request, format=format),
        'politics': reverse('politics', request=request, format=format),

    })

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id
        token['username'] = user.username
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=CreateUserSerilizer

class UserView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerilizer

class NotificationsViews(generics.ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerilizer

class NewsViews(generics.ListCreateAPIView):
    queryset =  News.objects.filter(category="everything")
    serializer_class = NewsSerilizer

class WorldViews(generics.ListCreateAPIView):
    queryset = News.objects.filter(category="world")
    serializer_class = NewsSerilizer

class SportsViews(generics.ListCreateAPIView):
    queryset =  News.objects.filter(category="sports")
    serializer_class = NewsSerilizer

class EconomyView(generics.ListCreateAPIView):
    queryset = News.objects.filter(category="economy")
    serializer_class = NewsSerilizer

class BussinesViews(generics.ListCreateAPIView):
    queryset =  News.objects.filter(category="bussiness")
    serializer_class = NewsSerilizer

class PoliticsView(generics.ListCreateAPIView):
    queryset = News.objects.filter(category="politics")
    serializer_class = NewsSerilizer

class WeatherView(generics.ListCreateAPIView):
    queryset = News.objects.filter(category="weather")
    serializer_class = NewsSerilizer

class EntertainmentView(generics.ListCreateAPIView):
    queryset = News.objects.filter(category="entertainment")
    serializer_class = NewsSerilizer
