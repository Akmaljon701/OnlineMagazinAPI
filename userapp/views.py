from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserCreateAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            valida_data = serializer.data
            valida_data['id'] = user.id
            return Response(valida_data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProfilCreateAPI(APIView):
    def post(self, request):
        serializer = ProfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProfilDetailAPI(APIView):
    def get(self, request):
        profil = Profil.objects.get(user=request.user)
        serializer = ProfilSerializer(profil)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profil = Profil.objects.get(user=request.user)
        serializer =ProfilSerializer(profil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        profil = Profil.objects.filter(user=request.user)
        if profil:
            profil.delete()
            return Response({"xabar": "Profil o'chrildi!"}, status=status.HTTP_200_OK)
        return Response({"xabar": "Xatolik!"}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                login(request, user)
                return Response({"xabar": "Tizimga kiritildi!"}, status=status.HTTP_200_OK)
            return Response({"xabar": "Login yoki parol noto'g'ri!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response({"xabar": "Tizimdan chiqarildi"})

