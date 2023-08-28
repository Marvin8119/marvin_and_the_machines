from django.urls import path
from . import views

urlpatterns = [
"""
URL pattern for the login, home, albums and members pages.

This URL pattern maps to the 'login' view function, which handles user login.

Parameters:
    - 'login/': The URL path where this pattern is active.
    - 'views.login': The view function that will be called to handle the request.
    - 'name='login'': A unique name for this URL pattern, which can be used to reverse URL matching.
"""
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('albums/', views.albums, name='albums'),
    path('members/', views.members, name='members'),
]
