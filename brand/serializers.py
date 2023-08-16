from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
    
    #images = BrandImageSerializer(many=True, read_only=True,source='brandimage.set')
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


class RequestPopupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popup
        #fields = ['id','popup_name', 'popup_main_image']
        fields = '__all__'


class PopupReservationSerializer(serializers.ModelSerializer):
    #popup_main_image = serializers.ImageField(source='popup.popup_main_image', read_only=True)
    popup = PopupSerializer(read_only=True)

    class Meta:
        model = PopupReservation
        fields = '__all__'


