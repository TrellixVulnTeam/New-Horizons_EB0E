# Generated by Django 3.0.7 on 2020-08-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0005_buildingrents'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='floor1_a',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='floor1_b',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='floor2_a',
            field=models.BooleanField(default=False),
        ),
    ]