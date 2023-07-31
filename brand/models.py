from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(verbose_name='기업이름',max_length=50)
    brand_intro=models.TextField(verbose_name='기업소개')
    brand_subcounts=models.IntegerField(verbose_name='구독수',default=0)
    def is_staff(self):
        return self.is_admin
    



class Popup(models.Model):
    popup_name=models.CharField(verbose_name='팝업이름',max_length=50)
    popup_opendate=models.DateField (verbose_name='오픈날짜', auto_now = False , auto_now_add = False )
    popup_closedate=models.DateField (verbose_name='마감날짜', auto_now = False , auto_now_add = False )
    popup_info=
    popup_image=
    popup_like=
    popup_category=
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

