# Generated by Django 3.0.7 on 2020-08-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0004_auto_20200813_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingRents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor1_a', models.BooleanField(default=False)),
                ('floor1_b', models.BooleanField(default=False)),
                ('floor2_a', models.BooleanField(default=False)),
                ('floor2_b', models.BooleanField(default=False)),
                ('floor3_a', models.BooleanField(default=False)),
                ('floor3_b', models.BooleanField(default=False)),
                ('floor4_a', models.BooleanField(default=False)),
                ('floor4_b', models.BooleanField(default=False)),
                ('floor5_a', models.BooleanField(default=False)),
                ('floor5_b', models.BooleanField(default=False)),
                ('floor6_a', models.BooleanField(default=False)),
                ('floor6_b', models.BooleanField(default=False)),
                ('floor7_a', models.BooleanField(default=False)),
                ('floor7_b', models.BooleanField(default=False)),
                ('floor8_a', models.BooleanField(default=False)),
                ('floor8_b', models.BooleanField(default=False)),
                ('floor9_a', models.BooleanField(default=False)),
                ('floor9_b', models.BooleanField(default=False)),
                ('floor10_a', models.BooleanField(default=False)),
                ('floor10_b', models.BooleanField(default=False)),
                ('floor11_a', models.BooleanField(default=False)),
                ('floor11_b', models.BooleanField(default=False)),
                ('floor12_a', models.BooleanField(default=False)),
                ('floor12_b', models.BooleanField(default=False)),
                ('floor13_a', models.BooleanField(default=False)),
                ('floor13_b', models.BooleanField(default=False)),
                ('floor14_a', models.BooleanField(default=False)),
                ('floor14_b', models.BooleanField(default=False)),
                ('floor15_a', models.BooleanField(default=False)),
                ('floor15_b', models.BooleanField(default=False)),
            ],
        ),
    ]
