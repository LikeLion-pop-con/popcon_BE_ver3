# Generated by Django 4.2.3 on 2023-08-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0015_popup_popup_closetime_popup_popup_opentime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='popup_closetime',
            field=models.TimeField(verbose_name='마감시간'),
        ),
        migrations.AlterField(
            model_name='popup',
            name='popup_opentime',
            field=models.TimeField(verbose_name='오픈시간'),
        ),
    ]