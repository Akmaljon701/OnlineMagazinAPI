from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from userapp.models import Profil

class IzohlarAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izohlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            profil = Profil.objects.filter(user=request.user).first()
            serializer.save(profil=profil, mahsulot=Mahsulot.objects.get(id=pk))
            natija = serializer.data
            natija['mahsulot'] = pk
            natija['profil'] = profil.id

            return Response(natija)
        return Response(serializer.errors)


class MahsulotAPIView(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MahsulotlarAPIView(APIView):
    def get(self, request):
        soz = request.query_params.get('qidirish')
        if soz is None or soz == "":
            mahsulotlar = Mahsulot.objects.all()
        else:
            mahsulotlar = Mahsulot.objects.filter(nom__contains=soz)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
