# Generated by Django 4.2.3 on 2023-08-08 08:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brand', '0013_alter_brand_brand_like_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_like_people',
            field=models.ManyToManyField(blank=True, related_name='brands', to=settings.AUTH_USER_MODEL),
        ),
    ]
