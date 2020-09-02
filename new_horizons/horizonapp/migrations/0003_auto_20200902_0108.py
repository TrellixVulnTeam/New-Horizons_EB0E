# Generated by Django 3.0.7 on 2020-09-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0002_auto_20200901_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='requested_time',
            field=models.DateField(auto_now=True, verbose_name='Огноо'),
        ),
        migrations.AlterField(
            model_name='buildingintro',
            name='pic',
            field=models.ImageField(blank=True, default='settings/horizon10.jpg', upload_to='Home/building_intro/', verbose_name='Зураг'),
        ),
        migrations.AlterField(
            model_name='buildingintro',
            name='title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box1_text',
            field=models.TextField(blank=True, default='Оруулаагүй', null=True, verbose_name='Box 1 текст'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box1_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, null=True, verbose_name='Box 1 гарчиг'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box2_text',
            field=models.TextField(blank=True, default='Оруулаагүй', null=True, verbose_name='Box 2 текст'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box2_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, null=True, verbose_name='Box 2 гарчиг'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box3_text',
            field=models.TextField(blank=True, default='Оруулаагүй', null=True, verbose_name='Box 3 текст'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box3_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, null=True, verbose_name='Box 3 гарчиг'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box4_text',
            field=models.TextField(blank=True, default='Оруулаагүй', null=True, verbose_name='Box 4 текст'),
        ),
        migrations.AlterField(
            model_name='featurecard',
            name='box4_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, null=True, verbose_name='Box 4 гарчиг'),
        ),
        migrations.AlterField(
            model_name='homeslider',
            name='background_pic',
            field=models.ImageField(blank=True, default='settings/index.jpeg', upload_to='Home', verbose_name='Зураг'),
        ),
        migrations.AlterField(
            model_name='homeslider',
            name='text_lil',
            field=models.CharField(blank=True, default='Default', max_length=255, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='homeslider',
            name='title',
            field=models.CharField(blank=True, default='Default', max_length=255, verbose_name='Гарчиг'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='or_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True, unique=True, verbose_name='Байгууллагын нэр'),
        ),
        migrations.AlterField(
            model_name='pdfbrochure',
            name='pdf',
            field=models.TextField(blank=True, default='asd', verbose_name='PDF link'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box1_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 1 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box1_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 1 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box2_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 2 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box2_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 2 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box3_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 3 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box3_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 3 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box4_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 4 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box4_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 4 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box5_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 5 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box5_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 5 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box6_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 6 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box6_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 6 гарчиг'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box7_text',
            field=models.TextField(blank=True, default='Оруулаагүй', verbose_name='Box 7 текст'),
        ),
        migrations.AlterField(
            model_name='reasonboxes',
            name='box7_title',
            field=models.CharField(blank=True, default='Оруулаагүй', max_length=255, verbose_name='Box 7 гарчиг'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Facebook хаяг'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Instagram хаяг'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Барилгын байршил'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(blank=True, default='settings/nh_logo.png', upload_to='settings', verbose_name='Барилгын лого'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='mail',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Компанийн э-мэйл хаяг'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Холбоо барих утас'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Twitter хаяг'),
        ),
    ]
