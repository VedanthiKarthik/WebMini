# Generated by Django 2.2.4 on 2019-12-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0007_auto_20191209_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributes',
            name='cont_urls',
        ),
    ]
