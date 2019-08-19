# Generated by Django 2.2 on 2019-08-19 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=' answer date time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=' question date time'),
            preserve_default=False,
        ),
    ]
