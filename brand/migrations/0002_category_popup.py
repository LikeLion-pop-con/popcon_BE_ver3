# Generated by Django 4.2.3 on 2023-07-31 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='카테고리')),
            ],
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popup_name', models.CharField(max_length=50, verbose_name='팝업이름')),
                ('popup_opendate', models.DateField(verbose_name='오픈날짜')),
                ('popup_closedate', models.DateField(verbose_name='마감날짜')),
                ('popup_info', models.TextField(verbose_name='팝업내용')),
                ('popup_image', models.ImageField(upload_to='', verbose_name='팝업이미지')),
                ('popup_like', models.IntegerField(default=0, verbose_name='팝업좋아요수')),
                ('Seoul', models.IntegerField(default=0, verbose_name='서울특별시')),
                ('Busan', models.IntegerField(default=0, verbose_name='부산광역시')),
                ('Incheon', models.IntegerField(default=0, verbose_name='인천광역시')),
                ('Daegu', models.IntegerField(default=0, verbose_name='대구광역시')),
                ('Daejeon', models.IntegerField(default=0, verbose_name='대전광역시')),
                ('Gwangju', models.IntegerField(default=0, verbose_name='광주광역시')),
                ('Ulsan', models.IntegerField(default=0, verbose_name='울산광역시')),
                ('Sejong', models.IntegerField(default=0, verbose_name='세종특별자치시')),
                ('Gyeonggi_Province', models.IntegerField(default=0, verbose_name='경기도')),
                ('Gangwon_Province', models.IntegerField(default=0, verbose_name='강원도')),
                ('Chungcheongbuk_Province', models.IntegerField(default=0, verbose_name='충청북도')),
                ('Chungcheongnam_Province', models.IntegerField(default=0, verbose_name='충청남도')),
                ('Jeollabuk_Province', models.IntegerField(default=0, verbose_name='전라북도')),
                ('Jeollanam_Province', models.IntegerField(default=0, verbose_name='전라남도')),
                ('Gyeongsangbuk_Province', models.IntegerField(default=0, verbose_name='경상북도')),
                ('Gyeongsangnam_Province', models.IntegerField(default=0, verbose_name='경상남도')),
                ('Jeju_Special_Self_Governing_Province', models.IntegerField(default=0, verbose_name='제주특별자치도')),
                ('brand_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('popup_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.category')),
            ],
        ),
    ]
