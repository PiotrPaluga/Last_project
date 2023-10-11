# Generated by Django 4.2.5 on 2023-10-07 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=64)),
                ('date', models.DateField(null=True)),
                ('participants', models.IntegerField(null=True)),
                ('start_hour', models.IntegerField(null=True)),
                ('end_hour', models.IntegerField(null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.restaurant')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.tables')),
            ],
        ),
    ]
