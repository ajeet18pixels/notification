from django.db import models
from django.contrib.auth.models import User
from .master_models import project_sector_Master,project_type_Master,Project_Technology_Master
from .employee_model import employeeDetails




class Project_Management(models.Model):
    project_name = models.CharField(max_length=200,unique=True)
    project_sector_FK = models.ForeignKey(project_sector_Master, verbose_name=("project_sector_FK"), on_delete=models.CASCADE)
    project_type_fk =  models.CharField(max_length=255,blank=True,null=True)
    # project_technology_fk = models.ManyToManyField(Project_Technology_Master, verbose_name=("project_technology_fk"),blank=True,null=True)
    project_technology_fk = models.CharField(max_length=200,blank=True,null=True)

    project_start_date = models.DateField(auto_now_add=False,blank=True,null=True)
    project_due_date = models.DateField(auto_now_add=False,blank=True,null=True)

    project_overview = models.TextField(blank=True,null=True)

    # project_manager = models.ManyToManyField(employeeDetails,symmetrical=False, verbose_name=("project_manager"),related_name='project_manager',blank=True,null=True)
    # project_team_member = models.ManyToManyField(employeeDetails,symmetrical=False, verbose_name=("project_team_member"),related_name='project_team_member',blank=True,null=True)
    project_manager = models.CharField(max_length=200,blank=True,null=True)
    project_team_member = models.CharField(max_length=200,blank=True,null=True)


    # upload_files = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)
    project_logo = models.ImageField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)

    upload_files = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)
    upload_files_1 = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)
    upload_files_2 = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)
    upload_files_3 = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)
    upload_files_4 = models.FileField(upload_to='Upload_Images/projectFiles/',blank=True,null=True)

    project_status = models.CharField(max_length=50,default="Just Created",blank=True,null=True)
    project_progress = models.IntegerField(default=0,blank=True,null=True)
    project_status_force_update = models.CharField(max_length=50,default="In Progress",blank=True,null=True)
    project_to_maintenance = models.BooleanField(default=False)



    project_url_for = models.CharField(max_length=150,blank=True,null=True)
    project_url = models.TextField(blank=True,null=True)
    project_url_for_1 = models.CharField(max_length=150,blank=True,null=True)
    project_url_1 = models.TextField(blank=True,null=True)
    project_url_for_2 = models.CharField(max_length=150,blank=True,null=True)
    project_url_2 = models.TextField(blank=True,null=True)
    project_url_for_3 = models.CharField(max_length=150,blank=True,null=True)
    project_url_3 = models.TextField(blank=True,null=True)
    project_url_for_4 = models.CharField(max_length=140,blank=True,null=True)
    project_url_4 = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name




class Module_management(models.Model):
    projectFK = models.ForeignKey(Project_Management, verbose_name=("projectFK"), on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=100)
    module_desc = models.TextField(blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.moduleName

    class Meta:
        unique_together = ('projectFK', 'moduleName',)


class Sub_module_management(models.Model):
    projectFK = models.ForeignKey(Project_Management, verbose_name=("projectFK"), on_delete=models.CASCADE)
    moduleFK = models.ForeignKey(Module_management, verbose_name=("moduleFK"), on_delete=models.CASCADE)
    subModuleName = models.CharField(max_length=100)
    subModule_desc = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        unique_together = ('projectFK', 'moduleFK','subModuleName',)