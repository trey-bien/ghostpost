# Generated by Django 3.1 on 2020-08-20 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('is_boast', models.BooleanField()),
                ('up_vote', models.IntegerField()),
                ('down_vote', models.IntegerField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
