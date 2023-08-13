from django.db import models
from user.models import *

class Card(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    account_password=models.CharField(verbose_name='결제비밀번호',max_length=50, null=True,blank=True)
    bank= models.CharField(verbose_name='은행',max_length=50,null=True,blank=True)
    bank_account_number= models.CharField(verbose_name='계좌번호',max_length=50, null=True,blank=True)
    card_number=models.CharField(verbose_name='카드번호',max_length=50, null=True,blank=True)
    max_date=models.DateField (verbose_name='카드유효기간', auto_now = False , auto_now_add = False , null=True,blank=True)
    cvc=models.CharField(verbose_name='cvc',max_length=50, null=True,blank=True)
    card_password=models.CharField(verbose_name='카드비밀번호',max_length=50, null=True,blank=True)
