# Generated by Django 3.1.2 on 2021-06-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_music_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
