# Generated by Django 4.1.7 on 2023-03-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_santiye_hakedis_sebebi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santiye',
            name='resim',
            field=models.FileField(default='static/images/636407734632442_h8daafR.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='sirket',
            name='resim',
            field=models.FileField(default='static/images/sirket-gorsel-e1643089635413_Nygl2Qy.jpg', upload_to=''),
        ),
    ]
