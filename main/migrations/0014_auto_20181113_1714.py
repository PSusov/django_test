# Generated by Django 2.1.3 on 2018-11-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20181113_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Цена'),
        ),
    ]
