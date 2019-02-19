"""easypatho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from easypathoapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.Index, name="Index"),
    url('corporate/', views.addinfo, name="Corporate"),
    url('register/',views.reginfo,name="register"),
    url('workculture/',views.workculture,name="workculture"),
    url('currentopenings/',views.currentopenings,name="currentopenings"),
    url('signin/',views.signin,name="signin"),
    url('cardiology/', views.cardiology, name="cardiology"),
    url('radiology/', views.radiology, name="radiology"),
    url('laboratory/',views.laboratory,name="laboratory"),
    url('tmt/', views.tmt, name="tmt"),
    url('echo/', views.echo, name="echo"),
    url('ecg/', views.ecg, name="ecg"),
    url('dst/', views.dst, name="dst"),
    url('osix/', views.osix, name="osix"),
    url('us/', views.us, name="us"),
    url('dxr/', views.dxr, name="dxr"),
    url('dma/', views.dma, name="dma"),
    url('dexa/', views.dexa, name="dexa"),
    url('cb/', views.cb, name="cb"),
    url('pac/', views.pac, name="pac"),
    url('ser/', views.ser, name="ser"),
    url('haem/', views.haem, name="haem"),
    url('md/', views.md, name="md"),
    url('hisp/', views.hisp, name="hisp"),
    url('hpp/', views.hpp, name="hpp"),
    url('emp/', views.employee, name="emp"),
    url('ov/', views.overview, name="overview"),
    url('vav/', views.vav, name="vav"),
    url('qpo/', views.qpo, name="qpo"),
    url('eb/', views.eb, name="eb"),
    url('sf/', views.sf, name="sf"),
    url('tt/', views.tt, name="tt"),




]
