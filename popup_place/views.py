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


class PopupPlaceAllView(APIView):
    def get(self,request):
        popup_places = PopupPlace.objects.all()
        serializer = PopupPlaceSerializer(popup_places,many=True)
        return Response(serializer.data)
        
class PopupPlaceView(APIView):
    
    def get(self, request, pkey=None):# pkey는 장소별로 정리해서 프론트로 전달 
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
            'popup_place_pkey': openapi.Schema(type=openapi.TYPE_INTEGER, description='popup_place_pkey'), #팝업공간의 pkey와 user_name입력
            'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='user_name'),
        },
        required=['popup_place_pkey', 'user_name']
    ), responses={200: 'Success'})
    
    def post(self,request):
        popupplace = PopupPlace.objects.get(pkey = request.data.get("popup_place_pkey"))
        user = User.objects.get(user_name=request.data.get("user_name"))
        if user in popupplace.popup_place_like_people.all():
            popupplace.popup_place_like_people.remove(user)
            popupplace.popup_place_like -=1
            popupplace.save()
        else:
            popupplace.popup_place_like_people.add(user)
            popupplace.popup_place_like +=1
            popupplace.save()
        return Response({"popup_place_like_people.count()":popupplace.popup_place_like_people.count(),"popupplace_like":popupplace.popup_place_like})