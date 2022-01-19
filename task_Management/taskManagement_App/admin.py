from django.contrib import admin
from .models.master_models import designation_Master,eventType_Master,holiday_Master,document_Master,culturalEvent_Master,employeeType_Master,qualification_Master,passingYear_Master,experience_Master,project_type_Master,project_sector_Master,Project_Technology_Master,event_highlight_Master,Location_master,secretKey
from .models.employee_model import employeeDetails,employee_Password,employee_request_edit
from .models.project_model import Project_Management,Module_management,Sub_module_management
from .models.task_model import Task_Management
from .models.leave_model import leave_management,holiday_management,leave_allotment_management
from .models.events_model import event_bday_annivarsary_management,event_wishes
from .models.hr_models import jobs,job_application,message_archieve
from .models.file_model import file_management
# Register your models here.
from .models.notification_model import Notification_Management

from .models.logs_model import AuditEntry

from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)


@admin.register(jobs)
class jobs(admin.ModelAdmin):
    list_display = ('id', 'position','visibility_status','job_location','job_description','created_at')
    list_filter = ['position','visibility_status']

@admin.register(job_application)
class job_application(admin.ModelAdmin):
    list_display = ('id', 'job_FK','candidate_name','email','contact','status','interviewDate','interviewer_name')
    list_filter = ['job_FK','status']

@admin.register(message_archieve)
class message_archieve(admin.ModelAdmin):
    list_display = ('id', 'applicationFK','message_text','created_at')


@admin.register(event_highlight_Master)
class event_highlight_Master(admin.ModelAdmin):
    list_display = ('id', 'highlight_name','created_at')


@admin.register(event_bday_annivarsary_management)
class event_bday_annivarsary_management(admin.ModelAdmin):
    list_display = ('id', 'employeeFK', 'event_year', 'event_status', 'event_type','created_at')
    list_filter = ['employeeFK','event_year','event_status','event_type']


@admin.register(event_wishes)
class event_wishes(admin.ModelAdmin):
    list_display = ('id', 'eventFK', 'senderFK', 'receiverFK', 'message_title', 'wish_type','wish_schedule_time','created_at')
    list_filter = ['eventFK','senderFK','receiverFK','wish_type']


@admin.register(secretKey)
class secretKey(admin.ModelAdmin):
    list_display = ('secret_key','created_at')

  
@admin.register(employee_Password)
class employee_Password(admin.ModelAdmin):
    list_display = ('id', 'userFK','created_at')

  
@admin.register(employee_request_edit)
class employee_request_edit(admin.ModelAdmin):
    list_display = ('id', 'userFK','request_status','request_edit','created_at')


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ('action', 'username', 'ip','created_at')
    list_filter = ['action','username']

@admin.register(leave_management)
class leave_management(admin.ModelAdmin):
  list_display = ('id', 'employeeFK', 'leave_date_from','leave_date_to','leave_reason','leave_approval_status','created_at', 'updated_at')
  list_filter = ['employeeFK','leave_approval_status']


@admin.register(leave_allotment_management)
class leave_allotment_management(admin.ModelAdmin):
  list_display = ('id', 'employeeFK', 'no_of_days','leave_reason','created_at', 'updated_at')
  list_filter = ['employeeFK']


@admin.register(holiday_management)
class holiday_management(admin.ModelAdmin):
  list_display = ('id', 'holiday_name', 'holiday_fromDate','holiday_toDate','holiday_number','holiday_year','created_at', 'updated_at')
  list_filter = ['holiday_year']


@admin.register(designation_Master)
class designation_Master(admin.ModelAdmin):
  list_display = ('id', 'designation_name', 'created_at', 'updated_at')


@admin.register(eventType_Master)
class eventType_Master(admin.ModelAdmin):
  list_display = ('id', 'event_type', 'created_at', 'updated_at')


@admin.register(holiday_Master)
class holiday_Master(admin.ModelAdmin):
  list_display = ('id', 'holiday_name', 'created_at', 'updated_at')


@admin.register(document_Master)
class document_Master(admin.ModelAdmin):
  list_display = ('id', 'document_type', 'created_at', 'updated_at')



@admin.register(qualification_Master)
class qualification_Master(admin.ModelAdmin):
  list_display = ('id', 'qualification_type', 'created_at', 'updated_at')


@admin.register(culturalEvent_Master)
class culturalEvent_Master(admin.ModelAdmin):
  list_display = ('id', 'event_name', 'created_at', 'updated_at')


@admin.register(employeeType_Master)
class employeeType_Master(admin.ModelAdmin):
  list_display = ('id', 'employee_type_name', 'created_at', 'updated_at')


@admin.register(passingYear_Master)
class passingYear_Master(admin.ModelAdmin):
  list_display = ('id', 'passingYear', 'created_at', 'updated_at')


@admin.register(experience_Master)
class experience_Master(admin.ModelAdmin):
  list_display = ('id', 'experience', 'created_at', 'updated_at')



@admin.register(employeeDetails)
class employeeDetails(admin.ModelAdmin):
  list_display = ('id', 'userFK', 'employee_name','contact','DOB','designationFK','employeeTypeFK','created_at', 'updated_at')
  list_filter = ['designationFK','employeeTypeFK']


@admin.register(project_sector_Master)
class project_sector_Master(admin.ModelAdmin):
  list_display = ('id', 'sector', 'created_at', 'updated_at')


@admin.register(project_type_Master)
class project_type_Master(admin.ModelAdmin):
  list_display = ('id', 'projectType', 'created_at', 'updated_at')


@admin.register(Project_Technology_Master)
class Project_Technology_Master(admin.ModelAdmin):
  list_display = ('id', 'Technology', 'created_at', 'updated_at')



@admin.register(Project_Management)
class Project_Management(admin.ModelAdmin):
  list_display = ('id', 'project_name', 'project_sector_FK', 'project_start_date','project_status','project_progress', 'created_at', 'updated_at')
  list_filter = ['project_sector_FK','project_progress','project_status']



@admin.register(Module_management)
class Module_management(admin.ModelAdmin):
  list_display = ('id', 'projectFK','moduleName', 'created_at', 'updated_at')
  list_filter = ['projectFK']




@admin.register(Sub_module_management)
class Sub_module_management(admin.ModelAdmin):
  list_display = ('id', 'projectFK','moduleFK','subModuleName', 'created_at', 'updated_at')
  list_filter = ['projectFK']



@admin.register(Task_Management)
class Task_Management(admin.ModelAdmin):
  list_display = ('id', 'task_title', 'task_description', 'projectFK','moduleFK','submoduleFK', 'employeeFK', 'due_date','due_time','priority','task_status','dependencies','created_at','updated_at')
  list_filter = ['projectFK','employeeFK','task_status','priority']



@admin.register(Notification_Management)
class Notification_Management(admin.ModelAdmin):
  list_display = ('id', 'notification_to', 'notification_from','notification_subject','notification_message','admin_read_status','manager_read_status','emp_read_status', 'notification_location','member_count', 'created_at')


@admin.register(file_management)
class file_management(admin.ModelAdmin):
  list_display = ('id','userFK','projectFK','file_title','created_at')
  list_filter = ['file_type']




@admin.register(Location_master)
class Location_master(admin.ModelAdmin):
  list_display = ('id','location','created_at')
