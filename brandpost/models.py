from django.db import models
from brand.models import *
# Create your models here.
class Brandpost(models.Model):
    
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, null=True,blank=True)
    brandpost_name = models.CharField(verbose_name='포스트이름',max_length=50)
    brandpost_intro=models.TextField(verbose_name='메인소개')
    brandpost_image=models.ImageField (verbose_name='포스트이미지', blank=True, null=True)
    def __str__(self):
        return self.brandpost_name
    
