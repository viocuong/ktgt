# Generated by Django 3.1.2 on 2021-05-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210527_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='num_listen',
            field=models.IntegerField(default=0),
        ),
    ]