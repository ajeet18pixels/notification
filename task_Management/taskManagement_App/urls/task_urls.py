from django.urls import path
from taskManagement_App.view.task_view import *


urlpatterns = [
    path('task-list', task_management,name='task_management'),
    path('get_project_module_employee_list/<int:id>', get_project_module_employee_list,name='get_project_module_employee_list'),
    path('add-task', add_task,name='add_task'),
    path('update-task-status', update_task_status,name='update_task_status'),
    path('get_task_details/<int:id>',get_task_details,name='get_task_details'),


    path('update-task-info', update_task_info,name='update_task_info'),
    path('update-task-dependencies', update_task_dependencies,name='update_task_dependencies'),


    path('delete-task/<int:id>', delete_task,name='delete_task'),
    path('get_module_list/<int:id>', get_module_list,name='get_module_list'),


    path('filter-task', filter_task,name='filter_task'),

    # path('check-module-name', check_module_name,name='check_module_name'),
    # path('check-subModule-name', check_submodule_name,name='check_submodule_name'),

]