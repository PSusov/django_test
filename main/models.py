from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # Импорт модели пользователя
# Create your models here.
class Client(models.Model):
    description = models.CharField(max_length=100,help_text="Название организации")
    contacts = models.TextField(blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        permissions = (("can_disable_cli","Set disable clients"),("can_full_view","Show owners"))
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

class Contract(models.Model):
    client = models.ForeignKey('Client',on_delete=models.SET_NULL,null=True,verbose_name="Клиент")
    email = models.EmailField(verbose_name="E-mail")
    contracttype = models.ForeignKey('ContractType',on_delete=models.SET_NULL,null=True,verbose_name="Тип договора")
    paystype = models.ForeignKey('PaysType',on_delete=models.SET_NULL,null=True)
    max_expense = models.DecimalField(max_digits=10,decimal_places=4, verbose_name="Возможное превышение расходов")
    description = models.TextField(verbose_name="Описание")
    sum_at_date = models.DecimalField(max_digits=10,decimal_places=4, verbose_name="Остаток на")
    date = models.DateField(null=True,blank=True, verbose_name="дату")
    adv_fac = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Дополнительные услуги на сумму")
    pays = models.DecimalField(max_digits=10,decimal_places=4,verbose_name="Платежи за месяц")
    epay = models.CharField(max_length=10, verbose_name="E-Pay аккаунт")
    comment = models.TextField(verbose_name="Комментарий",blank=True,null=True)
    def __str__(self):
        return str(self.client)
    def get_absolute_url(self):
        return reverse('contract-detail', args=[str(self.id)])

class ContractType(models.Model):
    contracttype = models.CharField(max_length=20,help_text="Тип договора")
    def __str__(self):
        return self.contracttype
class PaysType(models.Model):
    paystype = models.CharField(max_length=20,help_text="Тип платежей")
    def __str__(self):
        return self.paystype
VECTOR_CHOICES = (
('in',u'входящий'),
('out',u'исходящий'),
('max',u'превалирующий'),
('min',u'наименьший'),
('bw',u'условный безлимит'),
)
class Facilitie(models.Model):
    cost = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Стоимость")
    bwi = models.IntegerField(verbose_name="Скорость",help_text="0 - для безлимитов")
    mbyte = models.IntegerField(verbose_name="Мбайт",help_text="0 - для безлимитов")
    transport = models.DecimalField(max_digits=10,decimal_places=4,verbose_name="Транспорт",help_text="Помегабайтная стоимость")
    vector = models.CharField(u'Направление',max_length=10,choices=VECTOR_CHOICES,help_text="(in,out,max) - расчет по входящему, исходящему, превалирующему трафику, bw для условных безлимитов")
    mul = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Множитель")
    description = models.CharField(max_length=30,verbose_name="Описание")
    comment = models.TextField(verbose_name="Комментарии",blank=True,null=True)
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('facilitie-detail', args=[str(self.id)])


class ContractTarif(models.Model):
    contract = models.ForeignKey('Contract',on_delete=models.CASCADE,null=True,verbose_name="Договор")
    description = models.CharField(max_length=30,verbose_name="Описание тарифа")
    comment = models.TextField(verbose_name="Комментарий",blank=True,null=True)
    fid = models.ForeignKey('Facilitie',on_delete=models.SET_NULL,null=True,verbose_name="Тариф")
    sale = models.IntegerField(verbose_name="Скидка, %")
    start = models.DateField(verbose_name="Начало действия тарифа")
    stop = models.DateField(default='3000-01-01',verbose_name="Конец действия тарифа")
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('contracttarif-detail', args=[str(self.id)])

class Network(models.Model):
    tarif = models.ForeignKey('ContractTarif',on_delete=models.SET_NULL,null=True,verbose_name="Тариф")
    calculate_point = models.CharField(max_length=20,default='127.0.0.1',verbose_name="Точка обсчета")
    from_net = models.CharField(max_length=20,default='0.0.0.0/0',verbose_name="Из сети")
    to_net = models.CharField(max_length=20,verbose_name="На сеть",help_text="IP-адрес/маска")
    from_int = models.CharField(max_length=20,default='0',verbose_name="С интерфейса")
    to_int = models.CharField(max_length=20,default='0',verbose_name="На интерфейс")
    description = models.CharField(max_length=20,verbose_name="Описание")
    comment = models.TextField(blank=True,null=True,verbose_name="Комментарий")
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('network-detail', args=[str(self.id)])

# Таблица услуг
TYPE_CHOICES = (
('p',u'ежемесячный платеж'),
('s',u'разовая услуга'),
)
class Service(models.Model):
    code = models.CharField(max_length=20,verbose_name="Код")
    description = models.CharField(max_length=40,verbose_name="Описание")
    typeserv = models.CharField(u'Тип',max_length=40, choices=TYPE_CHOICES)
    cost = models.DecimalField(max_digits=10,decimal_places=4,verbose_name="Цена")
    comment = models.TextField(verbose_name="Комментарий",blank=True,null=True)
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])
