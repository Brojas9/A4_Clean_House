from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('home/', views.home, name='home'),
    path('thank-you/', views.thank_you, name='thank_you'),

    # Customer booking
    path('requests/new/', views.request_create, name='request_create'),
    path('requests/<int:pk>/edit/', views.request_update, name='request_update'),
    path('requests/<int:pk>/delete/', views.request_delete, name='request_delete'),

    # Admin
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-requests/', views.request_list_admin, name='request_list_admin'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
]
