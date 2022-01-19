from django.urls import path
from taskManagement_App.view.file_view import *

urlpatterns = [

    path('add-file', add_files,name='add_files'),
    path('file-list', files_list,name='files_list'),
    path('delete_files/<int:id>', delete_files,name='delete_files'),
    # path('get-application-info/<int:id>', get_application_info,name='get_application_info'),

]

