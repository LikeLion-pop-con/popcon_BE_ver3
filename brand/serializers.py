from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'


class PopupSerializer(serializers.ModelSerializer):
    brand_info=serializers.StringRelatedField()
    popup_category = serializers.StringRelatedField()
    class Meta:
        model = Popup
        fields = '__all__'

