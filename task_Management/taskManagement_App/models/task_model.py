from django.db import models
from .employee_model import employeeDetails
from .project_model import Project_Management,Module_management,Sub_module_management


class Task_Management(models.Model):
    task_title = models.TextField()
    task_description = models.TextField(blank=True,null=True)
    
    projectFK = models.ForeignKey(Project_Management, verbose_name=("projectFK"), on_delete=models.CASCADE)
    moduleFK = models.ForeignKey(Module_management, verbose_name=("moduleFK"), on_delete=models.CASCADE)
    submoduleFK = models.ForeignKey(Sub_module_management, verbose_name=("submoduleFK"), on_delete=models.CASCADE,blank=True,null=True)
    employeeFK = models.ForeignKey(employeeDetails, verbose_name=("employeeFK"), on_delete=models.CASCADE)

    due_date = models.DateField()
    due_time = models.TimeField()

    priority = models.CharField(max_length=10)
    task_status = models.CharField(default='To do', max_length=10)

    dependencies = models.TextField(blank=True,null=True)
    created_by = models.CharField(max_length=20,blank=True,null=True)
    created_by_user_email = models.CharField(max_length=200,blank=True,null=True)


    updated_by = models.CharField(max_length=20,blank=True,null=True)
    updated_by_user_email = models.CharField(max_length=200,blank=True,null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    completed_at = models.DateField(blank=True,null=True)
    reviewed_at = models.DateField(blank=True,null=True)
    delayed_by_diff = models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.task_title