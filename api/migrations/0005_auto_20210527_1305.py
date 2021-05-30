# Generated by Django 3.1.2 on 2021-05-27 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_music_num_listen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='num_listen',
            new_name='num_favourite',
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.music')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
        ),
    ]