# Generated by Django 4.2.13 on 2024-05-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_courier_paypal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('in', 'In'), ('out', 'Out')], default='in', max_length=20),
        ),
    ]
