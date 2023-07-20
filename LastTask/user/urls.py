from django.contrib import admin
from django.urls import path
from . import views
from user import views as user_view
urlpatterns = [
    path('login', views.login_view),
    path('register', views.register_view),
    path('logout', views.logout_view),
    path('info', user_view.user_list)
]
