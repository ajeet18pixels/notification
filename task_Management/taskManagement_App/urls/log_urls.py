from django.urls import path
from taskManagement_App.view.log_view import *


urlpatterns = [
    path('online-users', online_employess,name='online_employess'),
    path('logs', logs,name='logs'),

]