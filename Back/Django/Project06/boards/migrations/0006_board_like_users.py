# Generated by Django 4.2.11 on 2024-10-20 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0005_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(related_name='like_boards', to=settings.AUTH_USER_MODEL),
        ),
    ]