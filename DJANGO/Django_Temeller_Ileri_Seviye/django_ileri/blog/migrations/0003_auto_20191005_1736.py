# Generated by Django 2.2.6 on 2019-10-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191003_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id'], 'verbose_name': 'Gönderi', 'verbose_name_plural': 'Gönderiler'},
        ),
    ]