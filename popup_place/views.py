from django.shortcuts import render
from rest_framework import status
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *
from user.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupPlaceSerializer, PopupPlaceReservationSerializer

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
    @swagger_auto_schema(tags=['팝업장소 좋아요 기능'], request_body=openapi.Schema(
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
    


class MyPopupPlaceLike_ListView(APIView):
    user_id_para= openapi.Parameter('id', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    #user_name= openapi.Parameter('user_name', openapi.IN_QUERY, description='이름', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['내가 좋아요한 팝업공간리스트_쿼리로 사용 id=user_pk'])
    def get(self,request):
        user_pk = request.GET.get("id")
        #user_name01 = request.GET.get("user_name")
        #user = User.objects.get(user_name=user_name01)
        user = User.objects.get(id =user_pk)

        popupPlace_list = user.popupplaces
        popupplace_serializer = PopupPlaceSerializer(popupPlace_list,many=True)
        
        return Response(popupplace_serializer.data, status=200)
    
class CheckPopup_PlaceLike(APIView):
    user_id_para= openapi.Parameter('user_pk', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    place_id_para= openapi.Parameter('place_pk', openapi.IN_QUERY, description='place_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['공간대여 좋아요 했나 확인 user_pk=id,place_pk=id'])
    def get(self, request):
        user_pk = request.GET.get("user_pk")
        place_pk = request.GET.get("place_pk")
        user = User.objects.get(id=user_pk)
        place = PopupPlace.objects.get(id=place_pk)
        if user in place.popup_place_like_people.all():
            return Response({"message": "좋아요눌린상태.","like_state":1}, status=200)
        else: 
            return Response({"message": "좋아요안눌린상태.","like_state":0}, status=200)

class PopupPlaceReservationView(APIView):
    
    @swagger_auto_schema(tags=['팝업공간예약'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="user_id"),
            'popup_place_pkey': openapi.Schema(type=openapi.TYPE_INTEGER, description='popup_place_pkey'),
            'reserved_basement_floor': openapi.Schema(type=openapi.TYPE_INTEGER, description='reserved_basement_floor'),
            'reserved_ground_floor': openapi.Schema(type=openapi.TYPE_INTEGER, description='reserved_ground_floor'),
            'reserved_date': openapi.Schema(type=openapi.TYPE_STRING, description='reserved_date'),
        },
        required=['user_id', 'popup_place_pkey','reserved_basement_floor','reserved_ground_floor','reserved_date']
    ), responses={200: 'Success'})
    
    def post(self, request):
        
        # 요청에서 데이터 추출
        user_id = request.data.get('user_id', None)
        popup_place_pkey = request.data.get('popup_place_pkey', None)
        # popup_place_id = request.data.get('popup_place_id', None)
        reserved_basement_floor = request.data.get('reserved_basement_floor', None)
        reserved_ground_floor = request.data.get('reserved_ground_floor', None)
        reserved_date = request.data.get('reserved_date', None)
        
        # 데이터 검증: 필요에 따라 추가 검증을 할 수 있습니다
        if not all([user_id, popup_place_pkey, reserved_basement_floor, reserved_ground_floor, reserved_date]):
            return Response({"detail": "필수 필드가 누락되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"detail": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            popup_place = PopupPlace.objects.get(pk=popup_place_pkey)
        except PopupPlace.DoesNotExist:
            return Response({"detail": "팝업 공간을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 새 PopupPlaceReservation 인스턴스 생성
        reservation = PopupPlaceReservation(
            user=user,
            popupplace=popup_place,
            popupplace_reserved_basement_floor=reserved_basement_floor,
            popupplace_reserved_ground_floor=reserved_ground_floor,
            popupplace_reserved_date=reserved_date
        )
        reservation.save()

        # 생성된 예약 인스턴스 반환
        return Response({"detail": "예약이 성공적으로 생성되었습니다!", "reservation_id": reservation.id}, status=status.HTTP_201_CREATED)


# class PopupPlaceReservationView(APIView):

#     @swagger_auto_schema(tags=['팝업공간예약'])
    
#     def post(self, request):

#         # Serializer를 사용하여 요청 데이터의 유효성 검사 및 처리
#         serializer = PopupPlaceReservationSerializer(data=request.data)

#         # Serializer의 유효성 검사
#         if serializer.is_valid():
#             # 유효한 데이터가 있다면 저장하고 응답 반환
#             serializer.save()

#             return Response({"detail": "예약이 성공적으로 생성되었습니다!", "reservation_id": serializer.instance.id},
#                             status=status.HTTP_201_CREATED)
#         else:
#             # 유효하지 않은 데이터에 대한 응답 반환
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MyPopupPlaceReservations(APIView):
#     @swagger_auto_schema(tags=['내가 예약한 팝업공간'])
#     def get(self,request):
#         popupplaces = PopupPlace.objects.filter
        
class MyPopupPlaceReservations(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='User ID', required=True, type=openapi.TYPE_INTEGER)
    
    @swagger_auto_schema(tags=['내가 예약한 팝업공간'], manual_parameters=[id_param])
    def get(self, request):
        
        # URL 쿼리 파라미터에서 사용자 ID 가져오기
        user_id = request.GET.get("id")
        if not user_id:
            return Response({"detail": "User ID를 제공해주세요."}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)

        # 해당 사용자의 모든 PopupPlaceReservation 객체들을 가져오기
        reservations = PopupPlaceReservation.objects.filter(user=user)

        # 해당 예약들과 연관된 PopupPlace 객체들을 가져오기
        popupplaces = [reservation.popupplace for reservation in reservations]

        # 데이터 직렬화
        serializer = PopupPlaceSerializer(popupplaces, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetAllPopupPlaceIDsAndTitlesView(APIView): #모든 팝업 장소의 id : 장소이름 값 가져오기
    @swagger_auto_schema(tags=['모든 팝업장소의 id : 장소이름'])
    def get(self, request):
        data = [{"id": instance.id, "title": instance.popup_place_title} for instance in PopupPlace.objects.all()]
        return Response({"data": data}, status=200)
#aaa