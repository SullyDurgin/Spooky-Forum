# Generated by Django 3.2.9 on 2021-11-30 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='user',
        ),
    ]
