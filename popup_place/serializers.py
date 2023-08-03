from rest_framework import serializers
from .models import PopupPlace

class PopupPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopupPlace
        fields = '__all__'
