from rest_framework import serializers
from .models import *

# class BrandImageSerializer(serializers.ModelSerializer):
    
#     image = serializers.ImageField(use_url=True)
    
#     class Meta:
#         model = BrandImage
#         fields = ['image']

class BrandSerializer(serializers.ModelSerializer):
    
    #images = BrandImageSerializer(many=True, read_only=True,source='brandimage.set')
    class Meta:
        model = Brand
        fields = '__all__'
        
        
    # def create(self,validated_data):
    #     images_data = self.context['request'].FILES
    #     brand = Brand.objects.create(**validated_data)
    #     for image_data in images_data.getlist('image'):
    #         BrandImage.objects.create(brand=brand,image=image_data)
            
    #     return brand        
# class BrandSerializer(serializers.ModelSerializer):
#     images = serializers.SerializerMethodField()
    
#     #images = BrandImageSerializer(many=True, read_only=True)
#     def get_images(self,obj):
#         image = obj.brandimage_set.all()
#         return BrandImageSerializer(instance=image, many=True).data
#     class Meta:
#         model = Brand
#         fields = '__all__'        
#     def create(self, validated_data):
#         instance = Brand.objects.create(**validated_data)
#         image_set = self.context['request'].FILES
#         for image_data in image_set.getlist('image'):
#             BrandImage.objects.create(brand=instance,image=image_data)
            
#         return instance

class PopupSerializer(serializers.ModelSerializer):
    brand_info=serializers.StringRelatedField()
    popup_category = serializers.StringRelatedField()
    #image = serializers.ImageField(use_url=True)# image를 추가를 위한
    class Meta:
        model = Popup
        fields = '__all__'




