# Generated by Django 3.1 on 2020-08-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0005_remove_post_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
