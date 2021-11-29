# Generated by Django 3.2.9 on 2021-11-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_forum_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.TextField(default="description", max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='comment',
            field=models.TextField(max_length=550),
        ),
    ]
