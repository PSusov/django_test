# Generated by Django 2.1.3 on 2018-11-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181113_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracttarif',
            name='start',
            field=models.DateField(verbose_name='Начало действия тарифа'),
        ),
    ]
