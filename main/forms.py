from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class EditClientForm(forms.Form):
    description = forms.CharField(label="Описание",help_text="Наименование клиента")
    contacts = forms.CharField(label="Контакты")
    comment = forms.CharField(label="Комментарий")

#from django.forms import ModelForm
#from .models import Service
#class ServiceModelForm(ModelForm):
#    class Meta:
#        model = Service
#        fields = '__all__'