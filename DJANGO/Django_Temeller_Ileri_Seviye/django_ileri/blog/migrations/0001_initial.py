# Generated by Django 2.2.6 on 2019-10-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Başlık Bilgisi Burada Girilir', max_length=100, null=True, verbose_name='Başlık')),
                ('content', models.TextField(max_length=1000, null=True, verbose_name='İçerik')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]