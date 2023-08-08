"""
URL configuration for innovators project.

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
from django.urls import path, include, re_path
from coverpage.views import *
from blog.views import *
from impactful_innovators.views import *
from contact.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="cover"),
    path('contact', contactme, name="contact"),
    path('blog', blog, name="blog"),
    path('innovators', impactful_innovators, name="innovators"),
    path('search', search, name="search"),
    path('personality_search', search_page, name="searchpage"),
    path('chatbot', chatbot, name="chatbot"),
    path('sent', sent, name="sent"),
]
