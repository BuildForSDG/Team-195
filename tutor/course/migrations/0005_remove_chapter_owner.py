# Generated by Django 3.0.5 on 2020-06-02 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200528_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='owner',
        ),
    ]
