# Generated by Django 3.1.2 on 2021-05-30 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_music_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='url',
        ),
    ]