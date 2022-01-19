
from django.db import models
from django.contrib.auth.models import User
from .employee_model import employeeDetails


class leave_management(models.Model):
    employeeFK = models.ForeignKey(employeeDetails, verbose_name=("employee_FK"), on_delete=models.CASCADE)
    leave_date_from = models.DateField(blank=True,null=True)
    leave_date_to = models.DateField(blank=True,null=True)
    leave_reason = models.TextField(blank=True,null=True)
    leave_approval_status = models.CharField(max_length=50,blank=True,null=True,default='pending')

    edit_leave_request = models.CharField(max_length=255,blank=True,null=True)
    edit_date_from = models.DateField(blank=True,null=True)
    edit_date_to = models.DateField(blank=True,null=True)

    request_edit_date = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.employeeFK.employee_name)


class leave_allotment_management(models.Model):
    employeeFK = models.ForeignKey(employeeDetails, verbose_name=("employee_FK"), on_delete=models.CASCADE)
    no_of_days = models.CharField(max_length=10,blank=True,null=True)
    leave_reason = models.TextField(blank=True,null=True,default="Monthly Paid Leave")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.employeeFK.employee_name)


class holiday_management(models.Model):
    holiday_name = models.CharField(max_length=100,blank=True,null=True)
    holiday_fromDate = models.DateField(blank=True,null=True)
    holiday_toDate = models.DateField(blank=True,null=True)
    holiday_number = models.CharField(max_length=10,blank=True,null=True)
    holiday_year = models.CharField(max_length=10,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.holiday_name)+' | '+str(self.holiday_fromDate)+' | '+str(self.holiday_year) 

    class Meta:
        unique_together = ('holiday_name', 'holiday_fromDate','holiday_toDate','holiday_year','holiday_number')
    