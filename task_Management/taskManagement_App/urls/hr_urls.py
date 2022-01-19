from django.urls import path
from taskManagement_App.view.hr_view import *
# from ..view.APIs import job_list

urlpatterns = [

    path('received-application_-list', received_application_list,name='received_application_list'),
    path('add-applications', add_applications,name='add_applications'),
    path('edit-application-status/<int:id>', edit_application_status,name='edit_application_status'),
    path('get-application-info/<int:id>', get_application_info,name='get_application_info'),
    path('delete_application/<int:id>', delete_application,name='delete_application'),


    path('job-list', job_list,name='job_list'),
    path('add-new-job', add_new_job,name='add_new_job'),
    path('edit-job/<int:id>', edit_job_detail,name='edit_job_detail'),
    path('edit-job-visibility/<int:id>', edit_job_visibility,name='edit_job_visibility'),
    path('delete-job/<int:id>', delete_job,name='delete_job'),
    path('fetch-job/<int:id>', fetch_job,name='fetch_job'),


    path('sent-message-archives', sent_message_archives,name='sent_message_archives'),
    path('send-message/<int:id>', send_message,name='send_message'),
    path('delete_message/<int:id>', delete_message,name='delete_message'),
    
    
    path('interview-archives', interview_archives,name='interview_archives'),
    path('schedule-interview/<int:id>', schedule_interview,name='schedule_interview'),

    path('latest-jobs', latest_job_list,name='latest_job_list'),
    path('apply-for-job', job_application_apply,name='job_application_apply'),
    path('get-experience', get_experience,name='get_experience'),


]

