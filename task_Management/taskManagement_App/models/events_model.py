from django.db import models
from django.contrib.auth.models import User
from .employee_model import employeeDetails
from .master_models import culturalEvent_Master

# ###############################################################################################################################
class event_bday_annivarsary_management(models.Model):
    employeeFK = models.ForeignKey(employeeDetails, verbose_name=("employee_FK"),related_name='employeeFK', on_delete=models.CASCADE,blank=True,null=True)
    event_year = models.CharField(max_length=20,blank=True,null=True)
    event_date = models.DateField(blank=True,null=True)
    event_status = models.CharField(max_length=20,blank=True,null=True,default='created')
    event_highlight = models.CharField(max_length=255,blank=True,null=True)
    event_budget = models.CharField(max_length=10,blank=True,null=True)
    event_type = models.CharField(max_length=20,blank=True,null=True)

    # ---------------------------------------------------------------------------------------------------------------------------
    #                                              EVENT MANAGEMENT DATA
    # ---------------------------------------------------------------------------------------------------------------------------
    cultural_eventFK = models.ForeignKey(culturalEvent_Master, verbose_name=("cultural_eventFK"), on_delete=models.CASCADE,blank=True,null=True)
    cultural_event_title = models.CharField(max_length=255,blank=True,null=True)
    cultural_event_manager = models.ForeignKey(employeeDetails, verbose_name=("cultural_event_manager"),related_name='cultural_event_manager',on_delete=models.CASCADE,blank=True,null=True)
    special_performance = models.TextField(blank=True,null=True)
    cultural_event_creative = models.FileField(upload_to='Upload_Images/cultural_event_creatives/',blank=True,null=True)
    # ---------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.event_type)

# ###############################################################################################################################
# ###############################################################################################################################
# ###############################################################################################################################
class event_wishes(models.Model):
    eventFK = models.ForeignKey(event_bday_annivarsary_management, verbose_name=("eventFK"), on_delete=models.CASCADE,blank=True,null=True)
    senderFK = models.ForeignKey(User, verbose_name=("sender_FK"), related_name='sender_fk',on_delete=models.CASCADE,blank=True,null=True)
    receiverFK = models.ForeignKey(employeeDetails, verbose_name=("employee_FK"), related_name='receiver_fk', on_delete=models.CASCADE,blank=True,null=True)
    message_title = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    creative = models.FileField(upload_to='Upload_Images/creatives/',blank=True,null=True)

    wish_type = models.CharField(max_length=50,blank=True,null=True,default='direct')
    wish_schedule_time = models.DateField(blank=True,null=True)
    wish_status = models.CharField(max_length=20,blank=True,null=True,default='sent')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

# ###############################################################################################################################
