from django.contrib import admin
from django.urls import path, include
from perfis import views

urlpatterns = [
    path('perfil', include ([
        path('', views.index),
        path('<int:perfil_id>/', views.exibir),
    ]))
]
