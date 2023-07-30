from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(verbose_name='기업이름',max_length=50)
    brand_intro=models.TextField(verbose_name='기업소개')
    brand_subcounts=models.IntegerField(verbose_name='구독수',default=0)
    def is_staff(self):
        return self.is_admin
    