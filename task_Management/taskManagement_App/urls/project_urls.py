from django.urls import path
from taskManagement_App.view.project_view import *


urlpatterns = [
    path('add-project', add_project,name='add_project'),
    path('project-list', project_list,name='project_list'),
    path('project-detail/<int:id>', project_detail,name='project_detail'),
    path('filter-project', filter_project,name='filter_project'),
    path('update-project-detail/<int:id>',update_project,name='update_project'),

    path('force-update-project-status/<int:id>',force_update_project_status,name='force_update_project_status'),


    path('get_selected_project_module_list/<int:id>', get_selected_project_module_list,name='get_selected_project_module_list'),
    path('get_selected_project_subModule_list/<int:id>', get_selected_project_subModule_list,name='get_selected_project_subModule_list'),


    path('add-module', create_module,name='create_module'),
    path('add-submodule', create_sub_module,name='create_sub_module'),
    path('module-list', module_list,name='module_list'),
    path('submodule-list', sub_module_list,name='sub_module_list'),

    path('edit-module', edit_module,name='edit_module'),
    path('delete-module', delete_module,name='delete_module'),

    path('edit-submodule', edit_submodule,name='edit_submodule'),
    path('delete-submodule', delete_submodule,name='delete_submodule'),

    path('check-project-name', checkProject,name='checkProject'),
    path('deleteProject/<int:id>', deleteProject,name='deleteProject'),

    path('check-module-name', check_module_name,name='check_module_name'),
    path('check-subModule-name', check_submodule_name,name='check_submodule_name'),



    path('change_to_maintenace_mode/<int:id>', change_to_maintenace_mode,name='change_to_maintenace_mode'),
    path('change_to_development_mode/<int:id>', change_to_development_mode,name='change_to_development_mode'),



]
