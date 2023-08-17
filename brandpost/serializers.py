from rest_framework import serializers
from .models import *
from brand.models import *


class BrandPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brandpost
        fields = '__all__'