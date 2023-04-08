"""
URL configuration for locadora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from filme.views import *


urlpatterns = [
     path('admin/', admin.site.urls),
     path("", base, name='base'),
     path('filme_list/', filme_list, name='filme_list'),
     path("filme_new/",filme_new, name='filme_new'),
     path('filme_edit/<int:pk>/', filme_edit, name='filme_edit'),
     path('filme_delete/<int:pk>/', filme_delete, name='filme_delete' ),
    ]
