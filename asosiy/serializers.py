from django.db.models import Avg
from .models import *
from rest_framework import serializers

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields ='__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields ='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Calculate average rating
        average_rating = Izoh.objects.filter(mahsulot=instance).aggregate(ortachasi=Avg('reyting'))['ortachasi']
        # Add average rating to data dictionary
        data['ortacha_rating'] = average_rating
        return data

    def validate_chegrma(self, qiymat):
        if qiymat < 0 or qiymat > 50:
            raise serializers.ValidationError("Chegirma 0 dan kichik yoki 50 dan baland foizda bo'lishi mumkin emas!")
        return qiymat

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields ='__all__'

    def validate_reyting(self, qiymat):
        if qiymat > 5 or qiymat < 1:
            raise serializers.ValidationError("Reyting [1;5] oraliqda bo'lishi shart!")
        return qiymat


