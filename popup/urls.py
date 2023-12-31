"""
URL configuration for popup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from user import views
from brand.views import *
from user.views import *
from card.views import *
from video.views import *

from popup_place.views import *
from brandpost.views import *


#Swagger 
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve

#image
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title = "POPCON",
        default_version = "v1",
        description = "Swagger를 사용한 API 문서입니다",
    ),
    public=True,
    permission_classes=(AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),    
    path('signup/',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('myinfo/',MyInfo.as_view()),
    path('logout/',LogoutView.as_view()),


    path('main/<int:input>',CategoryPopup_listView.as_view(),name='input'),#팝업카테고리로+진행중인팝업
    path('main/<int:input>/ing',CategoryPopuping_listView.as_view(),name='input'),#팝업카테고리로+신청중인팝업
    path('main/<int:input>/end',CategoryPopupEnd_listView.as_view(),name='input'),#팝업카테고리로+종료된인팝업
    
    
    path('main/newbrand',NewBrand_listView.as_view()), #새로운 브랜드 
    path('main/hotpopup',HotPopup_listView.as_view()), #인기팝업리스트
    path('main/hotbrand',HotBrand_listView.as_view()), #인기브랜드리스트

    path('main/brand/<int:input>',CategoryBrand_listView.as_view(),name='input'), #브랜드+아티스트 카테고리 

    path('brandlike/',BrandLike_View.as_view()), #브랜드 좋아요 누르기
    path('mylikebrand/',MyBrandLikeList.as_view()),#내가 좋아요 누른 브랜드
    path('mylikebrand/check/',CheckBradnLike.as_view()),# 브랜드 좋아요 눌렀는지 확인

    path('brand/subscribe/',BrandSubscribe_View.as_view()), #브랜드 구독 누르기
    path('brand/subscribe/my/',MyBrandSubscribeList.as_view()),#내가 구독 누른 브랜드
    path('brand/subscribe/check/',CheckBradnSubscribe.as_view()),# 브랜드 구독 눌렀는지 확인
    path('brand/subcounts',BrandsubcountsView.as_view()),# 브랜드구독수


    path('popuplike/',PopupLike_View.as_view()), #팝업 좋아요 누르기
    path('popuprequest/',PopupRequset_View.as_view()), #팝업 요청
    
    path('mylikepopup/',MyPopupLikeList.as_view()), #내가 좋아요 누른 팝업
    path('mylikepopup/request/',MyPopupReservationList.as_view()), #내가 요청한 팝업
    path('mylikepopup/check/',CheckPopupLike.as_view()), # 팝업 좋아요 눌렀는지 확인
    path("mypopupreservation/",MyPopupReservationsView.as_view()),#내가예약한팝업
    


    path('popupinfo/',PopupInfoView.as_view()), #팝업정보
    path('brandinfo/',BrandInfoView.as_view()), #브랜드정보
    path('brandinfo/popup/',Brand_Open_PopupView.as_view()), #브랜드가 연 팝업
    path('brandinfo/post/',Brand_Have_PostView.as_view()), #브랜드의 post
    path('brandinfo/post/all/',Brand_PostallList.as_view()), #브랜드의 모든 post
    
    
    path('card/signup/',CardSignup.as_view()), #카드등록
    path('card/info/',CardinfoView.as_view()), #카드정보 card/info/?id=user_id
    path('card/check/',AccountPassword_Check.as_view()), #결제비번확인

    
    
    path('brandlist/all',AllBrand_listView.as_view()),


    path('popuplist/all',AllPopup_listView.as_view()),
    


    path('popuplist/opened',OpenedPopup_listView.as_view()),
    path('popuplist/willopen',willOpenPopup_listView.as_view()),
    
    path('search/<str:search_name>',SearchView.as_view(),name='search_name'),
    
    
    path('popupplace/all',PopupPlaceAllView.as_view()),# 전체 팝업공간 정보 전달
    path('popupplace/<int:id>',PopupPlaceView.as_view(),name='id'),# pkey 값 추가로 입력하면 그 pkey에 맞는 팝업공간 전달
    path('popupplace/check/',CheckPopup_PlaceLike.as_view()), #공간 좋아요 눌렀나 안눌렀나 확인
     
     

    path('popupplacelike',PopupPlaceLike_View.as_view()),
    path('popupplacelike/check/',PopupPlaceLikeCheck_View.as_view()),
    path('popupplace/likecounts/',PopupPlaceLikeCountView.as_view()),
    path("mylikepopupplace/",MyPopupPlaceLike_ListView.as_view()),
    path('popupplacereservation/', PopupPlaceReservationView.as_view(), name='popup-place-reservation'),
    path("mypopupplacereservations/",MyPopupPlaceReservations.as_view()),
    path("popupplaceid/",GetAllPopupPlaceIDsAndTitlesView.as_view()),
    
    path("popupid/",GetAllPopupIDsAndTitlesView.as_view()),
    
    path("userid/",GetAllUserIDsAndTitlesView.as_view()),
    
    path("brandid/",GetAllBrandIDsAndTitlesView.as_view()),
    
    path("popupreservation/",PopupReservationView.as_view()),
    path("deletepopupreservation/",DeletePopupReservationView.as_view()),
    
    path("gif/",Video_GetView.as_view()),#gif가져오기
    path("gif/all/",Video_allGetList.as_view()),#gif가져오기

  

    
    # Swagger url
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^image/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # image


