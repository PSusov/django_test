from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^facilities/$', views.FacilitiesListView.as_view(), name='facilities'),
    url(r'^facilities/(?P<pk>\d+)$',views.FacilitieDetailView.as_view(), name='facilitie-detail'),
    url(r'^clients/(?P<pk>\d+)$',views.ClientDetailView.as_view(), name='client-detail'),
    url(r'^clients/(?P<pk>\d+)/editcli/$',views.editcli, name='editcli'),
    url(r'^contracts/(?P<pk>\d+)$',views.ContractDetailView.as_view(), name='contract-detail'),
    url(r'^contracttarifs/(?P<pk>\d+)$',views.ContracttarifDetailView.as_view(), name='contracttarif-detail'),
    url(r'^services/$', views.ServicesListView.as_view(), name='services'),
    url(r'^services/(?P<pk>\d+)$',views.ServiceDetailView.as_view(), name='service-detail'),
    url(r'^networks/(?P<pk>\d+)$',views.NetworkDetailView.as_view(), name='network-detail'),
    url(r'^my_clients/$', views.MyClientsListView.as_view(), name='my_clients'),
]
# ModelForm create,update,delete
urlpatterns += [  
    url(r'^services/create/$', views.ServiceCreate.as_view(), name='service_create'),
    url(r'^services/(?P<pk>\d+)/update/$', views.ServiceUpdate.as_view(), name='service_update'),
    url(r'^services/(?P<pk>\d+)/delete/$', views.ServiceDelete.as_view(), name='service_delete'),
]
urlpatterns += [  
    url(r'^facilities/create/$', views.FacilitieCreate.as_view(), name='facilitie_create'),
    url(r'^facilities/(?P<pk>\d+)/update/$', views.FacilitieUpdate.as_view(), name='facilitie_update'),
    url(r'^facilities/(?P<pk>\d+)/delete/$', views.FacilitieDelete.as_view(), name='facilitie_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)