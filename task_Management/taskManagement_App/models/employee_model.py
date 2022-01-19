from django.db import models
from django.contrib.auth.models import User
from .master_models import employeeType_Master,designation_Master,experience_Master
# userFK = models.ForeignKey(User, verbose_name=("User ID"), on_delete=models.CASCADE)

class employeeDetails(models.Model):
    userFK = models.ForeignKey(User, verbose_name=("UserFk"), on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=50,blank=True,null=True)
    father_name = models.CharField(max_length=50,blank=True,null=True)

    state = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.CharField(max_length=6,blank=True,null=True)


    contact = models.CharField(max_length=10,unique=True)
    alternate_contact = models.CharField(max_length=10,blank=True,null=True)
    DOB = models.DateField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    designationFK = models.ForeignKey(designation_Master, verbose_name=("Designation"), on_delete=models.CASCADE,blank=True,null=True)
    employeeTypeFK = models.ForeignKey(employeeType_Master, verbose_name=("Employee Type"), on_delete=models.CASCADE,blank=True,null=True)

    joiningDate = models.DateField(blank=True,null=True)
    qualification = models.TextField(blank=True,null=True)
    experience_year = models.ForeignKey(experience_Master, verbose_name=("Experience Year"), on_delete=models.CASCADE,blank=True,null=True)
    
    work_experience = models.TextField(blank=True,null=True)

    upload_docs_type = models.CharField(max_length=20,blank=True,null=True)
    upload_docs = models.FileField(upload_to='Upload_Images/employeeFiles/',blank=True,null=True)

    upload_docs_type_2 = models.CharField(max_length=20,blank=True,null=True)
    upload_docs_2 = models.FileField(upload_to='Upload_Images/employeeFiles/',blank=True,null=True)

    upload_docs_type_3 = models.CharField(max_length=20,blank=True,null=True)
    upload_docs_3 = models.FileField(upload_to='Upload_Images/employeeFiles/',blank=True,null=True)

    upload_docs_type_4 = models.CharField(max_length=20,blank=True,null=True)
    upload_docs_4 = models.FileField(upload_to='Upload_Images/employeeFiles/',blank=True,null=True)

    upload_docs_type_5 = models.CharField(max_length=20,blank=True,null=True)
    upload_docs_5 = models.FileField(upload_to='Upload_Images/employeeFiles/',blank=True,null=True)

    profile_image = models.ImageField(upload_to='Upload_Images/profileImages/',blank=True,null=True)

    alloted_leave = models.CharField(max_length=20,blank=True,null=True,default=0)
    taken_leave = models.CharField(max_length=20,blank=True,null=True,default=0)
    remaining_leave = models.CharField(max_length=20,blank=True,null=True,default=0)

    send_credentials = models.CharField(max_length=20,blank=True,null=True,default='not-sent')



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    # def __str__(self):
    #     return self.employee_name




class employee_Password(models.Model):
    userFK = models.ForeignKey(User, verbose_name=("UserFk"), on_delete=models.CASCADE)
    user_password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)




class employee_request_edit(models.Model):
    userFK = models.ForeignKey(User, verbose_name=("UserFk"), on_delete=models.CASCADE)
    request_edit = models.TextField(blank=True,null=True)
    request_status = models.TextField(default='pending',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)



