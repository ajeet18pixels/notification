from django.db import models
from django.contrib.auth.models import User
from .project_model import Project_Management


class file_management(models.Model):
    userFK = models.ForeignKey(User, on_delete=models.CASCADE)
    projectFK = models.ForeignKey(Project_Management, on_delete=models.CASCADE,blank=True,null=True)

    file_title = models.CharField(max_length=150)
    file_type = models.CharField(max_length=30)
    file = models.FileField(upload_to='Upload_Images/file_management/projectFiles/')

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)


