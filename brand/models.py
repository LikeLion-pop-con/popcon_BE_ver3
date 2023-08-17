from django.db import models
from user.models import User


class BrandCategory(models.Model):
    name= models.CharField(verbose_name='브랜드/아티스트_카테고리',max_length=50)
    def __str__(self):
        return self.name


class Brand(models.Model):
    type=models.IntegerField(verbose_name='타입_1브랜드/2_아트스트',default=0)
    brand_category=models.ForeignKey(BrandCategory, on_delete=models.CASCADE, null=True,blank=True)
    brand_name = models.CharField(verbose_name='기업이름',max_length=50)
    
    brand_simple_intro = models.CharField(verbose_name='한 줄 소개',max_length=200, null=True,blank=True)
    brand_intro=models.TextField(verbose_name='메인소개')
    brand_about_link = models.CharField(verbose_name='추가링크',max_length=100, null=True,blank=True)

    brand_borndate=models.DateField (verbose_name='생성날짜', auto_now = False , auto_now_add = False )
    brand_subcounts=models.IntegerField(verbose_name='구독수',default=0)
    
    brand_main_image=models.ImageField (verbose_name='메인이미지', blank=True, null=True)# 브랜드 이미지 추가
    brand_logo=models.ImageField (verbose_name='브랜드로고', blank=True, null=True)# 브랜드 이미지 추가
    brand_detail_image=models.ImageField (verbose_name='브랜드상세이미지', blank=True, null=True)# 브랜드 이미지 추가

    brand_like_people = models.ManyToManyField(User,blank=True, related_name="brands")# 브랜드 좋아요 누른 사람
    brand_subscribe_people = models.ManyToManyField(User,blank=True, related_name="subscribe_brands")# 브랜드 구독 누른 사람
    

    
    def __str__(self):
        return self.brand_name
# class BrandImage(models.Model):
#     brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
#     image = models.ImageField(verbose_name='브랜드이미지', blank=True, null=True)

class Category(models.Model):
    name= models.CharField(verbose_name='카테고리',max_length=50)
    def __str__(self):
        return self.name




# 임시로 카테고리 생성 프론트에서 요청시 확정
# class PopupCategory(models.Model):
#     name= models.CharField(verbose_name='팝업카테고리',max_length=50)
#     def __str__(self):
#         return self.name    
# class BrandCategory(models.Model):
#     name= models.CharField(verbose_name='브랜드카테고리',max_length=50)
#     def __str__(self):
#         return self.name    
# class ArtistCategory(models.Model):
#     name= models.CharField(verbose_name='아티스트카테고리',max_length=50)
#     def __str__(self):
#         return self.name    

class Popup(models.Model):
    brand_info = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    popup_state = models.IntegerField(verbose_name='오픈1_예정2_종료3', default=0,null=True)

    popup_name=models.CharField(verbose_name='팝업이름',max_length=50)
    
    popup_simple_info = models.CharField(verbose_name='간단소개',max_length=150,default='',null=True,blank=True)
    popup_date = models.CharField(verbose_name='운영기간',max_length=150,default='',null=True,blank=True)
    popup_time = models.CharField(verbose_name='운영시간',max_length=150,default='',null=True,blank=True)
    popup_operation = models.CharField(verbose_name='기획/운영',max_length=150,default='',null=True,blank=True)
    popup_detailplace=models.CharField(verbose_name='팝업장소',null=True,max_length=50)
    popup_map_place=models.CharField(verbose_name='지도위치',null=True,blank=True,max_length=50)

    popup_info=models.TextField(verbose_name='팝업내용')
    popup_add_info = models.CharField(verbose_name='더많은정보',max_length=200,default='',null=True,blank=True)
    
    
    popup_opendate=models.DateField (verbose_name='오픈날짜', auto_now = False , auto_now_add = False )
    popup_closedate=models.DateField (verbose_name='마감날짜', auto_now = False , auto_now_add = False )
    
    popup_opentime=models.TimeField (verbose_name='오픈시간',  auto_now = False ,auto_now_add = False)
    popup_closetime=models.TimeField (verbose_name='마감시간',  auto_now = False ,auto_now_add = False)

    
    popup_main_image=models.ImageField (verbose_name='메인포스터', blank=True, null=True)
    popup_brand_logo=models.ImageField (verbose_name='브랜드로고', blank=True, null=True)
    
    popup_image01=models.ImageField (verbose_name='팝업이미지01', blank=True, null=True)
    popup_image02=models.ImageField (verbose_name='팝업이미지02', blank=True, null=True)
    popup_image03=models.ImageField (verbose_name='팝업이미지03', blank=True, null=True)
    popup_image04=models.ImageField (verbose_name='팝업이미지04', blank=True, null=True)
    popup_image05=models.ImageField (verbose_name='팝업이미지05', blank=True, null=True)
    popup_image06=models.ImageField (verbose_name='팝업이미지06', blank=True, null=True)
    popup_image07=models.ImageField (verbose_name='팝업이미지07', blank=True, null=True)
    
    
    popup_like= models.IntegerField(verbose_name='팝업좋아요수', default=0) # 팝업 좋아요 수

    popup_category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    
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


    popup_like_people = models.ManyToManyField(User,blank=True, related_name="popups") # 팝업 좋아요 사람
    popup_request_people = models.ManyToManyField(User,blank=True, related_name="request_popups") # 팝업 요청한 사람



    def __str__(self):
        return self.popup_name
    
    
class PopupReservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    popup = models.ForeignKey(Popup,on_delete=models.CASCADE,null=True)
    # popupplace_reserved_floor = models.IntegerField(verbose_name='팝업공간예약층')#,null=True 
    
    #popup_reservation_date = models.CharField(verbose_name='팝업예약날짜',max_length=100)
    popup_reservation_date = models.DateField(verbose_name='팝업예약날짜', auto_now = False , auto_now_add = False )
    popup_reservation_time = models.CharField(verbose_name='팝업예약시간',max_length=100)
    #popupp_reservation_date = models.CharField(verbose_name='팝업날짜',max_length=100) # 프론트에서 날짜형식 or 스트링 에 따라 수정필요
    def __str__(self):
        return str(self.popup.popup_name) if self.popup else "No PopupPlace Assigned"# if 뒤에는 popup에 내용이 부족한 정보가 있을 때 저렇게 표기해줌(없으면 오류발생)
