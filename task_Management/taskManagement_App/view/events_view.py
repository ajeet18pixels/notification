from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from taskManagement_App.models.notification_model import Notification_Management
from django.contrib.auth.decorators import login_required
from ..models.master_models import *
from ..models.employee_model import employeeDetails
from ..models.events_model import event_bday_annivarsary_management,event_wishes
# ########################################################################################################## 
@login_required(login_url='/')
def event_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            cultural_eventObj = culturalEvent_Master.objects.all()
            empObj = employeeDetails.objects.all()
            highlightObj = event_highlight_Master.objects.all()
            birthdayObj = event_bday_annivarsary_management.objects.filter(event_type = 'Birthday')
            anniversaryObj = event_bday_annivarsary_management.objects.filter(event_type = 'Anniversary')
            culturalEventObjObj = event_bday_annivarsary_management.objects.filter(event_type = 'CulturalEvent')
            empID = []
            empName = []
            for i in empObj:
                empID.append(i.id)
                empName.append(i.employee_name)
            return render(request,'admin/events/event-list.html',{'empID':empID,'empName':empName,'cultural_eventObj':cultural_eventObj,'empObj':empObj,'highlightObj':highlightObj,'birthdayObj_len':len(birthdayObj),'anniversaryObj_len':len(anniversaryObj),'culturalEventObjObj':len(culturalEventObjObj)})

        if(request.session['userType'] == 'teacheR' or request.session['userType'] == 'studdenT'):
            from datetime import date,timedelta
            today = date.today()
            birthdayObj_today = event_bday_annivarsary_management.objects.filter(event_date__month = today.month,event_date__day = today.day,event_year = today.year)
            highlightStr = ''
            highlightList = []
            for i in birthdayObj_today:
                if(i.employeeFK != None):
                    i.first_name = i.employeeFK.employee_name.split(' ')[0]
                    if(i.employeeFK.userFK == request.user):
                        i.view_data = 'no'
                    else:
                        i.view_data = 'yes'
                        for j in eval(i.event_highlight):
                            highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                            highlightStr = highlightStr + highlight_Obj.highlight_name + ','                    
                        i.highlightStr = highlightStr
                        i.first_name = i.employeeFK.employee_name.split(' ')[0]
                        highlightStr = ''
                else:
                    listData = eval(i.event_highlight)[0].split(',')
                    for j in listData:
                        highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                        highlightList.append(highlight_Obj.highlight_name)                                      
                    i.highlightStr = highlightList
                    highlightList = []
            date_today = date.today()
            startdate = date_today + timedelta(days=1)
            enddate = date_today + timedelta(days=30)
            birthdayObj_month = event_bday_annivarsary_management.objects.filter(event_date__range=[startdate, enddate],event_year = today.year).order_by('event_date')
            # =====================================================================
            # ==================  check date and add color   ======================
            highlightStr = ''
            highlightList = []
            for i in birthdayObj_month:
                if(i.employeeFK != None):
                    i.first_name = i.employeeFK.employee_name.split(' ')[0]
                    if(i.employeeFK.userFK == request.user):
                        i.view_data = 'no'
                    else:
                        i.view_data = 'yes'
                        i.first_name = i.employeeFK.employee_name.split(' ')[0]
                        d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                        d0 = date(today.year,today.month,today.day)
                        delta = d1 - d0
                        color = ""
                        if(delta.days <= 0):
                            color = 'secondary'
                        elif(delta.days <= 15):
                            color = 'danger'
                        elif(16 <= delta.days <= 25):
                            color = 'success'
                        elif(26 <= delta.days <= 35):
                            color = 'info'
                        elif(36 <= delta.days):
                            color = 'warning'
                        i.Color = color
                        for j in eval(i.event_highlight):
                            highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                            highlightStr = highlightStr + highlight_Obj.highlight_name + ','                    
                        i.highlightStr = highlightStr
                        highlightStr = ''
                else:
                    listData = eval(i.event_highlight)[0].split(',')
                    for j in listData:
                        highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                        highlightList.append(highlight_Obj.highlight_name)                   
                    i.highlightStr = highlightList
                    highlightList = []
                    d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                    d0 = date(today.year,today.month,today.day)
                    delta = d1 - d0
                    color = ""
                    if(delta.days <= 0):
                        color = 'secondary'
                    elif(delta.days <= 15):
                        color = 'danger'
                    elif(16 <= delta.days <= 25):
                        color = 'success'
                    elif(26 <= delta.days <= 35):
                        color = 'info'
                    elif(36 <= delta.days):
                        color = 'warning'
                    i.Color = color
            highlightObj = event_highlight_Master.objects.all()
            from datetime import date,timedelta
            today = date.today()
            culturalObj = event_bday_annivarsary_management.objects.filter(event_year = today.year,event_type = 'CulturalEvent').order_by('event_date')
            highlightStr = []
            for i in culturalObj:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                if(delta.days <= 0):
                    color = 'secondary'
                elif(3 <= delta.days <= 2):
                    color = 'danger'
                elif(8 <= delta.days <= 15):
                    color = 'warning'
                elif(16 <= delta.days):
                    color = 'success'
                i.date_color = color
                listData = eval(i.event_highlight)[0].split(',')
                for j in listData:
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    print('highlight_Obj.highlight_name >>>> ',highlight_Obj.highlight_name)
                    highlightStr.append(highlight_Obj.highlight_name) 
                i.highlightStr = highlightStr
                highlightStr = []
            highlightObj = event_highlight_Master.objects.all()
            from datetime import date,timedelta
            today = date.today()
            anniversaryObj = event_bday_annivarsary_management.objects.filter(event_year = today.year,event_type = 'Anniversary').order_by('event_date')
            highlightStr = []
            for i in culturalObj:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                if(delta.days <= 0):
                    color = 'secondary'
                elif(3 <= delta.days <= 2):
                    color = 'danger'
                elif(8 <= delta.days <= 15):
                    color = 'warning'
                elif(16 <= delta.days):
                    color = 'success'
                i.date_color = color
                listData = eval(i.event_highlight)[0].split(',')
                for j in listData:
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    print('highlight_Obj.highlight_name >>>> ',highlight_Obj.highlight_name)
                    highlightStr.append(highlight_Obj.highlight_name) 
                i.highlightStr = highlightStr
                highlightStr = []              
            # =====================================================================
            return render(request,'admin/events/user-event-list.html',{'birthdayObj_today':birthdayObj_today,'birthdayObj_month':birthdayObj_month,'culturalObj':culturalObj,'anniversaryObj':anniversaryObj})
