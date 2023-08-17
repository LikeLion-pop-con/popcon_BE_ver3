from django.shortcuts import render
from rest_framework import status
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *
from user.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupSerializer,BrandSerializer,PopupReservationSerializer,RequestPopupSerializer

from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema



class AllBrand_listView(APIView):
    def get(self,request):
        all_brand_list=Brand.objects.all()
        brandlistSerializer=BrandSerializer(all_brand_list,many=True)
        return Response(brandlistSerializer.data,status=200)
    
class AllPopup_listView(APIView):
    def get(self,request):
        all_popup_list=Popup.objects.all()
        popuplistSerializer=PopupSerializer(all_popup_list,many=True)
        return Response(popuplistSerializer.data,status=200)


class OpenedPopup_listView(APIView):
    def get(self,request):
        opened_popup_list=Popup.objects.filter(popup_state=1)
        popuplistSerializer=PopupSerializer(opened_popup_list,many=True)
        return Response(popuplistSerializer.data,status=200)

class willOpenPopup_listView(APIView):
    def get(self,request):
        willopen_popup_list=Popup.objects.filter(popup_state=2)
        popuplistSerializer=PopupSerializer(willopen_popup_list,many=True)
        return Response(popuplistSerializer.data,status=200)

class SearchView(APIView):
    def get(self, request, search_name):
        # 먼저 popup_name으로 검색해봅니다.
        popups = Popup.objects.filter(popup_name__icontains=search_name)
        brands = Brand.objects.filter(brand_name__icontains=search_name)
        if popups.exists() or brands.exists():
            # popup_name이 존재하는 경우, 해당 Popup을 리턴합니다.
            popup_serializer = PopupSerializer(popups, many=True)
            brand_serializer = BrandSerializer(brands, many=True)
            combined_data = {
                "brands": brand_serializer.data,
                "popups": popup_serializer.data,
            }
            return Response(combined_data, status=200)
        else:
            # Brand도 존재하지 않는 경우 에러 메시지를 리턴합니다.
            error_message = {"message": "검색 결과가 없습니다."}
            return Response(error_message, status=404)
        

class CategoryPopup_listView(APIView):
    @swagger_auto_schema(tags=['팝업카테고리_1,2,3,4 _진행중인팝업'])
    def get(self,request,input):
        if input==1:
            popups=Popup.objects.filter(popup_category=5,popup_state=1)#스토어
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==2:
            popups=Popup.objects.filter(popup_category=6,popup_state=1)#갤러리
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==3:
            popups=Popup.objects.filter(popup_category=7,popup_state=1)#스테이지
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==4:
            popups=Popup.objects.filter(popup_category=8,popup_state=1)#클래스
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        


class CategoryPopuping_listView(APIView):
    @swagger_auto_schema(tags=['팝업카테고리_1,2,3,4 _신청중인팝업'])
    def get(self,request,input):
        if input==1:
            popups=Popup.objects.filter(popup_category=5,popup_state=2)#스토어
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==2:
            popups=Popup.objects.filter(popup_category=6,popup_state=2)#갤러리
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==3:
            popups=Popup.objects.filter(popup_category=7,popup_state=2)#스테이지
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==4:
            popups=Popup.objects.filter(popup_category=8,popup_state=2)#클래스
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        

class CategoryPopupEnd_listView(APIView):
    @swagger_auto_schema(tags=['팝업카테고리_1,2,3,4 _종료된 팝업'])
    def get(self,request,input):
        if input==1:
            popups=Popup.objects.filter(popup_category=5,popup_state=3)#스토어
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==2:
            popups=Popup.objects.filter(popup_category=6,popup_state=3)#갤러리
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==3:
            popups=Popup.objects.filter(popup_category=7,popup_state=3)#스테이지
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)
        
        elif input==4:
            popups=Popup.objects.filter(popup_category=8,popup_state=3)#클래스
            popuplistSerializer=PopupSerializer(popups,many=True)
            return Response(popuplistSerializer.data,status=200)

class CategoryBrand_listView(APIView):
    @swagger_auto_schema(tags=['브랜드+아티스트 카테고리/1~5브랜드 6~9아티스트'])

    def get(self,request,input):
        if input==1:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==2:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==3:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==4:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==5:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==6:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==7:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==8:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)
        elif input==9:
            brands=Brand.objects.filter(brand_category=input)
            brandlistSerializer=BrandSerializer(brands,many=True)
            return Response(brandlistSerializer.data,status=200)


