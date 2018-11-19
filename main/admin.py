from django.contrib import admin

# Register your models here.
from .models import Client,Contract,ContractType,PaysType,Facilitie,ContractTarif,Network,Service

class ClientWithMoreContracts(admin.StackedInline):
    model = Contract
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('description', 'creator')
    inlines = [ClientWithMoreContracts]

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('description','client')

@admin.register(Facilitie)
class Facilitie(admin.ModelAdmin):
    list_display = ('description','cost')
    list_filter = ('cost',)

@admin.register(ContractTarif)
class ContractTarif(admin.ModelAdmin):
    list_display = ('description', 'contract')

@admin.register(Network)
class Network(admin.ModelAdmin):
    list_display = ('description', 'tarif')

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('code','description','cost')
    list_filter = ('cost',)