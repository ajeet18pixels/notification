from django.urls import path
from taskManagement_App.view.notification_view import *


urlpatterns = [
    path('notification', notification,name='notification'),
    path('delete-notification/<int:id>', delete_notification,name='delete_notification'),
    path('read-notification/<int:id>',read_notification,name='read_notification'),
    path('unread-notification/<int:id>',unread_notification,name='unread_notification'),

    # path('project-list', project_list,name='project_list'),
    # path('filter-project', filter_project,name='filter_project'),
    path('view-notification/<int:id>', view_notification,name='view_notification'),


    path('move-to-trash/<int:id>', move_to_trash,name='move_to_trash'),
    path('move-to-starred/<int:id>', move_to_starred,name='move_to_starred'),
    path('remove-from-starred/<int:id>', remove_from_starred,name='remove_from_starred'),

    path('get-selected-notification', get_selected_notification,name='get_selected_notification'),
    # path('view-notification/<int:id>', view_notification,name='view_notification'),
    path('notificationPagination', notificationPagination,name='notificationPagination'),
    

]