from django.urls import path
from taskManagement_App.view.master_view import *


urlpatterns = [
    path('designation-master', designation_master,name='designation_master'),
    path('get-specific-designation-master/<int:id>', get_specific_designation_master,name='get_specific_designation_master'),
    path('designation-master-check', check_designation_master,name='check_designation_master'),
    path('designation-master-edit/<int:id>', edit_designation_master,name='edit_designation_master'),
    path('designation-master-delete/<int:id>', delete_designation_master,name='delete_designation_master'),


    path('qualification-master', qualification_master,name='task_management'),
    path('get-specific-qualification-master/<int:id>', get_specific_qualification_master,name='get_specific_qualification_master'),
    path('qualification-master-check', check_qualification_master,name='check_qualification_master'),
    path('qualification-master-edit/<int:id>', edit_qualification_master,name='edit_qualification_master'),
    path('qualification-master-delete/<int:id>', delete_qualification_master,name='delete_qualification_master'),


    path('project-sector-master', project_sector_master,name='project_sector_master'),
    path('get-specific-project-sector-master/<int:id>', get_specific_project_sector_master,name='get_specific_project_sector_master'),
    path('project-sector-master-check', check_project_sector_master,name='check_project_sector_master'),
    path('project-sector-master-edit/<int:id>', edit_project_sector_master,name='edit_project_sector_master'),
    path('project-sector-master-delete/<int:id>', delete_project_sector_master,name='delete_project_sector_master'),


    path('project-type-master', project_type_master,name='project_type_master'),
    path('get-specific-project-type-master/<int:id>', get_specific_project_type_master,name='get_specific_project_type_master'),
    path('project-type-master-check', check_project_type_master,name='check_project_type_master'),
    path('project-type-master-edit/<int:id>', edit_project_type_master,name='edit_project_type_master'),
    path('project-type-master-delete/<int:id>', delete_project_type_master,name='delete_project_type_master'),


    path('project-tech-master', project_tech_master,name='project_tech_master'),
    path('get-specific-project-tech-master/<int:id>', get_specific_project_tech_master,name='get_specific_project_tech_master'),
    path('project-tech-master-check', check_project_tech_master,name='check_project_tech_master'),
    path('project-tech-master-edit/<int:id>', edit_project_tech_master,name='edit_project_tech_master'),
    path('project-tech-master-delete/<int:id>', delete_project_tech_master,name='delete_project_tech_master'),


    path('event-highlight-master', event_highlight_master,name='event_highlight_master'),
    path('get-specific-event-highlight-master/<int:id>', get_specific_event_highlight_master,name='get_specific_event_highlight_master'),
    path('event-highlight-master-check', check_event_highlight_master,name='check_event_highlight_master'),
    path('event-highlight-master-edit/<int:id>', edit_event_highlight_master,name='edit_event_highlight_master'),
    path('event-highlight-master-delete/<int:id>', delete_event_highlight_master,name='delete_event_highlight_master'),


    path('cultural-event-master', cultural_event_master,name='cultural_event_master'),
    path('get-specific-cultural-event-master/<int:id>', get_specific_cultural_event_master,name='get_specific_cultural_event_master'),
    path('cultural-event-master-check', check_cultural_event_master,name='check_cultural_event_master'),
    path('cultural-event-master-edit/<int:id>', edit_cultural_event_master,name='edit_cultural_event_master'),
    path('cultural-event-master-delete/<int:id>', delete_cultural_event_master,name='delete_cultural_event_master'),


    path('documentType-master', documentType_master,name='documentType_master'),
    path('get-specific-documentType-master/<int:id>', get_specific_documentType_master,name='get_specific_documentType_master'),
    path('documentType-master-check', check_documentType_master,name='check_documentType_master'),
    path('documentType-master-edit/<int:id>', edit_documentType_master,name='edit_documentType_master'),
    path('documentType-master-delete/<int:id>', delete_documentType_master,name='delete_documentType_master'),


    path('passingYear-master', passingYear_master,name='passingYear_master'),
    path('get-specific-passingYear-master/<int:id>', get_specific_passingYear_master,name='get_specific_passingYear_master'),
    path('passingYear-master-check', check_passingYear_master,name='check_passingYear_master'),
    path('passingYear-master-edit/<int:id>', edit_passingYear_master,name='edit_passingYear_master'),
    path('passingYear-master-delete/<int:id>', delete_passingYear_master,name='delete_passingYear_master'),


    path('location-master', location_master,name='location_master'),
    path('get-specific-location-master/<int:id>', get_specific_location_master,name='get_specific_location_master'),
    path('location-master-check', check_location_master,name='check_location_master'),
    path('location-master-edit/<int:id>', edit_location_master,name='edit_location_master'),
    path('location-master-delete/<int:id>', delete_location_master,name='delete_location_master'),
]