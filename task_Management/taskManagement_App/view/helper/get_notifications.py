import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ...models.master_models import designation_Master
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ...models.project_model import Project_Management,Module_management,Sub_module_management
from ...models.employee_model import employeeDetails
from ...models.master_models import *
from ...models.notification_model import *

def get_notifications(userType=None,request=None):
    if(userType=='Admin'):
        return Notification_Management.objects.all().order_by('-id')
    if(userType=='Manager'):
        managerObj = User.objects.get(email = request)
        return Notification_Management.objects.filter(notification_created_for=managerObj,notification_delete_status=False).order_by('-id')
    if(userType=='Employee'):
        pass