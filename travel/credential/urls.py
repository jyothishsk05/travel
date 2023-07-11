from django.conf.urls.static import static

from project4 import settings
from . import views
from django.urls import path

urlpatterns = [

path('register', views.register,name='register'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
    ]
