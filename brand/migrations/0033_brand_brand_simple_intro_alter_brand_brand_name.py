# Generated by Django 4.2.3 on 2023-08-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0032_alter_brand_brand_intro_alter_brand_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_simple_intro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='한 줄 소개'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=50, verbose_name='기업이름'),
        ),
    ]