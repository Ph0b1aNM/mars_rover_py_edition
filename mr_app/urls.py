from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_index, name='redirect_index'),
    path('index/', views.index, name='index'),
    path('index/del_view/', views.del_view, name='del_view'),
    path('index/input/', views.input, name='input'),
    path('index/success/', views.success, name='success'),
]