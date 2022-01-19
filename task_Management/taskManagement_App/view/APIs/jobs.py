from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from taskManagement_App.models.hr_models import jobs
from ...models.master_models import designation_Master, employeeType_Master
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ...models.project_model import Project_Management,Module_management,Sub_module_management
from ...models.employee_model import employeeDetails
from ...models.master_models import project_sector_Master,project_type_Master,Project_Technology_Master
from ...models.task_model import Task_Management
from django.contrib.auth.models import User
from ...models.leave_model import leave_management,holiday_management,leave_allotment_management

from rest_framework.decorators import api_view

# @api_view(['GET'])
def job_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    jobObj = jobs.objects.all().order_by('-id')
    return JsonResponse({'response':jobObj})