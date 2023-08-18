from django.shortcuts import render
from .models import *
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema
from .serializers import *


class Video_GetView(APIView):
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description='video id', required=True, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(tags=['영상얻어오기 /  id =영상id'], manual_parameters=[id_param])
    
    def get(self, request):
        video_id1 = request.GET.get('id')        
        video=GifModel.objects.filter(id=video_id1)    
        video_serializer = VideoSerializer(video, many=True)

        return Response(video_serializer.data, status=200)
    


class Video_allGetList(APIView):
    
    @swagger_auto_schema(tags=['모든영상'])
    
    def get(self, request):
           
        video=GifModel.objects.all()
        video_serializer = VideoSerializer(video, many=True)

        return Response(video_serializer.data, status=200)