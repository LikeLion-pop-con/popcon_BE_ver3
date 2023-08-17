from rest_framework import serializers
from .models import PopupPlace,PopupPlaceReservation

class PopupPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopupPlace
        fields = '__all__'
        
class PopupPlaceReservationSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = PopupPlaceReservation
        fields = '__all__'  