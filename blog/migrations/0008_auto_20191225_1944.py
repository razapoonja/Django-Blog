# Generated by Django 2.2 on 2019-12-25 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191225_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
