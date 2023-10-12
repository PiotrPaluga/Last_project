# Generated by Django 4.2.5 on 2023-10-12 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Main', '0006_remove_reservation_restaurant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_nr', models.CharField(max_length=64)),
                ('min_cap', models.IntegerField()),
                ('max_cap', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('participants', models.IntegerField()),
                ('start_hour', models.IntegerField()),
                ('end_hour', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.restaurant')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.tables')),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('open_hour', models.IntegerField()),
                ('close_hour', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.restaurant')),
            ],
        ),
    ]
