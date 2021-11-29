# Generated by Django 3.2.9 on 2021-11-27 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_posts_spookylevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='author', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='comment',
            field=models.TextField(default='enter text', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
    ]