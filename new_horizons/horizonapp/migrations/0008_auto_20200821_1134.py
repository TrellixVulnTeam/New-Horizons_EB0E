# Generated by Django 3.0.7 on 2020-08-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0007_auto_20200821_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslider',
            name='choice1',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='homeslider',
            name='choice2',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='homeslider',
            name='choice3',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]