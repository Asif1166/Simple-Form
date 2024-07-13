from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_create_view, name='user_create_view'),
    path('verify/', views.user_success_view, name='user_success_view'),
    path('facetime/users/all_user/', views.all_user_view, name='all_user_view'),
    
    
]