# Generated by Django 2.2.7 on 2019-11-22 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, max_length=100),
        ),
    ]
