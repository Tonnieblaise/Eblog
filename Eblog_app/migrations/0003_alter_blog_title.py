# Generated by Django 4.0.4 on 2022-05-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eblog_app', '0002_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='my_title', max_length=400),
        ),
    ]