
from django.contrib import admin
from django.urls import path
from . import views, login_views


urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.annonce_create.as_view() ),
    path('annonce_list/<int:id>/', views.annonce_detail.as_view() , name= 'annonce_detail'),
    
    path('search', views.annoce_search, name="annoce_search"),
    
    path("register", login_views.register_request, name="register"),
    path("login", login_views.login_request, name="login"),
    path("logout", login_views.logout_request, name= "logout"),
    
    path("t", views.t, name="t"),
    
]

