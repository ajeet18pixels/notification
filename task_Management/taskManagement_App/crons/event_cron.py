from ..models.events_model import *
from datetime import date
from taskManagement_App.models.notification_model import Notification_Management

# #####################################################################################################################
'''send scheduled messages to the receiver @ 12:05 AM as notification and also as wish'''
# #####################################################################################################################
def send_scheduled_message():
    wishObj = event_wishes.objects.filter(wish_status='scheduled',wish_schedule_time=date.today())
    print('len(wishObj) >>> ',len(wishObj))
    for i in wishObj:
        try:
            i.wish_status = 'sent'
            i.save()
            # ######################################################################################################################
            # new notification for sending happy birthday wishes
            # ######################################################################################################################
            notification_obj = Notification_Management(notification_to=i.receiverFK.userFK,notification_from=i.senderFK,
                                                        notification_subject=f'{i.message_title}',
                                                        notification_message=f'{i.message}'
                                                        )
            notification_obj.save()
            # ######################################################################################################################
        except:
            print(i)

# #####################################################################################################################
'''send birthday/anniversary and events messages to the receiver @ 12:00 AM as notification and also as wish'''
# #####################################################################################################################
def send_wishes():
    pass

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
