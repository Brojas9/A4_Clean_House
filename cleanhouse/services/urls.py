from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
     path('new/', views.request_create, name='request_create'),  # form view
]
