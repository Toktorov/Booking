# Generated by Django 3.2.7 on 2021-09-27 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='hotels',
        ),
    ]
