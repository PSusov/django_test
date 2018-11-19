from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Client,Contract,Facilitie,Network,ContractTarif,Service

@login_required
def index(request):
    num_cli = Client.objects.all()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    return render(
        request,
        'index.html',
        context={'num_cli': num_cli, 'num_visits': num_visits},
    )

from .forms import EditClientForm
from django.urls import reverse

@login_required
def editcli(request,pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = EditClientForm(request.POST)
        if form.is_valid():
            client.description = form.cleaned_data['description']
            client.contacts = form.cleaned_data['contacts']
            client.comment = form.cleaned_data['comment']
            client.creator = request.user
            client.save()
            return HttpResponseRedirect(reverse('my_clients'))
    else:
        def_description = client.description
        def_contacts = client.contacts
        def_comment = client.comment
        form = EditClientForm(initial={'description': def_description, 'contacts': def_contacts, 'comment': def_comment,})
    return render(request,'main/editcli.html',{'form': form})


class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services')

class FacilitieCreate(CreateView):
    model = Facilitie
    fields = '__all__'

class FacilitieUpdate(UpdateView):
    model = Facilitie
    fields = '__all__'

class FacilitieDelete(DeleteView):
    model = Facilitie
    success_url = reverse_lazy('facilities')





















from django.views import generic

class FacilitiesListView(LoginRequiredMixin, generic.ListView):
    model = Facilitie

class MyClientsListView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'main/my_clients_listview.html'
    paginate_by = 10
    def get_queryset(self):
        return Client.objects.filter(creator=self.request.user).order_by('description')

class ServicesListView(LoginRequiredMixin, generic.ListView):
    model = Service

class ServiceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Service

class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client

class ContractDetailView(LoginRequiredMixin, generic.DetailView):
    model = Contract

class ContracttarifDetailView(LoginRequiredMixin, generic.DetailView):
    model = ContractTarif

class NetworkDetailView(LoginRequiredMixin, generic.DetailView):
    model = Network

class FacilitieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Facilitie
