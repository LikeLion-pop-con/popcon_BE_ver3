from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Popup

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PopupSerializer

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
    def get(self, request,search_name):
       
        Popups = Popup.objects.filter(popup_name = search_name)
        popupserializer = PopupSerializer(Popups, many=True)
        return Response(popupserializer.data, status=200)


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
    