class NewBrand_listView(APIView):
    @swagger_auto_schema(tags=['새로운브랜드 list'])
    def get(self,request):
        brands=Brand.objects.all().order_by('-brand_borndate')
        brandlistSerializer=BrandSerializer(brands,many=True)
        return Response(brandlistSerializer.data,status=200)


class HotPopup_listView(APIView):
    @swagger_auto_schema(tags=['예매가능인기팝업 list'])
    def get(self,request):
        popups=Popup.objects.filter(popup_state=2).order_by('-popup_like')
        popuplistSerializer=PopupSerializer(popups,many=True)
        return Response(popuplistSerializer.data,status=200)
    
class HotBrand_listView(APIView):
    @swagger_auto_schema(tags=['구독수에따른인기브랜드및아티스트 list'])
    def get(self,request):
        brands=Brand.objects.order_by('-brand_subcounts')
        brandlistSerializer=BrandSerializer(brands,many=True)
        return Response(brandlistSerializer.data,status=200)

class BrandLike_View(APIView):
    @swagger_auto_schema(tags=['브랜드좋아요'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "brand_pk": openapi.Schema(type=openapi.TYPE_INTEGER, description="brand_pk"),
            'user_pk': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_pk'),
        },
        required=['brand_pk', 'user_pk']
    ), responses={200: 'Success'})

    def post(self, request):
        brand = Brand.objects.get(id = request.data.get("brand_pk"))         
        user = User.objects.get(id=request.data.get("user_pk"))
        if user in brand.brand_like_people.all():
            brand.brand_like_people.remove(user)
            brand.save()
        else:
            brand.brand_like_people.add(user)
            brand.save()
        return Response({"message":brand.brand_like_people.count()})
    

class BrandSubscribe_View(APIView):
    @swagger_auto_schema(tags=['브랜드구독'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "brand_pk": openapi.Schema(type=openapi.TYPE_INTEGER, description="brand_pk"),
            'user_pk': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_pk'),
        },
        required=['brand_pk', 'user_pk']
    ), responses={200: 'Success'})

    def post(self, request):
        brand = Brand.objects.get(id = request.data.get("brand_pk"))         
        user = User.objects.get(id=request.data.get("user_pk"))
        if user in brand.brand_subscribe_people.all():
            brand.brand_subscribe_people.remove(user)
            brand.brand_subcounts -=1
            brand.save()
        else:
            brand.brand_subscribe_people.add(user)
            brand.brand_subcounts +=1
            brand.save()
        return Response({"brand_subscribe_people.count()":brand.brand_subscribe_people.count(),"brand_subcounts":brand.brand_subcounts})


class MyBrandLikeList(APIView):
    
    user_id_para= openapi.Parameter('id', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['내가 좋아요한 브랜드목록_쿼리로 사용 id=user_pk'])
    def get(self, request):
        
        user_pk = request.GET.get("id")
        user = User.objects.get(id=user_pk)
        brand_list = user.brands
        brand_serializer = BrandSerializer(brand_list, many=True)

        return Response(brand_serializer.data, status=200)
    
class MyBrandSubscribeList(APIView):
    
    user_id_para= openapi.Parameter('id', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['내가 구독한 브랜드목록_쿼리로 사용 id=user_pk'])
    def get(self, request):
        
        user_pk = request.GET.get("id")
        user = User.objects.get(id=user_pk)
        brand_list = user.subscribe_brands
        brand_serializer = BrandSerializer(brand_list, many=True)

        return Response(brand_serializer.data, status=200)



