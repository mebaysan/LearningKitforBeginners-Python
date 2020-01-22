# Generated by Django 2.2.6 on 2020-01-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='siparis',
        ),
        migrations.AddField(
            model_name='customuser',
            name='manager',
            field=models.ManyToManyField(related_name='manager', to='users.Manager'),
        ),
    ]