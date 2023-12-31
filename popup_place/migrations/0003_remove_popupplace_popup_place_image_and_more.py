# Generated by Django 4.2.3 on 2023-08-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup_place', '0002_popupplace_popup_place_like_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popupplace',
            name='popup_place_image',
        ),
        migrations.AddField(
            model_name='popupplace',
            name='popup_place_image01',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업공간사진01'),
        ),
        migrations.AddField(
            model_name='popupplace',
            name='popup_place_image02',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업공간사진02'),
        ),
        migrations.AddField(
            model_name='popupplace',
            name='popup_place_image03',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업공간사진03'),
        ),
        migrations.AddField(
            model_name='popupplace',
            name='popup_place_image04',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업공간사진04'),
        ),
    ]
