from .models import *
from rest_framework import serializers

class TanlanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlangan
        fields = '__all__'

class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        savat_items = instance.savat.savat_items.all()
        data['savat_itemlari'] = SavatItemSerializer(savat_items, many=True).data

        return data