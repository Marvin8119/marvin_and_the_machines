from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('albums/', views.albums, name='albums'),
    path('members/', views.members, name='members'),
]
