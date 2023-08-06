# Generated by Django 4.2.3 on 2023-08-06 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0007_popup_popup_detailplace_alter_popup_popup_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='popup_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.category'),
        ),
        migrations.AlterField(
            model_name='popup',
            name='popup_detailplace',
            field=models.CharField(max_length=50, null=True, verbose_name='실제위치'),
        ),
    ]
