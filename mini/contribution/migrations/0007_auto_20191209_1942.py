# Generated by Django 2.2.4 on 2019-12-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0006_contributes_urls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributes',
            old_name='urls',
            new_name='cont_urls',
        ),
    ]
