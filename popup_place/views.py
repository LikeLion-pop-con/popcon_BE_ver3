from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import PopupPlace
from user.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupPlaceSerializer

from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema

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
    
    
    
class PopupPlaceLike_View(APIView):
    @swagger_auto_schema(tags=['팝업장소 좋아요'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'brand_name': openapi.Schema(type=openapi.TYPE_STRING, description='brand_name'),
            'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='user_name'),
        },
        required=['brand_name', 'user_name']
    ), responses={200: 'Success'})
    
    def post(self,request):
        popupplace = PopupPlace.objects.get(popupplace = request.data.get("popup_place_name"))
        user = User.objects.get(user_name=request.data.get("user_name"))
        if user in popupplace.popup_place_like_people.all():
            popupplace.popup_place_like_people.remove(user)
            popupplace.save()
        else:
            popupplace.popup_place_like_people.add(user)
            popupplace.save()
        return Response({"message":popupplace.popup_place_like_people.count()})