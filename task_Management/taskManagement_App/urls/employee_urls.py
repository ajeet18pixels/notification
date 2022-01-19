from django.urls import path
from taskManagement_App.view.employee_view import *


urlpatterns = [
    path('employee-list', employee_list,name='employee_list'),
    path('add-employee', add_employee,name='add_employee'),
    

    path('view-employee-detail/<int:id>', view_employee_detail,name='view_employee_detail'),
    path('update-employee-detail/<int:id>', update_employee_detail,name='update_employee_detail'),
    path('update_employee_active_status/<int:id>', update_employee_active_status,name='update_employee_active_status'),
    path('delete_employee/<int:id>', delete_employee,name='delete_employee'),


    path('check-employee-email', check_emp_email,name='check_emp_email'),
    path('check-employee-contact', check_emp_contact,name='check_emp_contact'),


    path('send_credentials/<int:id>', send_credentials,name='send_credentials'),
    path('update-profile', update_profile,name='update_profile'),
    path('request-edit', request_edit,name='request_edit'),


    path('filter-users', filter_users,name='filter_users'),


]