# ##########################################################################################################
@login_required(login_url='/')
def wishes_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            wishObj = event_wishes.objects.filter(senderFK=request.user).order_by('-created_at')
            return render(request,'admin/events/wishes.html',{'wishObj':wishObj})
        if(request.session['userType'] == 'teacheR'):
            empObj = employeeDetails.objects.get(userFK=request.user)
            wishObj = event_wishes.objects.filter(receiverFK=empObj,wish_status='sent').order_by('-created_at')
            wishEnd_Obj = event_wishes.objects.filter(senderFK=request.user,wish_status='sent').order_by('-created_at') | event_wishes.objects.filter(senderFK=request.user,wish_status='scheduled').order_by('-created_at')
            return render(request,'admin/events/user-wishes-list.html',{'wishObj':wishObj,'wishEnd_Obj':wishEnd_Obj})
        if(request.session['userType'] == 'studdenT'):
            empObj = employeeDetails.objects.get(userFK=request.user)
            wishObj = event_wishes.objects.filter(receiverFK=empObj,wish_status='sent').order_by('-created_at')
            wishEnd_Obj = event_wishes.objects.filter(senderFK=request.user,wish_status='sent').order_by('-created_at') | event_wishes.objects.filter(senderFK=request.user,wish_status='scheduled').order_by('-created_at')
            return render(request,'admin/events/user-wishes-list.html',{'wishObj':wishObj,'wishEnd_Obj':wishEnd_Obj})
