# Generated by Django 3.1.2 on 2021-05-21 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='content',
            new_name='message',
        ),
    ]
