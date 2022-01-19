from django.urls import path
from taskManagement_App.view.reports_view import *


urlpatterns = [

    path('employee-report', employee_report,name='employee_report'),
    path('download-excel-report', download_excel_data,name='download_excel_data'),

    path('holiday-report', holiday_report,name='holiday_report'),

    path('project-report', project_report,name='project_report'),
    path('leave-report', leave_report,name='leave_report'),

    path('event-report', event_report,name='event_report'),
    path('job-application-report', job_application_report,name='job_application_report'),

]