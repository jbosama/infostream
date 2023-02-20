from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView

urlpatterns=[ 
    path("",views.api_root,name="api_root"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/", views.UserView.as_view(), name="user"),
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("Notifications/", views.NotificationsViews.as_view(),name="Notifications"),
    path("news/", views.NewsViews.as_view(),name="news"),
    path("world/", views.WorldViews.as_view(),name="world"),
    path("economy/", views.EconomyView.as_view(),name="economy"),
    path("bussiness/", views.BussinesViews.as_view(),name="bussiness"),
    path("sports/", views.SportsViews.as_view(),name="sports"),
    path("weather/", views.WeatherView.as_view(),name="weather"),
    path("entertainment/", views.EntertainmentView.as_view(),name="entertainment"),
    path("politics/", views.PoliticsView.as_view(),name="politics"),



]




