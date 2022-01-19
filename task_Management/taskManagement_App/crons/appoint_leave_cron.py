from ..models.leave_model import *
from ..models.employee_model import *
from django.contrib.auth.models import User
from taskManagement_App.models.notification_model import Notification_Management

from datetime import date,datetime

# #####################################################################################################################
'''Add monthly paid leave to employee account whose employement is greter than 180 days on 01 of every month'''
# #####################################################################################################################
def allocate_leave():
   # =======================================================================
   users = User.objects.filter(is_superuser = False,is_active=True)
   for i in users:
         print(i.first_name)
         empObj1 = employeeDetails.objects.get(userFK=i)
         date1 = empObj1.joiningDate
         date2 = date.today()
         diff = date2 - date1
         print(diff, "days")
         if(int(diff.days) >= 180):
            allotObj = leave_allotment_management(
               employeeFK = empObj1,
               no_of_days = 1,
               leave_reason = f'{datetime.now().strftime("%B")} month paid leave.'
            )
            allotObj.save()

            # ######################################################################################################################
            # new notification for sending happy birthday wishes
            # ######################################################################################################################
            # mydate = datetime.datetime.now()
            # mydate.strftime("%B")
            notification_obj = Notification_Management(notification_to=i,notification_from=User.objects.get(username='admin@gmail.com'),
                                                        notification_subject='Monthly paid leave alloted.',
                                                        notification_message=f'Monthly paid leave for the month {datetime.now().strftime("%B")} has been added to your account.'
                                                        )
            notification_obj.save()
            # ######################################################################################################################

            # empObj1.alloted_leave = int(empObj1.alloted_leave) + 1
            # empObj1.remaining_leave = int(empObj1.remaining_leave) + 1
            # empObj1.save()
   # =======================================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
