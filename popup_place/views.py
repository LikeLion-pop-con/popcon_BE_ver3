from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import PopupPlace

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupPlaceSerializer

# class PopupPlaceAllView(APIView):
#     def get(self,request):
#         popup_places = PopupPlace.objects.all()
#         serializer = PopupPlaceSerializer(popup_places,many=True)
#         return Response(serializer.data)
    
class PopupPlaceView(APIView):
    
    def get(self, request, pkey=None):
        if pkey:
            popup_place = get_object_or_404(PopupPlace, pkey=pkey)
            serializer = PopupPlaceSerializer(popup_place)
        else:
            popup_places = PopupPlace.objects.all()
            serializer = PopupPlaceSerializer(popup_places, many=True)
        return Response(serializer.data)