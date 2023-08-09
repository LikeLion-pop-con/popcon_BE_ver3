from django.db import models
from user.models import User

class Artist(models.Model):
    artist_name = models.CharField(verbose_name='아티스트이름',max_length=50)
    artist_intro=models.TextField(verbose_name='아티스트소개')
    artist_borndate=models.DateField (verbose_name='생성날짜', auto_now = False , auto_now_add = False )
    artist_subcounts=models.IntegerField(verbose_name='구독수',default=0)

    artist_like_people = models.ManyToManyField(User,blank=True, related_name="artists")# 브랜드 좋아요 누른 사람 수
    
    def __str__(self):
        return self.artist_name

class Category(models.Model):
    name= models.CharField(verbose_name='카테고리',max_length=50)
    def __str__(self):
        return self.name


class Popup(models.Model):
    artist_info = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    popup_state = models.IntegerField(verbose_name='오픈1_예정2', default=0,null=True)

    popup_name=models.CharField(verbose_name='팝업이름',max_length=50)
    
    popup_opendate=models.DateField (verbose_name='오픈날짜', auto_now = False , auto_now_add = False )
    popup_closedate=models.DateField (verbose_name='마감날짜', auto_now = False , auto_now_add = False )

    popup_opentime=models.TimeField (verbose_name='오픈시간',  auto_now = False ,auto_now_add = False)
    popup_closetime=models.TimeField (verbose_name='마감시간',  auto_now = False ,auto_now_add = False)

    popup_info=models.TextField(verbose_name='팝업내용')
    popup_image=models.ImageField (verbose_name='팝업이미지', blank=True, null=True)
    popup_like= models.IntegerField(verbose_name='팝업좋아요수', default=0)

    popup_category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    popup_detailplace=models.CharField(verbose_name='실제위치',null=True,max_length=50)

    Seoul = models.IntegerField(verbose_name='서울특별시', default=0)
    Busan = models.IntegerField(verbose_name='부산광역시', default=0)
    Incheon = models.IntegerField(verbose_name='인천광역시', default=0)
    Daegu = models.IntegerField(verbose_name='대구광역시', default=0)
    Daejeon = models.IntegerField(verbose_name='대전광역시', default=0)
    Gwangju = models.IntegerField(verbose_name='광주광역시', default=0)
    Ulsan = models.IntegerField(verbose_name='울산광역시', default=0)
    Sejong = models.IntegerField(verbose_name='세종특별자치시', default=0)
    Gyeonggi_Province = models.IntegerField(verbose_name='경기도', default=0)
    Gangwon_Province = models.IntegerField(verbose_name='강원도', default=0)
    Chungcheongbuk_Province = models.IntegerField(verbose_name='충청북도', default=0)
    Chungcheongnam_Province = models.IntegerField(verbose_name='충청남도', default=0)
    Jeollabuk_Province = models.IntegerField(verbose_name='전라북도', default=0)
    Jeollanam_Province = models.IntegerField(verbose_name='전라남도', default=0)
    Gyeongsangbuk_Province = models.IntegerField(verbose_name='경상북도', default=0)
    Gyeongsangnam_Province = models.IntegerField(verbose_name='경상남도', default=0)
    Jeju_Special_Self_Governing_Province = models.IntegerField(verbose_name='제주특별자치도', default=0)

    popup_like_people = models.ManyToManyField(User,blank=True, related_name="popups") # 팝업 좋아요 수 

    def __str__(self):
        return self.popup_name