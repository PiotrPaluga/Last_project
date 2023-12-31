# Generated by Django 4.2.5 on 2023-10-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_reservation_guest_delete_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='participants',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='tables',
            name='max_cap',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tables',
            name='min_cap',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hours',
            name='close_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='hours',
            name='open_hour',
            field=models.TimeField(null=True),
        ),
    ]
