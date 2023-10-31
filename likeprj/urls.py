"""
URL configuration for likeprj project.

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
from django.urls import path, include
import likeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', likeapp.views.index, name='index'),
    path('create/', likeapp.views.create, name='create'),
    path('read/', likeapp.views.read, name = 'read'),
    path('detail/<str:id>/', likeapp.views.detail, name = 'detail'),
    
    path('update/<str:id>/', likeapp.views.update, name='update'),
    
    path('update/<str:id>/', likeapp.views.update, name = 'update'),
    path('delete/<str:id>/', likeapp.views.delete, name = 'delete'),
    
    path('user/', include('userapp.urls')),
]