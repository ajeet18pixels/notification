from django.db import models
from django.contrib.auth.models import User
from .employee_model import employeeDetails
from .master_models import designation_Master,experience_Master
# from tinymce.models import HTMLField 


class jobs(models.Model):
    position = models.ForeignKey("designation_Master", verbose_name=("DesignationFK"), on_delete=models.CASCADE)
    job_location = models.CharField(max_length=255,blank=True,null=True)
    job_description = models.TextField()
    visibility_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.position.designation_name)





class job_application(models.Model):
    job_FK = models.ForeignKey("jobs", verbose_name=("job_FK"), on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    experienceFK = models.ForeignKey("experience_Master", verbose_name=("experienceFK"), on_delete=models.CASCADE)
    status = models.CharField(default='Applied', max_length=50)
    resume_doc = models.FileField(upload_to='Upload_Images/applicants_resume/',blank=True,null=True)
    applicationData = models.DateField(blank=True,null=True)

    interviewDate = models.DateField(blank=True,null=True)
    interviewer_name = models.CharField(max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.candidate_name


class message_archieve(models.Model):
    applicationFK = models.ForeignKey("job_application", verbose_name=("applicationFK"), on_delete=models.CASCADE)
    message_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
