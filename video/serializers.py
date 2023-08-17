from rest_framework import serializers
from .models import *


class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GifModel
        fields = '__all__'