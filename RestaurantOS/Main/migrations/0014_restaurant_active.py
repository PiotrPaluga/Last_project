# Generated by Django 4.2.6 on 2023-10-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_reservation_end_hour_reservation_start_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
