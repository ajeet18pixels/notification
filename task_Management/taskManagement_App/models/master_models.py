from django.db import models
from django.contrib.auth.models import User

# userFK = models.ForeignKey(User, verbose_name=("User ID"), on_delete=models.CASCADE)
# Create your models here.
class designation_Master(models.Model):
    designation_name = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.designation_name



class eventType_Master(models.Model):
    event_type = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)



class holiday_Master(models.Model):
    holiday_name = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)


class document_Master(models.Model):
    document_type = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

class qualification_Master(models.Model):
    qualification_type = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)


class passingYear_Master(models.Model):
    passingYear = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

class experience_Master(models.Model):
    experience = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return str(self.experience)


class employeeType_Master(models.Model):
    employee_type_name = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.employee_type_name


class culturalEvent_Master(models.Model):
    event_name = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)



class event_highlight_Master(models.Model):
    highlight_name = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.event_name

class project_sector_Master(models.Model):
    sector = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.sector


class project_type_Master(models.Model):
    projectType = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.projectType


class Project_Technology_Master(models.Model):
    Technology = models.CharField(unique=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.Technology



class Location_master(models.Model):
    location = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.location


class secretKey(models.Model):
    secret_key = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)