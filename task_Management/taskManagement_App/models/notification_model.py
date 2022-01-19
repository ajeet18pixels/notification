from django.db import models
from django.contrib.auth.models import User




class Notification_Management(models.Model):
    notification_to = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE,null=True,blank=True)
    notification_from = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE,null=True,blank=True)

    notification_subject = models.CharField(max_length=255,blank=True,null=True)
    notification_message = models.TextField(blank=True,null=True)

    # notification_type = models.CharField(max_length=50,default='single')

    admin_read_status = models.BooleanField(default=False)
    manager_read_status = models.BooleanField(default=False)
    emp_read_status = models.BooleanField(default=False)

    admin_trash_status = models.BooleanField(default=False)
    manager_trash_status = models.BooleanField(default=False)
    emp_trash_status = models.BooleanField(default=False)

    admin_starred_status = models.BooleanField(default=False)
    manager_starred_status = models.BooleanField(default=False)
    emp_starred_status = models.BooleanField(default=False)


    notification_location = models.CharField(max_length=50,default='inbox',null=True,blank=True)
    member_count = models.CharField(max_length=10,default=1,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.notification_subject


# class Notification_Management(models.Model):
#     notification_sender = models.CharField(max_length=255,blank=True,null=True)
#     notification_title = models.CharField(max_length=255,blank=True,null=True)
#     notification_description = models.TextField(blank=True,null=True)
#     notification_type = models.CharField(max_length=10,default='single',blank=True,null=True)  #single/multiple

#     notification_creatives = models.FileField(upload_to='Upload_Images/notification_Creatives/',blank=True,null=True)
#     notification_userCount = models.CharField(max_length=10,default=1,blank=True,null=True)

#     notification_read_status = models.BooleanField(default=False,blank=True,null=True)
#     notification_admin_read_status = models.BooleanField(default=False,blank=True,null=True)
#     notification_delete_status = models.BooleanField(default=False,blank=True,null=True)
 
#     created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
#     updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

#     def __str__(self):
#         return self.notification_title



# class Notification_reciepents(models.Model):
#     notificationFK = models.ForeignKey(Notification_Management,verbose_name=("notificationFK"), on_delete=models.CASCADE,blank=True,null=True)
#     notification_receiver = models.CharField(max_length=255,blank=True,null=True)

#     created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
#     updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

#     def __str__(self):
#         return self.notification_receiver
