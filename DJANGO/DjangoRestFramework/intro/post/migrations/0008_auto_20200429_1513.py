# Generated by Django 3.0.5 on 2020-04-29 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200429_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='modifed_by',
            new_name='modified_by',
        ),
    ]