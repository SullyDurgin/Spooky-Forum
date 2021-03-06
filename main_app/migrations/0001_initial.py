# Generated by Django 3.2.9 on 2021-11-26 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=250)),
                ('spookyLevel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Post date')),
                ('topic', models.CharField(choices=[('R', 'Real Life'), ('H', 'Haunting'), ('N', 'Nightmare')], default='R', max_length=1)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.forum')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
