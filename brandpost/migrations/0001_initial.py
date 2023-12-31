# Generated by Django 4.2.3 on 2023-08-17 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0037_brand_brand_subscribe_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brandpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandpost_name', models.CharField(max_length=50, verbose_name='포스트이름')),
                ('brandpost_intro', models.TextField(verbose_name='메인소개')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]
