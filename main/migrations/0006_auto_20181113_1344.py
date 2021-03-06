# Generated by Django 2.1.3 on 2018-11-13 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181113_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractTarif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30, verbose_name='Описание тарифа')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('sale', models.IntegerField(verbose_name='Скидка, %')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Contract', verbose_name='Договор')),
            ],
        ),
        migrations.CreateModel(
            name='Facilitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('bwi', models.IntegerField(help_text='0 - для безлимитов', verbose_name='Скорость')),
                ('mbyte', models.IntegerField(help_text='0 - для безлимитов', verbose_name='Мбайт')),
                ('transport', models.DecimalField(decimal_places=4, help_text='Помегабайтная стоимость', max_digits=10, verbose_name='Транспорт')),
                ('vector', models.CharField(help_text='(in,out,max) - расчет по входящему, исходящему, превалирующему трафику, bw для условных безлимитов', max_length=10, verbose_name='Направление')),
                ('mul', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Множитель')),
                ('description', models.CharField(max_length=30, verbose_name='Описание')),
                ('comment', models.TextField(verbose_name='Комментарии')),
            ],
        ),
        migrations.AddField(
            model_name='contracttarif',
            name='fid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Facilitie', verbose_name='Тариф'),
        ),
    ]
