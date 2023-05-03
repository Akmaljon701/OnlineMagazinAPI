from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserCreateAPI.as_view()),
    path('profil/create/', ProfilCreateAPI.as_view()),
    path('profil/', ProfilDetailAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]