from django.db import models


class GifModel(models.Model):
    gif = models.ImageField(upload_to='gifs/')  # 이미지를 저장할 필드

    def __str__(self):
        return self.gif.name