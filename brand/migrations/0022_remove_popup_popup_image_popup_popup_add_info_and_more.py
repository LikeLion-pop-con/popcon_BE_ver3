# Generated by Django 4.2.3 on 2023-08-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0021_popup_popup_simple_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popup',
            name='popup_image',
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_add_info',
            field=models.CharField(default='', max_length=200, verbose_name='더많은정보'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_brand_logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='브랜드로고'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_date',
            field=models.CharField(default='', max_length=150, verbose_name='운영기간'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image01',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지01'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image02',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지02'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image03',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지03'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image04',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지04'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image05',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지05'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image06',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지06'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_image07',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='팝업이미지07'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_main_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='메인포스터'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_operation',
            field=models.CharField(default='', max_length=150, verbose_name='기획/운영'),
        ),
        migrations.AddField(
            model_name='popup',
            name='popup_time',
            field=models.CharField(default='', max_length=150, verbose_name='운영시간'),
        ),
        migrations.AlterField(
            model_name='popup',
            name='popup_detailplace',
            field=models.CharField(max_length=50, null=True, verbose_name='팝업장소'),
        ),
    ]
