# Generated by Django 2.1.3 on 2018-11-13 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181113_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contracttype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ContractType', verbose_name='Тип договора'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='max_expense',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Возможное превышение расходов'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='pays',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Платежи за месяц'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sum_at_date',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Остаток на'),
        ),
    ]
