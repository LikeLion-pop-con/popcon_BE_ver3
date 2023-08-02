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

# class SearchView(APIView):
#     def get(self, request, search_name):
#         # 먼저 popup_name으로 검색해봅니다.
#         popups = Popup.objects.filter(popup_name__icontains=search_name)
#         if popups.exists():
#             # popup_name이 존재하는 경우, 해당 Popup을 리턴합니다.
#             popup_serializer = PopupSerializer(popups, many=True)
#             return Response(popup_serializer.data, status=200)
#         else:
#             # popup_name이 존재하지 않는 경우 Brand를 검색합니다.
#             brands = Brand.objects.filter(brand_name__icontains=search_name)
#             if brands.exists():
#                 # Brand가 존재하는 경우, 해당 Brand를 리턴합니다.
#                 brand_serializer = BrandSerializer(brands, many=True)
#                 return Response(brand_serializer.data, status=200)
#             else:
#                 # Brand도 존재하지 않는 경우 에러 메시지를 리턴합니다.
#                 error_message = {"message": "검색 결과가 없습니다."}
#                 return Response(error_message, status=404)



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