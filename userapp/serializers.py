from .models import *
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'