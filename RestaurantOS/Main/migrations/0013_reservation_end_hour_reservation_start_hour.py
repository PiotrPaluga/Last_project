# Generated by Django 4.2.6 on 2023-10-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_remove_reservation_end_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='end_hour',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_hour',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
