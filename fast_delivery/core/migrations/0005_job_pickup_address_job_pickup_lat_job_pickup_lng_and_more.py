# Generated by Django 4.2.13 on 2024-05-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
