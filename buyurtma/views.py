from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userapp.models import Profil

from .models import *
from .serializers import *

class TanlanganlarAPIView(APIView):
    def get(self, request):
        tanlanganlar = Tanlangan.objects.filter(profil__user=request.user)
        serializer = TanlanganSerializer(tanlanganlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TanlanganlarDetailAPIView(APIView):
    def get(self, request, pk):
        tanlangan = Tanlangan.objects.get(id=pk, profil__user=request.user)
        serializer = TanlanganSerializer(tanlangan)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        tanlangan = Tanlangan.objects.get(id=pk, profil__user=request.user)
        serializer = TanlanganSerializer(tanlangan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        tanlangan = Tanlangan.objects.filter(id=pk, profil__user=request.user)
        if tanlangan:
            tanlangan.delete()
            return Response({"xabar": "Ma'lumotlar o'chrildi!"})
        return Response({"xabar": "Xarolik!"})

class SavatlarAPIView(APIView):
    def get(self, request):
        savat = Savat.objects.get(profil__user=request.user)
        savat_itemlar = SavatItem.objects.filter(savat=savat)
        serializer = SavatItemSerializer(savat_itemlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SavatItemSerializer(data=request.data)
        savat = Savat.objects.filter(profil__user=request.user)
        if not savat:
            Savat.objects.create(profil=Profil.objects.get(user=request.user))
        savat = Savat.objects.get(profil__user=request.user)
        if serializer.is_valid():
            serializer.save(savat=savat)
            return Response(serializer.data)
        return Response(serializer.errors)

class SavatItemDetailAPIView(APIView):
    def get(self, request, pk):
        savat = SavatItem.objects.get(id=pk, savat__profil__user=request.user)
        serializer = SavatItemSerializer(savat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        savat = SavatItem.objects.get(id=pk, savat__profil__user=request.user)
        serializer = SavatItemSerializer(savat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        savat = SavatItem.objects.filter(id=pk, savat__profil__user=request.user)
        if savat:
            savat.delete()
            return Response({"xabar": "Ma'lumotlar o'chrildi!"})
        return Response({"xabar": "Xatolik!"})

class BuyurtmaDetailView(APIView):
    def get(self, request, pk):
        buyurtma = Buyurtma.objects.get(id=pk)
        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data)

class BuyurtmalarAPIView(APIView):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.filter(profil__user=request.user)
        serializer = BuyurtmaSerializer(buyurtmalar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)