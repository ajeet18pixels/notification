from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('taskManagement_App.urls.urls')),
    path('employee-management/',include('taskManagement_App.urls.employee_urls')),
    path('project-management/',include('taskManagement_App.urls.project_urls')),
    path('task-management/',include('taskManagement_App.urls.task_urls')),
    path('master-management/',include('taskManagement_App.urls.master_urls')),
    path('notification-management/',include('taskManagement_App.urls.notification_urls')),
    path('leave-management/',include('taskManagement_App.urls.leave_urls')),
    path('log-management/',include('taskManagement_App.urls.log_urls')),
    path('event-management/',include('taskManagement_App.urls.events_urls')),
    path('report-management/',include('taskManagement_App.urls.reports_urls')),
    path('hr-management/',include('taskManagement_App.urls.hr_urls')),
    path('file-management/',include('taskManagement_App.urls.file_urls')),

    # path('api/',include('taskManagement_App.urls.hr_urls')),

]

# handler404 = "task_Management.views.error_404_view"


# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()