from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Popup,Brand
from user.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupSerializer,BrandSerializer

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
    

class BrandLike_View(APIView):
    @swagger_auto_schema(tags=['브랜드좋아요'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'brand_name': openapi.Schema(type=openapi.TYPE_STRING, description='brand_name'),
            'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='user_name'),
        },
        required=['brand_name', 'user_name']
    ), responses={200: 'Success'})

    def post(self, request):
        brand = Brand.objects.get(brand_name = request.data.get("brand_name"))         
        user = User.objects.get(user_name=request.data.get("user_name"))
        if user in brand.brand_like_people.all():
            brand.brand_like_people.remove(user)
            brand.save()
        else:
            brand.brand_like_people.add(user)
            brand.save()
        return Response({"message":brand.brand_like_people.count()})
    
class MyBrandLikeList(APIView):
    user_name= openapi.Parameter('user_name', openapi.IN_QUERY, description='이름', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['내가 좋아요한 브랜드목록_쿼리로 사용 user_name=이름'])
    def get(self, request):
        user_name1 = request.GET.get("user_name")
        user = User.objects.get(user_name=user_name1)
        brand_list = user.brands
        brand_serializer = BrandSerializer(brand_list, many=True)

        return Response(brand_serializer.data, status=200)


class PopupLike_View(APIView):
    @swagger_auto_schema(tags=['팝업좋아요'], request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "popup_name": openapi.Schema(type=openapi.TYPE_STRING, description="popup_name"),
            'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='user_name'),
        },
        required=["popup_name", 'user_name']
    ), responses={200: 'Success'})

    def post(self, request):
        popup = Popup.objects.get(popup_name = request.data.get("popup_name"))         
        user = User.objects.get(user_name=request.data.get("user_name"))
    
        if user in popup.popup_like_people.all():
            popup.popup_like_people.remove(user)
            popup.popup_like -=1
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
        else:
            popup.popup_like_people.add(user)
            popup.popup_like +=1
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
            elif '제주특별자치도' in user.user_address:
                popup.Jeju_Special_Self_Governing_Province += 1
            popup.save()
        return Response({"mylikestate":popup.popup_like_people.count(),"total_like":popup.popup_like})
    

class MyPopupLikeList(APIView):
    user_name= openapi.Parameter('user_name', openapi.IN_QUERY, description='이름', required=True, type=openapi.TYPE_STRING)
    @swagger_auto_schema(tags=['내가 좋아요한 팝업목록_쿼리로 사용 user_name=이름'])
    def get(self, request):
        user_name1 = request.GET.get("user_name")
        user = User.objects.get(user_name=user_name1)
        popup_list = user.popups
        popup_serializer = PopupSerializer(popup_list, many=True)
        return Response(popup_serializer.data, status=200)