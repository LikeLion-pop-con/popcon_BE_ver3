from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Popup,Brand

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupSerializer,BrandSerializer

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
        popups = Popup.objects.filter(popup_name=search_name)
        if popups.exists():
            # popup_name이 존재하는 경우, 해당 Popup을 리턴합니다.
            popup_serializer = PopupSerializer(popups, many=True)
            return Response(popup_serializer.data, status=200)
        else:
            # popup_name이 존재하지 않는 경우 Brand를 검색합니다.
            brands = Brand.objects.filter(brand_name=search_name)
            if brands.exists():
                # Brand가 존재하는 경우, 해당 Brand를 리턴합니다.
                brand_serializer = BrandSerializer(brands, many=True)
                return Response(brand_serializer.data, status=200)
            else:
                # Brand도 존재하지 않는 경우 에러 메시지를 리턴합니다.
                error_message = {"message": "검색 결과가 없습니다."}
                return Response(error_message, status=404)

def get_popup(request, popup_id):
    if request.method == 'GET':
        popup = get_object_or_404(Popup, id=popup_id)
        popup_data = {
            "popup_name": popup.popup_name,
            "popup_opendate": popup.popup_opendate,
            "popup_closedate": popup.popup_closedate,
            "popup_info": popup.popup_info,
            "popup_image": popup.popup_image.url if popup.popup_image else None,
            "popup_like": popup.popup_like,
            "popup_category": popup.popup_category,
            "Seoul": popup.Seoul,
            "Busan": popup.Busan,
            "Incheon": popup.Incheon,
            "Daegu": popup.Daegu,
            "Daejeon": popup.Daejeon,
            "Gwangju": popup.Gwangju,
            "Ulsan": popup.Ulsan,
            "Sejong": popup.Sejong,
            "Gyeonggi_Province": popup.Gyeonggi_Province,
            "Gangwon_Province": popup.Gangwon_Province,
            "Chungcheongbuk_Province": popup.Chungcheongbuk_Province,
            "Chungcheongnam_Province": popup.Chungcheongnam_Province,
            "Jeollabuk_Province": popup.Jeollabuk_Province,
            "Jeollanam_Province": popup.Jeollanam_Province,
            "Gyeongsangbuk_Province": popup.Gyeongsangbuk_Province,
            "Gyeongsangnam_Province": popup.Gyeongsangnam_Province,
            "Jeju_Special_Self_Governing_Province": popup.Jeju_Special_Self_Governing_Province
        }
        return JsonResponse(popup_data)
    else:
        return JsonResponse({"error": "GET request required."}, status=400)
    