# ##########################################################################################################
@login_required(login_url='/')
def archieves_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            from datetime import date,timedelta
            today = date.today()
            eventObj = event_bday_annivarsary_management.objects.filter(event_date__lt=today,event_year = today.year).order_by('event_date')
            highlightStr = ''
            for i in eventObj:
                try:
                    for j in eval(i.event_highlight):
                        highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                        highlightStr = highlightStr + highlight_Obj.highlight_name + ','               
                    i.highlightStr = highlightStr
                    highlightStr = ''
                except:
                    listData = eval(i.event_highlight)[0].split(',')
                    for j in listData:
                        highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                        highlightStr = highlightStr + highlight_Obj.highlight_name + ','               
                    i.highlightStr = highlightStr
                    highlightStr = ''
            return render(request,'admin/events/events-archive.html',{'eventObj':eventObj})
        if(request.session['userType'] == 'teacheR'):
            return render(request,'unauthorizedAccess.html')
        if(request.session['userType'] == 'studdenT'):
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def anniversary(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            cultural_eventObj = culturalEvent_Master.objects.all()
            empObj = employeeDetails.objects.all()
            highlightObj = event_highlight_Master.objects.all()
            from datetime import date,timedelta
            today = date.today()
            anniversaryObj_today = event_bday_annivarsary_management.objects.filter(event_date__month = today.month,event_date__day = today.day,event_year = today.year,event_type = 'Anniversary')
            highlightStr = ''
            for i in anniversaryObj_today:
                for j in eval(i.event_highlight):
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr = highlightStr + highlight_Obj.highlight_name + ','                
                i.highlightStr = highlightStr
                i.first_name = i.employeeFK.employee_name.split(' ')[0]
                highlightStr = ''
            date_today = date.today()
            startdate = date_today + timedelta(days=1)
            enddate = date_today + timedelta(days=30)
            anniversaryObj_month = event_bday_annivarsary_management.objects.filter(event_date__range=[startdate, enddate],event_year = today.year,event_type = 'Anniversary').order_by('event_date')            
            # =====================================================================
            # ==================  check date and add color   ======================
            highlightStr = ''
            for i in anniversaryObj_month:
                i.first_name = i.employeeFK.employee_name.split(' ')[0]
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                if(delta.days <= 2):
                    color = 'danger'
                elif(3 <= delta.days <= 7):
                    color = 'success'
                elif(8 <= delta.days <= 15):
                    color = 'info'
                elif(16 <= delta.days):
                    color = 'warning'
                i.date_color = color

                for j in eval(i.event_highlight):
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr = highlightStr + highlight_Obj.highlight_name + ','               
                i.highlightStr = highlightStr
                highlightStr = ''
            # =====================================================================
            startdate = date_today + timedelta(days=31)
            enddate = date(date.today().year, 12, 31)
            anniversaryObj_remain = event_bday_annivarsary_management.objects.filter(event_year = today.year,event_type = 'Anniversary').order_by('event_date')
            # =====================================================================
            # ==================  check date and add color   ======================
            for i in anniversaryObj_remain:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""

                if(delta.days <= 0):
                    color = 'secondary'
                elif(delta.days <= 15):
                    color = 'danger'
                elif(16 <= delta.days <= 25):
                    color = 'success'
                elif(26 <= delta.days <= 35):
                    color = 'info'
                elif(36 <= delta.days):
                    color = 'warning'
                i.Color = color

            return render(request,'admin/events/anniversary.html',{'cultural_eventObj':cultural_eventObj,'empObj':empObj,'highlightObj':highlightObj,'anniversaryObj_today':anniversaryObj_today,'anniversaryObj_month':anniversaryObj_month,'anniversaryObj_remain':anniversaryObj_remain})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################

@login_required(login_url='/')
def check_existing_anniversary(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            from datetime import date,datetime
            today = date.today()
            try:
                empObj = employeeDetails.objects.get(id=int(id))
                anniversaryObj_today = event_bday_annivarsary_management.objects.filter(employeeFK = empObj,event_year = today.year,event_status='created',event_type = 'Anniversary')
                dataArray = []
                if(len(anniversaryObj_today) > 0):
                    context = {}
                    context['date'] = datetime.strptime(str(empObj.joiningDate), '%Y-%m-%d').strftime('%d/%m/%Y')
                    context['highlight'] = eval(anniversaryObj_today[0].event_highlight)
                    context['message'] = 'exist'
                    dataArray.append(context)
                else:
                    context = {}
                    context['date'] = datetime.strptime(str(empObj.joiningDate), '%Y-%m-%d').strftime('%d/%m/%Y')
                    context['message'] = 'new'
                    dataArray.append(context)
                return JsonResponse({'response':dataArray})
            except:
                empObj = employeeDetails.objects.get(id=int(id))
                dataArray = []
                context = {}
                context['date'] = datetime.strptime(str(empObj.joiningDate), '%Y-%m-%d').strftime('%d/%m/%Y')
                context['message'] = 'new'
                dataArray.append(context)
                return JsonResponse({'response':dataArray})
        else:
            return render(request,'unauthorizedAccess.html')


# ##############################################################################################################


@login_required(login_url='/')
def add_anniversary(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            anniversary_highlights = request.POST.getlist('anniversary_highlights[]')
            message = 'created'
            from datetime import date,datetime
            today = date.today()
            try:
                empObj = employeeDetails.objects.get(id=int(id))
                anniversaryObj = event_bday_annivarsary_management.objects.get(employeeFK = empObj,event_year = today.year,event_status='created',event_type = 'Anniversary')
                anniversaryObj.event_highlight = anniversary_highlights
                data = str(empObj.joiningDate).split('-')
                eventDate = f"{today.year}-{data[1]}-{data[2]}"
                date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                anniversaryObj.event_date = date_time_obj
                anniversaryObj.save()
                message = 'updated'
                return JsonResponse({'response':message})
            except:
                try:
                    empObj = employeeDetails.objects.get(id=int(id))
                    data = str(empObj.joiningDate).split('-')
                    eventDate = f"{today.year}-{data[1]}-{data[2]}"
                    date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                    anniversaryObj = event_bday_annivarsary_management(employeeFK = empObj,event_date=date_time_obj,event_highlight = anniversary_highlights,event_year = today.year,event_status='created',event_type = 'Anniversary')
                    anniversaryObj.save()
                    return JsonResponse({'response':message})
                except:
                    return JsonResponse({'response':'fail'})
        else:
            return render(request,'unauthorizedAccess.html')
# ##############################################################################################################

@login_required(login_url='/')
def send_wish_anniversary(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')


            message_success = 'success'
            # try:
            receiverObj = employeeDetails.objects.get(id=int(receiver))
            eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type='Anniversary')
            wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
            if(len(wishObj) == 0):
                send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                senderFK = request.user,
                                                                receiverFK = receiverObj,
                                                                message_title = title,
                                                                message = send_message,
                                                                creative = creative_data)
                send_bday_anniversary_messageObj.save()
                # ######################################################################################################################
                # new notification for sending anniversary wishes
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=receiverObj.userFK,notification_from=request.user,
                                                            notification_subject=f'{title}',
                                                            notification_message=f'{send_message}'
                                                            )
                notification_obj.save()
                # ######################################################################################################################
            elif(len(wishObj) == 1):
                wishObj[0].message_title = title
                wishObj[0].message = send_message
                wishObj[0].creative = creative_data
                wishObj[0].save()
            # except:
            #     message_success = 'fail'

            return JsonResponse({'response':message_success})
        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type=eventType)

                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
                if(len(wishObj) == 0):
                    send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data)
                    send_bday_anniversary_messageObj.save()
                    # ######################################################################################################################
                    # new notification for sending happy birthday wishes
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=receiverObj,notification_from=request.user,
                                                                notification_subject=f'{title}',
                                                                notification_message=f'{send_message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})
