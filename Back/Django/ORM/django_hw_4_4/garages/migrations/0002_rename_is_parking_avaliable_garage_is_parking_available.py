# Generated by Django 4.2.11 on 2024-09-23 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garage',
            old_name='is_parking_avaliable',
            new_name='is_parking_available',
        ),
    ]