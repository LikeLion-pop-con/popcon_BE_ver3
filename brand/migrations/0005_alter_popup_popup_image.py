# Generated by Django 4.2.3 on 2023-08-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_popup_popup_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='popup_image',
            field=models.ImageField(default='media/sungsimdang.png', null=True, upload_to='', verbose_name='팝업이미지'),
        ),
    ]
