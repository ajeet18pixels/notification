from django.urls import path
from taskManagement_App.view.events_view import *


urlpatterns = [
    path('event-list', event_list,name='event_list'),


    path('birthday', birthday,name='birthday'),
    path('add-birthday/<int:id>',add_birthday,name='add_birthday'),
    path('check_existing_cultural_event/<int:id>', check_existing_cultural_event,name='check_existing_cultural_event'),


    path('anniversary', anniversary,name='anniversary'),
    path('add-anniversary/<int:id>',add_anniversary,name='add_anniversary'),
    path('check_existing_anniversary/<int:id>', check_existing_anniversary,name='check_existing_anniversary'),
    path('send-message-anniversary', send_wish_anniversary,name='send_wish_anniversary'),
    path('schedule-message-anniversary', schedule_wish_anniversary,name='schedule_wish_anniversary'),



    path('cultural-events', cultural_events,name='cultural_event'),
    path('add-cultural-event/<int:id>',add_cultural_event,name='add_cultural_event'),
    path('check_existing_birthday/<int:id>', check_existing_birthday,name='check_existing_birthday'),
    path('send-message-culturalevent', send_wish_culturalevent,name='send_wish_culturalevent'),
    path('shedule-message-culturalevent', schedule_wish_culturalevent,name='schedule_wish_culturalevent'),

    
    path('wishes-list', wishes_list,name='wishes_list'),


    path('event-archieves-list', archieves_list,name='archieves_list'),


    path('send-message', send_wish,name='send_wish'),
    path('schedule-message', schedule_wish,name='schedule_wish'),

    path('get_wish_data/<int:id>', get_wish_data,name='get_wish_data'),
    # path('get_leave_record_history/<int:id>', get_leave_record_history,name='get_leave_record_history'),
    # path('get_module_list/<int:id>', get_module_list,name='get_module_list'),

    # path('deleteProject/<int:id>', deleteProject,name='deleteProject'),

    # path('check-module-name', check_module_name,name='check_module_name'),
    # path('check-subModule-name', check_submodule_name,name='check_submodule_name'),

]