# ###############################################################################################################

@login_required(login_url='/')
def schedule_wish_anniversary(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type='Anniversary')
                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    if(creative_data == None):
                        send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = eventObj.event_date,
                                                                        wish_status = 'scheduled')
                        send_bday_anniversary_messageObj.save()
                    else:
                        send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        creative = creative_data,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = eventObj.event_date,
                                                                        wish_status = 'scheduled')
                        send_bday_anniversary_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    if(creative_data != None):
                        wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})

        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022')
                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data,
                                                                    wish_type = 'scheduled',
                                                                    wish_schedule_time = eventObj.event_date,
                                                                    wish_status = 'scheduled')
                    send_bday_anniversary_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'

            return JsonResponse({'response':message_success})
# ######################################################################################################################
@login_required(login_url='/')
def birthday(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            cultural_eventObj = culturalEvent_Master.objects.all()
            empObj = employeeDetails.objects.all()
            highlightObj = event_highlight_Master.objects.all()
            from datetime import date,timedelta
            today = date.today()
            birthdayObj_today = event_bday_annivarsary_management.objects.filter(event_date__month = today.month,event_date__day = today.day,event_year = today.year,event_type = 'Birthday')
            highlightStr = ''
            for i in birthdayObj_today:
                for j in eval(i.event_highlight):
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr = highlightStr + highlight_Obj.highlight_name + ','                
                i.highlightStr = highlightStr
                i.first_name = i.employeeFK.employee_name.split(' ')[0]
                highlightStr = ''
            date_today = date.today()
            startdate = date_today + timedelta(days=1)
            enddate = date_today + timedelta(days=30)
            birthdayObj_month = event_bday_annivarsary_management.objects.filter(event_date__range=[startdate, enddate],event_year = today.year,event_type = 'Birthday').order_by('event_date')            
            # =====================================================================
            # ==================  check date and add color   ======================
            highlightStr = ''
            for i in birthdayObj_month:
                i.first_name = i.employeeFK.employee_name.split(' ')[0]
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                if(delta.days <= 2):
                    color = 'danger'
                elif(3 <= delta.days <= 7):
                    color = 'success'
                elif(8 <= delta.days <= 15):
                    color = 'info'
                elif(16 <= delta.days):
                    color = 'warning'
                i.date_color = color

                for j in eval(i.event_highlight):
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr = highlightStr + highlight_Obj.highlight_name + ','               
                i.highlightStr = highlightStr
                highlightStr = ''
            # =====================================================================
            startdate = date_today + timedelta(days=31)
            enddate = date(date.today().year, 12, 31)
            birthdayObj_remain = event_bday_annivarsary_management.objects.filter(event_year = today.year,event_type = 'Birthday').order_by('event_date')
            # =====================================================================
            # ==================  check date and add color   ======================
            for i in birthdayObj_remain:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""

                if(delta.days <= 0):
                    color = 'secondary'
                elif(delta.days <= 15):
                    color = 'danger'
                elif(16 <= delta.days <= 25):
                    color = 'success'
                elif(26 <= delta.days <= 35):
                    color = 'info'
                elif(36 <= delta.days):
                    color = 'warning'
                i.Color = color
            # =====================================================================
            return render(request,'admin/events/birthday.html',{'cultural_eventObj':cultural_eventObj,'empObj':empObj,'highlightObj':highlightObj,'birthdayObj_today':birthdayObj_today,'birthdayObj_month':birthdayObj_month,'birthdayObj_remain':birthdayObj_remain})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def cultural_events(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            cultural_eventObj = culturalEvent_Master.objects.all()
            empObj = employeeDetails.objects.all()
            highlightObj = event_highlight_Master.objects.all()
            from datetime import date,timedelta
            today = date.today()
            culturalObj_today = event_bday_annivarsary_management.objects.filter(event_date__month = today.month,event_date__day = today.day,event_year = today.year,event_type = 'CulturalEvent')
            highlightStr = []
            for i in culturalObj_today:
                listData = eval(i.event_highlight)[0].split(',')
                for j in listData:
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr.append(highlight_Obj.highlight_name)                
                i.highlightStr = highlightStr
                highlightStr = []
            date_today = date.today()
            startdate = date_today + timedelta(days=1)
            enddate = date_today + timedelta(days=30)
            culturalObj_month = event_bday_annivarsary_management.objects.filter(event_date__range=[startdate, enddate],event_year = today.year,event_type = 'CulturalEvent').order_by('event_date')            
            # =====================================================================
            # ==================  check date and add color   ======================
            highlightStr = []
            for i in culturalObj_month:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                if(delta.days <= 2):
                    color = 'danger'
                elif(3 <= delta.days <= 7):
                    color = 'success'
                elif(8 <= delta.days <= 15):
                    color = 'info'
                elif(16 <= delta.days):
                    color = 'warning'
                i.date_color = color

                listData = eval(i.event_highlight)[0].split(',')
                for j in listData:
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr.append(highlight_Obj.highlight_name) 
                i.highlightStr = highlightStr
                highlightStr = []
            # =====================================================================
            startdate = date_today + timedelta(days=31)
            enddate = date(date.today().year, 12, 31)
            culturalObj_remain = event_bday_annivarsary_management.objects.filter(event_year = today.year,event_type = 'CulturalEvent').order_by('event_date')
            # =====================================================================
            # ==================  check date and add color   ======================
            for i in culturalObj_remain:
                d1 = date(i.event_date.year,i.event_date.month,i.event_date.day)
                d0 = date(today.year,today.month,today.day)
                delta = d1 - d0
                color = ""
                highlightStr = []     
                if(delta.days <= 0):
                    color = 'secondary'
                elif(delta.days <= 15):
                    color = 'danger'
                elif(16 <= delta.days <= 25):
                    color = 'success'
                elif(26 <= delta.days <= 35):
                    color = 'info'
                elif(36 <= delta.days):
                    color = 'warning'
                i.Color = color

                listData = eval(i.event_highlight)[0].split(',')
                for j in listData:
                    highlight_Obj = event_highlight_Master.objects.get(id=int(j))
                    highlightStr.append(highlight_Obj.highlight_name) 
                i.highlightStr = highlightStr
                highlightStr = []     
            # =====================================================================
            return render(request,'admin/events/cultural-event.html',{'cultural_eventObj':cultural_eventObj,'empObj':empObj,'highlightObj':highlightObj,'culturalObj_today':culturalObj_today,'culturalObj_month':culturalObj_month,'culturalObj_remain':culturalObj_remain})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def check_existing_birthday(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            from datetime import date,datetime
            today = date.today()
            try:
                empObj = employeeDetails.objects.get(id=int(id))
                birthdayObj_today = event_bday_annivarsary_management.objects.filter(employeeFK = empObj,event_year = today.year,event_status='created',event_type = 'Birthday')
                dataArray = []
                if(len(birthdayObj_today) > 0):
                    context = {}
                    context['date'] = datetime.strptime(str(empObj.DOB), '%Y-%m-%d').strftime('%d/%m/%Y')
                    context['highlight'] = eval(birthdayObj_today[0].event_highlight)
                    context['message'] = 'exist'
                    dataArray.append(context)
                else:
                    context = {}
                    context['date'] = datetime.strptime(str(empObj.DOB), '%Y-%m-%d').strftime('%d/%m/%Y')
                    context['message'] = 'new'
                    dataArray.append(context)
                return JsonResponse({'response':dataArray})
            except:
                empObj = employeeDetails.objects.get(id=int(id))
                dataArray = []
                context = {}
                context['date'] = datetime.strptime(str(empObj.DOB), '%Y-%m-%d').strftime('%d/%m/%Y')
                context['message'] = 'new'
                dataArray.append(context)
                return JsonResponse({'response':dataArray})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def add_birthday(request,id):
    
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            bday_highlights = request.POST.getlist('bday_highlights[]')
            message = 'created'
            from datetime import date,datetime
            today = date.today()
            try:
                empObj = employeeDetails.objects.get(id=int(id))
                birthdayObj = event_bday_annivarsary_management.objects.get(employeeFK = empObj,event_year = today.year,event_status='created',event_type = 'Birthday')
                birthdayObj.event_highlight = bday_highlights
                data = str(empObj.DOB).split('-')
                eventDate = f"{today.year}-{data[1]}-{data[2]}"
                date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                birthdayObj.event_date = date_time_obj
                birthdayObj.save()
                message = 'updated'
                return JsonResponse({'response':message})
            except:
                try:
                    empObj = employeeDetails.objects.get(id=int(id))
                    data = str(empObj.DOB).split('-')
                    eventDate = f"{today.year}-{data[1]}-{data[2]}"
                    date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                    birthdayObj = event_bday_annivarsary_management(employeeFK = empObj,event_date=date_time_obj,event_highlight = bday_highlights,event_year = today.year,event_status='created',event_type = 'Birthday')
                    birthdayObj.save()
                    return JsonResponse({'response':message})
                except:
                    return JsonResponse({'response':'fail'})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def send_wish(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')


            message_success = 'success'
            # try:
            receiverObj = employeeDetails.objects.get(id=int(receiver))
            eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type='Birthday')
            wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
            if(len(wishObj) == 0):
                send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                senderFK = request.user,
                                                                receiverFK = receiverObj,
                                                                message_title = title,
                                                                message = send_message,
                                                                creative = creative_data)
                send_bday_anniversary_messageObj.save()
                # ######################################################################################################################
                # new notification for sending happy birthday wishes
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=receiverObj.userFK,notification_from=request.user,
                                                            notification_subject=f'{title}',
                                                            notification_message=f'{send_message}'
                                                            )
                notification_obj.save()
                # ######################################################################################################################
            elif(len(wishObj) == 1):
                wishObj[0].message_title = title
                wishObj[0].message = send_message
                wishObj[0].creative = creative_data
                wishObj[0].save()
            # except:
            #     message_success = 'fail'

            return JsonResponse({'response':message_success})
        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type=eventType)

                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
                if(len(wishObj) == 0):
                    send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data)
                    send_bday_anniversary_messageObj.save()
                    # ######################################################################################################################
                    # new notification for sending happy birthday wishes
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=receiverObj,notification_from=request.user,
                                                                notification_subject=f'{title}',
                                                                notification_message=f'{send_message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})
