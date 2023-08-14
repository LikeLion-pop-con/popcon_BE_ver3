from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *
from user.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CardSerializer
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema

class CardSignup(APIView):
    @swagger_auto_schema(tags=['카드등록기능'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_pk': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_pk'),
            'account_password': openapi.Schema(type=openapi.TYPE_STRING, description='account_password'),
            'bank': openapi.Schema(type=openapi.TYPE_STRING, description='bank'),
            'bank_account_number': openapi.Schema(type=openapi.TYPE_STRING, description='bank_account_number'),
            'card_number': openapi.Schema(type=openapi.TYPE_STRING, description='card_number'),
            'max_date': openapi.Schema(type=openapi.TYPE_STRING, description='max_date'),
            'cvc': openapi.Schema(type=openapi.TYPE_STRING, description='cvc'),
            'card_password': openapi.Schema(type=openapi.TYPE_STRING, description='card_password'),
            
        },
        required=['user_pk','account_password', 'bank', 'bank_account_number', 'card_number', 'max_date', 'cvc', 'card_password']
    ), responses={200: 'Success'})
    def post(self, request):
        card =Card()
        card.user=User.objects.get(id=request.data.get("user_pk"))
        card.account_password=request.data["account_password"]
        card.bank=request.data["bank"]
        card.bank_account_number=request.data["bank_account_number"]
        card.card_number=request.data["card_number"]
        card.max_date=request.data["max_date"]
        card.cvc=request.data["cvc"]
        card.card_password=request.data["card_password"]

        card.save()
        cardSerializer = CardSerializer(card)
        return Response(cardSerializer.data, status=200) 
    


class CardinfoView(APIView):# card/info/?id=user_id 
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='user pk id', required=True, type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(tags=['카드정보 /id=userpk'], manual_parameters=[id_param])
    
    def get(self, request):

        user_pk = request.GET.get("id")

        # 유저에 해당하는 카드 정보 검색
        cards = Card.objects.filter(user_id=user_pk)

        # Serializer 사용하여 데이터 변환 (many=True 옵션으로 여러 개의 카드 정보 처리)
        cardSerializer = CardSerializer(cards, many=True)

        return Response(cardSerializer.data, status=200) 


class AccountPassword_Check(APIView):# card/info/?id=user_id 
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='user pk id', required=True, type=openapi.TYPE_INTEGER)
    password_param = openapi.Parameter('pw', openapi.IN_QUERY, description='password', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['결제비밀번호확인 쿼리로 id=user_pk,pw=비번'])
    def get(self, request):

        user_pk = request.GET.get("id")
        password = request.GET.get("pw")

        # 유저에 해당하는 카드 정보 검색
        card = Card.objects.filter(user_id=user_pk).first()
        password1=card.account_password
        if password ==password1:
            return Response({"message": "결제성공.","state":1}, status=200)
        else: 
            return Response({"message": "결제실패.","state":0}, status=200)


