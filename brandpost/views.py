from django.shortcuts import render
from brandpost.models import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
from .serializers import *



class Brand_Have_PopupView(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='브랜드 id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['브랜드의 포스트(광고느낌) post있는브랜드id=(6,26,23,14,7)  /브랜드 id쿼리로  id =브랜드id'], manual_parameters=[id_param])
    
    # id= openapi.Parameter('id', openapi.IN_QUERY, description='id', required=True, type=openapi.TYPE_INTEGER)
    # @swagger_auto_schema(tags=['팝업정보_쿼리로 사용 id=팝업id'])
    def get(self, request):
        brand_id1 = request.GET.get('id')        
        brand_post=Brandpost.objects.filter(brand=brand_id1)    
        brandpost_serializer = BrandPostSerializer(brand_post, many=True)

        return Response(brandpost_serializer.data, status=200)
            