class CheckBradnLike(APIView):
    user_id_para= openapi.Parameter('user_pk', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    brand_id_para= openapi.Parameter('brand_pk', openapi.IN_QUERY, description='brand_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['브랜드 좋아요 했나 확인 user_pk=id,brand_pk=id'])
    def get(self, request):
        user_pk = request.GET.get("user_pk")
        brand_pk = request.GET.get("brand_pk")
        user = User.objects.get(id=user_pk)
        brand = Brand.objects.get(id=brand_pk)
        if user in brand.brand_like_people.all():
            return Response({"message": "좋아요눌린상태.","like_state":1}, status=200)
        else: 
            return Response({"message": "좋아요안눌린상태.","like_state":0}, status=200)
        

class CheckBradnSubscribe(APIView):
    user_id_para= openapi.Parameter('user_pk', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    brand_id_para= openapi.Parameter('brand_pk', openapi.IN_QUERY, description='brand_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['브랜드 구독 했나 확인 user_pk=id,brand_pk=id'])
    def get(self, request):
        user_pk = request.GET.get("user_pk")
        brand_pk = request.GET.get("brand_pk")
        user = User.objects.get(id=user_pk)
        brand = Brand.objects.get(id=brand_pk)
        if user in brand.brand_subscribe_people.all():
            return Response({"message": "구독눌린상태.","subscribe_state":1}, status=200)
        else: 
            return Response({"message": "구독안눌린상태.","subscribe_state":0}, status=200)


class PopupLike_View(APIView):
    @swagger_auto_schema(tags=['팝업좋아요'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "popup_pk": openapi.Schema(type=openapi.TYPE_INTEGER, description="popup_pk"),
            'user_pk': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_pk'),
        },
        required=["popup_pk", 'user_pk']
    ), responses={200: 'Success'})

    def post(self, request):

        popup = Popup.objects.get(id = request.data.get("popup_pk"))         
        user = User.objects.get(id=request.data.get("user_pk"))
    
        if user in popup.popup_like_people.all():
            popup.popup_like_people.remove(user)
            popup.popup_like -=1
            popup.save()
            state=0
        else:
            popup.popup_like_people.add(user)
            popup.popup_like +=1
            popup.save()
            state=1
        return Response({"total_like":popup.popup_like,"mystate":state})
    
class PopupRequset_View(APIView):
    @swagger_auto_schema(tags=['팝업요청'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "popup_pk": openapi.Schema(type=openapi.TYPE_INTEGER, description="popup_pk"),
            'user_pk': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_pk'),
        },
        required=["popup_pk", 'user_pk']
    ), responses={200: 'Success'})

    def post(self, request):

        popup = Popup.objects.get(id = request.data.get("popup_pk"))         
        user = User.objects.get(id=request.data.get("user_pk"))
    
        if user in popup.popup_request_people.all():
            popup.popup_request_people.remove(user)
            if '서울특별시' in user.user_address:
                popup.Seoul -= 1
            elif '부산광역시' in user.user_address:
                popup.Busan -= 1
            elif '인천광역시' in user.user_address:
                popup.Incheon -= 1
            elif '대구광역시' in user.user_address:
                popup.Daegu -= 1
            elif '대전광역시' in user.user_address:
                popup.Daejeon -= 1
            elif '광주광역시' in user.user_address:
                popup.Gwangju -= 1
            elif '울산광역시' in user.user_address:
                popup.Ulsan -= 1
            elif '세종특별자치시' in user.user_address:
                popup.Sejong -= 1
            elif '경기도' in user.user_address:
                popup.Gyeonggi_Province -= 1
            elif '강원도' in user.user_address:
                popup.Gangwon_Province -= 1
            elif '충청북도' in user.user_address:
                popup.Chungcheongbuk_Province -= 1
            elif '충청남도' in user.user_address:
                popup.Chungcheongnam_Province -= 1
            elif '전라북도' in user.user_address:
                popup.Jeollabuk_Province -= 1
            elif '전라남도' in user.user_address:
                popup.Jeollanam_Province -= 1
            elif '경상북도' in user.user_address:
                popup.Gyeongsangbuk_Province -= 1
            elif '경상남도' in user.user_address:
                popup.Gyeongsangnam_Province -= 1
            elif '제주특별자치도' in user.user_address:
                popup.Jeju_Special_Self_Governing_Province -= 1
            popup.save()
            state=0
        else:
            popup.popup_request_people.add(user)
            if '서울특별시' in user.user_address:
                popup.Seoul += 1
            elif '부산광역시' in user.user_address:
                popup.Busan += 1
            elif '인천광역시' in user.user_address:
                popup.Incheon += 1
            elif '대구광역시' in user.user_address:
                popup.Daegu += 1
            elif '대전광역시' in user.user_address:
                popup.Daejeon += 1
            elif '광주광역시' in user.user_address:
                popup.Gwangju += 1
            elif '울산광역시' in user.user_address:
                popup.Ulsan += 1
            elif '세종특별자치시' in user.user_address:
                popup.Sejong += 1
            elif '경기도' in user.user_address:
                popup.Gyeonggi_Province += 1
            elif '강원도' in user.user_address:
                popup.Gangwon_Province += 1
            elif '충청북도' in user.user_address:
                popup.Chungcheongbuk_Province += 1
            elif '충청남도' in user.user_address:
                popup.Chungcheongnam_Province += 1
            elif '전라북도' in user.user_address:
                popup.Jeollabuk_Province += 1
            elif '전라남도' in user.user_address:
                popup.Jeollanam_Province += 1
            elif '경상북도' in user.user_address:
                popup.Gyeongsangbuk_Province += 1
            elif '경상남도' in user.user_address:
                popup.Gyeongsangnam_Province += 1
            elif '제주' in user.user_address:
                popup.Jeju_Special_Self_Governing_Province += 1
            popup.save()
            state=1
        return Response({"total_request":popup.popup_request_people.count(),"request_state":state})





class MyPopupLikeList(APIView):
    id_para= openapi.Parameter('id', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)   
    @swagger_auto_schema(tags=['내가 좋아요한 팝업목록_쿼리로 사용 id=user_pk'])
    def get(self, request):
        pk = request.GET.get("id")
        user = User.objects.get(id=pk)
        popup_list = user.popups
        popup_serializer = PopupSerializer(popup_list, many=True)
        return Response(popup_serializer.data, status=200)
    
class MyPopupReservationList(APIView):
    id_para= openapi.Parameter('id', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)   
    @swagger_auto_schema(tags=['내가 요청한 팝업목록_쿼리로 사용 id=user_pk'])
    def get(self, request):
        pk = request.GET.get("id")
        user = User.objects.get(id=pk)
        requestpops=user.request_popups
        
        request_serializer=PopupSerializer(requestpops, many=True)
    
        
        return Response(request_serializer.data, status=200)



    
class CheckPopupLike(APIView):
    user_id_para= openapi.Parameter('user_pk', openapi.IN_QUERY, description='user_id', required=True, type=openapi.TYPE_INTEGER)
    popup_id_para= openapi.Parameter('popup_pk', openapi.IN_QUERY, description='popup_id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['팝업 좋아요 했나 확인 user_pk=id,popup_pk=id'])
    def get(self, request):
        user_pk = request.GET.get("user_pk")
        popup_pk = request.GET.get("popup_pk")
        user = User.objects.get(id=user_pk)
        popup = Popup.objects.get(id=popup_pk)
        if user in popup.popup_like_people.all():
            return Response({"message": "좋아요눌린상태.","like_state":1}, status=200)
        else: 
            return Response({"message": "좋아요안눌린상태.","like_state":0}, status=200)
            

    
class PopupInfoView(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='팝업 id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['팝업정보_쿼리로 사용 id=팝업id'], manual_parameters=[id_param])
    
    # id= openapi.Parameter('id', openapi.IN_QUERY, description='id', required=True, type=openapi.TYPE_INTEGER)
    # @swagger_auto_schema(tags=['팝업정보_쿼리로 사용 id=팝업id'])
    def get(self, request):
        popup_id1 = request.GET.get('id')
        popup=Popup.objects.get(id=popup_id1)
        #brand_pk=popup.brand_info
        brand=Brand.objects.get(id=popup.brand_info_id)

        brand_serializer = BrandSerializer(brand)
        popup_serializer = PopupSerializer(popup)

        combined_data = {
            "brand": brand_serializer.data,
            "popup": popup_serializer.data,
        }
        return Response(combined_data, status=200)
    
class BrandInfoView(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='브랜드 id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['브랜드정보_쿼리로 사용 id=팝업id'], manual_parameters=[id_param])
    
    # id= openapi.Parameter('id', openapi.IN_QUERY, description='id', required=True, type=openapi.TYPE_INTEGER)
    # @swagger_auto_schema(tags=['팝업정보_쿼리로 사용 id=팝업id'])
    def get(self, request):
        brand_id1 = request.GET.get('id')
        brand=Brand.objects.get(id=brand_id1)
        brand_serializer = BrandSerializer(brand)
        return Response(brand_serializer.data, status=200)
    

class Brand_Open_PopupView(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='브랜드 id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['브랜드가 연 팝업 /qmfo브랜드정보_쿼리로 사용 id=팝업id'], manual_parameters=[id_param])
    
    # id= openapi.Parameter('id', openapi.IN_QUERY, description='id', required=True, type=openapi.TYPE_INTEGER)
    # @swagger_auto_schema(tags=['팝업정보_쿼리로 사용 id=팝업id'])
    def get(self, request):
        brand_id1 = request.GET.get('id')        
        popups=Popup.objects.filter(brand_info=brand_id1).order_by('-popup_opendate')     
        popup_serializer = PopupSerializer(popups, many=True)

        return Response(popup_serializer.data, status=200)
            #popups=Popup.objects.filter(popup_state=2).order_by('-popup_like')
            


class PopupReservationView(APIView):
    
    
    @swagger_auto_schema(tags=['팝업예약'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="user_id"),
            'popup_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='popup_id'),
            'popup_reservation_date': openapi.Schema(type=openapi.TYPE_STRING, description='popup_reservation_date'),
            'popup_reservation_time': openapi.Schema(type=openapi.TYPE_STRING, description='popup_reservation_time'),
        },
        
        required=['user_id', 'popup_id','popup_reservation_date','popup_reservation_time']
    ), responses={200: 'Success'})
    
    def post(self, request):
        
        # 요청에서 데이터 추출
        user_id = request.data.get('user_id', None)
        popup_id = request.data.get('popup_id', None)
        
        popup_reservation_date = request.data.get('popup_reservation_date', None)
        popup_reservation_time = request.data.get('popup_reservation_time', None)
        
        # 데이터 검증: 필요에 따라 추가 검증을 할 수 있습니다
        if not all([user_id, popup_id, popup_reservation_date, popup_reservation_time]):
            return Response({"detail": "필수 필드가 누락되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"detail": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            popup = Popup.objects.get(pk=popup_id)
        except Popup.DoesNotExist:
            return Response({"detail": "팝업을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 새 PopupPlaceReservation 인스턴스 생성
        popupreservation = PopupReservation(
            user=user,
            popup=popup,
            popup_reservation_date=popup_reservation_date,
            popup_reservation_time=popup_reservation_time
        )
        popupreservation.save()

        # 생성된 예약 인스턴스 반환
        return Response({"detail": "예약이 성공적으로 되었습니다!", "popupreservation_id": popupreservation.id}, status=status.HTTP_201_CREATED)


class MyPopupReservationsView(APIView):

    @swagger_auto_schema(
        tags=['팝업예약 조회 쿼리로 id=user_pk '],
        manual_parameters=[
            openapi.Parameter('id', in_=openapi.IN_QUERY, description='User ID', type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: PopupReservationSerializer(many=True)}
    )
    def get(self, request):
        # 사용자 ID 추출
        user_id = request.GET.get('id')
        
        user = User.objects.get(id=user_id)

        # 해당 사용자의 모든 팝업 예약 가져오기
        reservations = PopupReservation.objects.filter(user=user)

        # 결과를 serialize하여 반환
        serializer = PopupReservationSerializer(reservations, many=True)



        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePopupReservationView(APIView):
    
    # 유저의 팝업 예약을 삭제하는 뷰
    
    @swagger_auto_schema(
        tags=['팝업예약 삭제'],
        manual_parameters=[
            openapi.Parameter('user_id', in_=openapi.IN_QUERY, description='User ID', type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('popupreservation_id', in_=openapi.IN_QUERY, description='Popup Reservation ID', type=openapi.TYPE_INTEGER, required=True),
        ],
        responses={
            200: "Successfully deleted",
            404: "Not Found"
        }
    )
    def delete(self, request):
        user_id = request.GET.get('user_id')
        popupreservation_id = request.GET.get('popupreservation_id')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            popupreservation = PopupReservation.objects.get(id=popupreservation_id, user=user)
        except PopupReservation.DoesNotExist:
            return Response({"detail": "예약을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        popupreservation.delete()

        return Response({"detail": "예약이 삭제되었습니다!"}, status=status.HTTP_200_OK)










class GetAllBrandIDsAndTitlesView(APIView): #모든 브랜드 및 아티스트의 id : 이름 값 가져오기
    @swagger_auto_schema(tags=['모든 브랜드 및 아티스트의 id : 이름'])
    def get(self, request):
        data = [{"id": instance.id, "title": instance.brand_name} for instance in Brand.objects.all()]
        return Response({"data": data}, status=200)            
            
            
class GetAllPopupIDsAndTitlesView(APIView): #모든 팝업의 id : 이름 값 가져오기
    @swagger_auto_schema(tags=['모든 팝업의 id : 이름'])
    def get(self, request):
        data = [{"id": instance.id, "title": instance.popup_name} for instance in Popup.objects.all()]
        return Response({"data": data}, status=200)


