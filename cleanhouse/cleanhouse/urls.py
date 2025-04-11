"""
URL configuration for cleanhouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from services import views

# This list defines which URLs will lead to which views or apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'), # main page as the default
    path('requests/', include('services.urls')),
    
]

# This part allows Django to serve static files (CSS, JS, images) during development
# It only runs if DEBUG = True in settings.py
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
