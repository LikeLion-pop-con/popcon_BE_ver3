# Generated by Django 4.2.3 on 2023-08-15 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brand', '0035_alter_brand_brand_simple_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='popup_request_people',
            field=models.ManyToManyField(blank=True, related_name='request_popups', to=settings.AUTH_USER_MODEL),
        ),
    ]
