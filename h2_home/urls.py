from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login),
    path("home",views.home,name="home"),
    path("landing",views.landing,name="landing"),
    path("register",views.register,name="register"),
    path("db",views.SqlDB.as_view(),name="db")
]
