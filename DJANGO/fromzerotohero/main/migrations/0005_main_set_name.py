# Generated by Django 2.2.6 on 2019-11-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191127_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]
