from django.shortcuts import render

from . import models      #?
from .models import User  #우리가 커스텀한 유저 모델

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def deco(requset):
    return HttpResponse("success")


class LoginView(APIView): # 로그인 관련 뷰
    def post(self, request):
        userID = request.data.get("userID")
        password = request.data.get("password")
        
        user = authenticate(request, username=userID,password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "로그인 성공"}, status=200)
        else:
            return Response({"message": "아이디 또는 비밀번호가 틀렸습니다."}, status=400)
        
        
        
class SignupView(APIView):
    def post(self, request):
        
        
        
        user = User.objects.create_user(
            userID = request.data.get("userID"),
            password = request.data.get("password"),
            user_type = request.data.get("user_type"),
            user_name = request.data.get("user_name"),
            user_phonenum = request.data.get("user_phonenum"),
            user_address = request.data.get("user_address"),
            user_gender = request.data.get("user_gender"),
        
            # userID=userID,
            # password=password,
            # user_type=user_type,
            # user_name=user_name,
            # user_phonenum=user_phonenum,
            # user_adress=user_adress,
            # user_gender=user_gender,
        )
        
        if user:
            return Response({"message": "회원가입 완료"},status=201)
        else:
            return Response({"message": "회원가입 실패"},status=400)
    


class LogoutView(APIView):
    def get(self, request):
        if request.user is not None: 
            auth.logout(request)
            return Response({"message": "로그아웃 성공"},status=200)
        else:
            return Response({"message": "로그아웃 실패"},status=403)
        
        
        
        
class MyInfo(APIView):
    def get(self, request):
        user = request.user

        if user is not None:
            # return Response({"message": user.id})
            return Response({"message": user.user_name})
        else:
            return Response({"message": "로그아웃 상태입니다."})