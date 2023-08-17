from django.shortcuts import render
from brandpost.models import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema






