# Generated by Django 3.1 on 2020-08-20 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0004_auto_20200820_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
    ]
