# Generated by Django 2.2.4 on 2019-12-09 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_auto_20191209_2004'),
        ('contribution', '0008_remove_contributes_cont_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributes',
            name='cont_urls',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='calc.Courses'),
        ),
    ]
