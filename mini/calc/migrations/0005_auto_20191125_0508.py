# Generated by Django 2.2.4 on 2019-11-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20191125_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
