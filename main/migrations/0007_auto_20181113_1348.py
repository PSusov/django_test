# Generated by Django 2.1.3 on 2018-11-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181113_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracttarif',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='facilitie',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
    ]
