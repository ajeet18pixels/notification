from django.urls import path
from taskManagement_App.view.leave_view import *


urlpatterns = [
    path('leave-record', get_leave_record,name='get_leave_record'),
    path('add-leave', add_leave,name='add_leave'),
    path('get_leave_record_history/<int:id>', get_leave_record_history,name='get_leave_record_history'),
    path('leave-request', get_leave_requests,name='get_leave_requests'),
    path('handle-leave-requests/<int:id>',handle_leave_requests,name='handle_leave_requests'),



    path('cancel_leave_request/<int:id>', cancel_leave_request,name='cancel_leave_request'),
    path('cancel_leave_request_to_admin/<int:id>', cancel_leave_request_to_admin,name='cancel_leave_request_to_admin'),



    path('edit_leave_request/<int:id>', edit_leave_request,name='edit_leave_request'),
    path('edit_leave/<int:id>', edit_leave,name='edit_leave'),
    path('fetch_leave/<int:id>', fetch_leave,name='fetch_leave'),



    path('leave-allotment', get_leave_allotment,name='get_leave_allotment'),
    path('allot-leave', allot_leave,name='allot_leave'),
    path('delete_alloted_leave/<int:id>', delete_alloted_leave,name='delete_alloted_leave'),


    path('holiday-list', holiday_list,name='holiday_list'),
    path('deleteHoliday/<int:id>', deleteHoliday,name='deleteHoliday'),
    path('fetchHoliday/<int:id>', fetchHoliday,name='fetchHoliday'),
    path('edit-holiday/<int:id>', edit_holiday,name='edit_holiday'),


    path('get-alloted-leave-record', get_alloted_leave_record,name='get_alloted_leave_record'),

]