# ##########################################################################################################
@login_required(login_url='/')
def schedule_wish(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022',event_type='Birthday')
                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    if(creative_data == None):
                        send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = eventObj.event_date,
                                                                        wish_status = 'scheduled')
                        send_bday_anniversary_messageObj.save()
                    else:
                        send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        creative = creative_data,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = eventObj.event_date,
                                                                        wish_status = 'scheduled')
                        send_bday_anniversary_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    if(creative_data != None):
                        wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})

        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = employeeDetails.objects.get(id=int(receiver))
                eventObj = event_bday_annivarsary_management.objects.get(employeeFK=receiverObj,event_year='2022')
                wishObj = event_wishes.objects.filter(eventFK=eventObj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    send_bday_anniversary_messageObj = event_wishes(eventFK = eventObj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data,
                                                                    wish_type = 'scheduled',
                                                                    wish_schedule_time = eventObj.event_date,
                                                                    wish_status = 'scheduled')
                    send_bday_anniversary_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'

            return JsonResponse({'response':message_success})
# ##########################################################################################################
@login_required(login_url='/')
def check_existing_cultural_event(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            from datetime import date,datetime
            today = date.today()
            try:
                eventObj = culturalEvent_Master.objects.get(id=int(id))
                cultutal_event_obj = event_bday_annivarsary_management.objects.filter(cultural_eventFK = eventObj,event_year = today.year,event_status='created',event_type = 'CulturalEvent')
                dataArray = []
                if(len(cultutal_event_obj) > 0):
                    context = {}
                    context['date'] = datetime.strptime(str(cultutal_event_obj[0].event_date), '%Y-%m-%d').strftime('%d/%m/%Y')
                    context['highlight'] = eval(cultutal_event_obj[0].event_highlight)
                    context['message'] = 'exist'
                    dataArray.append(context)
                else:
                    context = {}
                    context['message'] = 'new'
                    dataArray.append(context)
                return JsonResponse({'response':dataArray})
            except:
                eventObj = culturalEvent_Master.objects.get(id=int(id))
                dataArray = []
                context = {}
                context['message'] = 'new'
                dataArray.append(context)
                return JsonResponse({'response':dataArray})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
@login_required(login_url='/')
def get_wish_data(request,id):
    if request.method == 'GET':
        dataArray = {}
        try:
            wishObj = event_wishes.objects.get(id=int(id))
            dataArray = {
                'sender' : wishObj.senderFK.first_name,
                'receiver' : wishObj.receiverFK.employee_name,
                'receiverID' : wishObj.receiverFK.id,
                'receiver_image' : str(wishObj.receiverFK.profile_image),
                'title' : wishObj.message_title,
                'message' : wishObj.message,
                'creative' : "/media/"+str(wishObj.creative),
                'event' : wishObj.eventFK.event_type
            }
            import datetime
            if(wishObj.wish_schedule_time == None):
                date = str(wishObj.created_at).split(' ')[0]
                dataArray['date'] = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d %b,%Y')
            else:
                dataArray['date'] = datetime.datetime.strptime(str(wishObj.wish_schedule_time), '%Y-%m-%d').strftime('%d %b,%Y')
        except:
            dataArray = {}

        return JsonResponse({'response':dataArray})
# ##########################################################################################################
@login_required(login_url='/')
def add_cultural_event(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            eventTitle = request.POST['eventTitle']
            eventDate = request.POST['eventDate']
            eventManagerID = request.POST['eventManagerID']
            eventBudget = request.POST['eventBudget']
            eventHighlight = request.POST.getlist('eventHighlight[]')
            performanceDetail = request.POST['performanceDetail']
            event_creative = request.FILES.get('event_creative')
            message = 'created'
            from datetime import date,datetime
            today = date.today()
            try:
                cEventObj = culturalEvent_Master.objects.get(id=int(id))
                cultural_event_obj = event_bday_annivarsary_management.objects.get(cultural_eventFK = cEventObj,event_year = today.year,event_status='created',event_type = 'CulturalEvent')
                cultural_event_obj.event_highlight = eventHighlight
                data = str(eventDate).split('-')
                eventDate = f"{today.year}-{data[0]}-{data[1]}"
                date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                cultural_event_obj.event_date = date_time_obj
                cultural_event_obj.cultural_event_title = eventTitle
                empObj = employeeDetails.objects.get(id=int(eventManagerID))
                cultural_event_obj.cultural_event_manager = empObj
                cultural_event_obj.special_performance = performanceDetail
                cultural_event_obj.cultural_event_creative = event_creative
                cultural_event_obj.event_budget = eventBudget
                cultural_event_obj.save()
                message = 'updated'
                return JsonResponse({'response':message})
            except:
                try:
                    cEventObj = culturalEvent_Master.objects.get(id=int(id))
                    empObj = employeeDetails.objects.get(id=int(eventManagerID))
                    data = str(eventDate).split('/')
                    eventDate = f"{today.year}-{data[0]}-{data[1]}"
                    date_time_obj = datetime.strptime(eventDate, '%Y-%m-%d')
                    cultural_event_obj = event_bday_annivarsary_management(cultural_eventFK = cEventObj,event_date=date_time_obj,event_highlight = eventHighlight,cultural_event_title = eventTitle,event_year = today.year,event_status='created',event_type = 'CulturalEvent',cultural_event_manager = empObj,special_performance = performanceDetail,cultural_event_creative = event_creative,event_budget = eventBudget)
                    cultural_event_obj.save()

                    # ######################################################################################################################
                    # new cultural wishes
                    # ######################################################################################################################
                    userObj = User.objects.filter(is_superuser=False,is_staff=True) | User.objects.filter(is_superuser=False,is_active=True)
                    for i in userObj:
                        notification_obj = Notification_Management(notification_to=i,notification_from=request.user,
                                                                    notification_subject=f'{cEventObj.event_name} cultural evenet added for the date : {eventDate}',
                                                                    notification_message=f'{eventTitle}, all employess presence will be appreciated.Lets come and celebrate this auspecious day together.'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################
                    return JsonResponse({'response':message})
                except:
                    return JsonResponse({'response':'fail'})
        else:
            return render(request,'unauthorizedAccess.html')
# ##########################################################################################################

@login_required(login_url='/')
def send_wish_culturalevent(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')


            message_success = 'success'
            # try:
            receiverObj = culturalEvent_Master.objects.get(id=int(receiver))
            cultural_event_obj  = event_bday_annivarsary_management.objects.get(cultural_eventFK=receiverObj,event_year='2022',event_type='CulturalEvent')
            wishObj = event_wishes.objects.filter(eventFK=cultural_event_obj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
            if(len(wishObj) == 0):
                send_cultural_event_messageObj = event_wishes(eventFK = cultural_event_obj,
                                                                senderFK = request.user,
                                                                receiverFK = receiverObj,
                                                                message_title = title,
                                                                message = send_message,
                                                                creative = creative_data)
                send_cultural_event_messageObj.save()
                # ######################################################################################################################
                # new notification for sending cultural event wishes
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=receiverObj.userFK,notification_from=request.user,
                                                            notification_subject=f'{title}',
                                                            notification_message=f'{send_message}'
                                                            )
                notification_obj.save()
                # ######################################################################################################################
            elif(len(wishObj) == 1):
                wishObj[0].message_title = title
                wishObj[0].message = send_message
                wishObj[0].creative = creative_data
                wishObj[0].save()
            # except:
            #     message_success = 'fail'

            return JsonResponse({'response':message_success})
        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = culturalEvent_Master.objects.get(id=int(receiver))
                cultural_event_obj = event_bday_annivarsary_management.objects.get(cultural_eventFK=receiverObj,event_year='2022',event_type=eventType)

                wishObj = event_wishes.objects.filter(eventFK=cultural_event_obj,senderFK = request.user,receiverFK = receiverObj,wish_status='sent')
                if(len(wishObj) == 0):
                    send_cultural_event_messageObj = event_wishes(eventFK = cultural_event_obj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data)
                    send_cultural_event_messageObj.save()
                    # ######################################################################################################################
                    # new notification for sending cultural wishes
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=receiverObj,notification_from=request.user,
                                                                notification_subject=f'{title}',
                                                                notification_message=f'{send_message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})
# ###############################################################################################################

@login_required(login_url='/')
def schedule_wish_culturalevent(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            message_success = 'success'
            try:
                receiverObj = culturalEvent_Master.objects.get(id=int(receiver))
                cultural_event_obj = event_bday_annivarsary_management.objects.get(cultural_eventFK=receiverObj,event_year='2022',event_type='CulturalEvent')
                wishObj = event_wishes.objects.filter(eventFK=cultural_event_obj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    if(creative_data == None):
                        send_cultural_event_messageObj = event_wishes(eventFK = cultural_event_obj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = cultural_event_obj.event_date,
                                                                        wish_status = 'scheduled')
                        send_cultural_event_messageObj.save()
                    else:
                        send_cultural_event_messageObj = event_wishes(eventFK = cultural_event_obj,
                                                                        senderFK = request.user,
                                                                        receiverFK = receiverObj,
                                                                        message_title = title,
                                                                        message = send_message,
                                                                        creative = creative_data,
                                                                        wish_type = 'scheduled',
                                                                        wish_schedule_time = cultural_event_obj.event_date,
                                                                        wish_status = 'scheduled')
                        send_cultural_event_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    if(creative_data != None):
                        wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'
            return JsonResponse({'response':message_success})

        else:
            receiver =  request.POST.get('receiverID')
            title =  request.POST.get('title')
            send_message =  request.POST.get('message')
            creative_data =  request.FILES.get('creative')
            eventType = request.POST.get('eventType')
            message_success = 'success'
            try:
                receiverObj = culturalEvent_Master.objects.get(id=int(receiver))
                cultural_event_obj = event_bday_annivarsary_management.objects.get(cultural_eventFK=receiverObj,event_year='2022')
                wishObj = event_wishes.objects.filter(eventFK=cultural_event_obj,senderFK = request.user,receiverFK = receiverObj,wish_status='scheduled')
                if(len(wishObj) == 0):
                    send_cultural_event_messageObj = event_wishes(eventFK = cultural_event_obj,
                                                                    senderFK = request.user,
                                                                    receiverFK = receiverObj,
                                                                    message_title = title,
                                                                    message = send_message,
                                                                    creative = creative_data,
                                                                    wish_type = 'scheduled',
                                                                    wish_schedule_time = cultural_event_obj.event_date,
                                                                    wish_status = 'scheduled')
                    send_cultural_event_messageObj.save()
                elif(len(wishObj) == 1):
                    wishObj[0].message_title = title
                    wishObj[0].message = send_message
                    wishObj[0].creative = creative_data
                    wishObj[0].save()
            except:
                message_success = 'fail'

            return JsonResponse({'response':message_success})
# ################################################################################################################