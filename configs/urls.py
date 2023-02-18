"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings

from app.views import create_user, delete_user, update_user, retrieve_user, create_competition, update_competition, delete_competition, retrieve_competition, create_entry, update_entry, delete_entry, retrieve_entry


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('createuser/', create_user),                       #Define the url for various operations in user
    path('updateuser/<int:id>', update_user),
    path('deleteuser/<int:abc>', delete_user),
    path('retrieveuser/<int:id>', retrieve_user),
    path('retrieveuser/', retrieve_user),

    path('createcompetition/', create_competition),         #Define the url for various operations in competition
    path('updatecompetition/<int:id>', update_competition),
    path('deletecompetition/<int:abc>', delete_competition),
    path('retrievecompetition/<int:id>', retrieve_competition),
    path('retrievecompetition/', retrieve_competition),

    path('createentry/', create_entry),                     ##Define the url for various operations in entry
    path('updateentry/<int:id>', update_entry),
    path('deleteentry/<int:abc>', delete_entry),
    path('retrieveentry/<int:id>', retrieve_entry),
    path('retrieveentry/', retrieve_entry)
]