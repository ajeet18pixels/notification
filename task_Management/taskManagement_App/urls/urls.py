from django.urls import path
from taskManagement_App.view.authentication_view import *


urlpatterns = [
    path('', user_login,name='user_login'),
    path('dashboard', admin_dashboard,name='admin_dashboard'),


    path('restricted-access', unautorizedaccess,name='unautorizedaccess'),


    path('change-password', change_password,name='change_password'),
    path('user-profile', profile,name='profile'),
    path('user_logout', user_logout,name='user_logout'),

    path('get-notifications', get_notifications,name='get_notifications'),
]