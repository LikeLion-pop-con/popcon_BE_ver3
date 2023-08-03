from django.db import models


class PopupPlace(models.Model):
    popup_place_image=models.ImageField (verbose_name='팝업공간사진', blank=True, null=True)
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