# Generated by Django 4.1.7 on 2023-03-07 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='santiye',
            name='hakedis_sebebi',
        ),
        migrations.RemoveField(
            model_name='santiye',
            name='hakedis_tarihi',
        ),
        migrations.DeleteModel(
            name='Hakedis',
        ),
    ]
