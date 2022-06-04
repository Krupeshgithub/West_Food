"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('index1',views.index1,name="index1"),
    path("change_password",views.change_password,name="change_password"),
    path("ngo_profile",views.ngo_profile,name = "ngo_profile"),
    path("logout",views.logout,name = "logout"),
    path("ngo_update_password",views.ngo_update_password,name = "ngo_update_password"),
    path("update_profile",views.update_profile,name = "update_profile"),
    path("all_ngo",views.all_ngo,name = "all_ngo"),
    path("specific_ngo_profile/<int:pk>",views.specific_ngo_profile,name = "specific_ngo_profile"),
    path("request_pickup",views.request_pickup,name = "request_pickup"),
    path("view_request",views.view_request,name = "view_request"),
    path("past_request",views.past_request,name = "past_request"),
    path("New_post",views.New_post,name = "New_post"),



    

    
]
