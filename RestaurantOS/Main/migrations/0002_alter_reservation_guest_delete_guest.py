# Generated by Django 4.2.5 on 2023-10-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]