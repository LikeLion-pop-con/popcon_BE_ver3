from django.db import models
from user.models import User

class PopupPlace(models.Model):
    #팝업공간사진 4장 필요하다고 
    popup_place_image01=models.ImageField (verbose_name='팝업공간사진01', blank=True, null=True)
    popup_place_image02=models.ImageField (verbose_name='팝업공간사진02', blank=True, null=True)
    popup_place_image03=models.ImageField (verbose_name='팝업공간사진03', blank=True, null=True)
    popup_place_image04=models.ImageField (verbose_name='팝업공간사진04', blank=True, null=True)
    
    popup_place_title=models.CharField(verbose_name='팝업공간이름',max_length=100)
    popup_place_location=models.CharField(verbose_name='팝업공간위치',max_length=100)
    popup_place_floor=models.CharField(verbose_name='팝업공간층수',max_length=50)
    popup_place_area=models.CharField(verbose_name='팝업공간연면적',max_length=50)
    popup_count=models.IntegerField(verbose_name='팝업횟수',default=0,null=True)
    popup_place_intro=models.TextField(verbose_name='공간소개',max_length=500)
    popup_place_point=models.TextField(verbose_name='주요포인트',max_length=300)
    popup_place_recom=models.CharField(verbose_name='공간활용추천',max_length=200)
    electricity=models.IntegerField(verbose_name='전기사용',default=0)
    warehouse=models.IntegerField(verbose_name='창고사용',default=0)
    freight=models.IntegerField(verbose_name='화물 E/V',default=0)
    parking=models.IntegerField(verbose_name='주차지원',default=0)
    
    
    popup_place_basement_floor = models.IntegerField(verbose_name="지하층",blank=True,null=True) # 지하층수입력
    popup_place_ground_floor = models.IntegerField(verbose_name="지상층",blank=True,null=True) # 지상층수입력
    
    pkey = models.IntegerField(verbose_name='팝업공간pk',default=0)# pkey값을 설정해서 팝업공간 정리하고 프론트에 전달
    
    popup_place_like = models.IntegerField(verbose_name='팝업장소좋아요수', default=0,null=True) # 팝업장소 좋아요 수
    popup_place_like_people = models.ManyToManyField(User,blank=True, related_name="popupplaces") # 팝업장소 좋아요 유저
    
    def __str__(self):
        return self.popup_place_title
    
    
    
    
class PopupPlaceReservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #null=True
    popupplace = models.ForeignKey(PopupPlace,on_delete=models.CASCADE,null=True)#,null=True
    # popupplace_reserved_floor = models.IntegerField(verbose_name='팝업공간예약층')#,null=True 
    
    popupplace_reserved_basement_floor = models.IntegerField(verbose_name='팝업공간예약지상층',blank=True,null=True)
    popupplace_reserved_ground_floor = models.IntegerField(verbose_name='팝업공간예약지하층',blank=True,null=True)
    
    popupplace_reserved_date = models.CharField(verbose_name='팝업공간날짜',max_length=100) # 프론트에서 날짜형식 or 스트링 에 따라 수정필요
    
    
    def __str__(self):
        return self.popupplace#.popup_place_title
