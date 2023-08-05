from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'


class PopupSerializer(serializers.ModelSerializer):
    brand_info=serializers.StringRelatedField()
    popup_category = serializers.StringRelatedField()
    #image = serializers.ImageField(use_url=True)# image를 추가를 위한
    class Meta:
        model = Popup
        fields = '__all__'




