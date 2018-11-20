"""stat_tst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^main/', include('main.urls')),
]

urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/main/', permanent=True)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#if settings.DEBUG:
#    urlpatterns += staticfiles_urlpatterns()