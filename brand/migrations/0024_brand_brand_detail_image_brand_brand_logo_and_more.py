# Generated by Django 4.2.3 on 2023-08-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0023_alter_popup_popup_add_info_alter_popup_popup_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_detail_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='브랜드상세이미지'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='브랜드로고'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_main_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='메인이미지'),
        ),
        migrations.DeleteModel(
            name='BrandImage',
        ),
    ]