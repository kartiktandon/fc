"""calc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('si/', views.si, name='si'),
    path('ci/', views.ci, name='ci'),
    path('emi/', views.emi, name='emi'),
    path('sip/', views.sip, name='sip'),
    path('fd/', views.fd, name='fd'),
    path('rd/', views.rd, name='rd'),
    path('pf/', views.pf, name='pf'),
    path('lumpsum/', views.lumpsum, name='lumpsum')
    

    
    
  
]

