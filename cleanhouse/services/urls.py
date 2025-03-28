from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('new/', views.request_create, name='request_create'),  # form view
    path('<int:pk>/edit/', views.request_update, name='request_update'),  # Edit form
    path('<int:pk>/delete/', views.request_delete, name='request_delete'), # delete view

]
