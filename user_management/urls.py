from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_create_view, name='user_create_view'),
    path('success/', views.user_success_view, name='user_success_view'),
    
    
]