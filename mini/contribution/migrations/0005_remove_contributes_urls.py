# Generated by Django 2.2.4 on 2019-12-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0004_contributes_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributes',
            name='urls',
        ),
    ]
