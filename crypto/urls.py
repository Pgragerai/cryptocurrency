"""crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url, include
from utils import requests_crypto

urlpatterns = [
    path('admin/', admin.site.urls),

    #Carga de datos
    url(r'^crypto/data_load',requests_crypto.data_load,
        name='data_load'),
    url(r'^crypto/statistics_bids',requests_crypto.statistics_bids,
        name='statistics_bids'),
    url(r'^crypto/statistics_asks',requests_crypto.statistics_asks,
        name='statistics_asks'),
    url(r'^crypto/statistics',requests_crypto.statistics,
        name='statistics'),
]
