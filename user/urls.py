from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',  views.logout, name='logout'),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    
]