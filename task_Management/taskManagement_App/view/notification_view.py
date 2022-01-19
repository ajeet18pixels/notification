from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models.employee_model import employeeDetails
from ..models.master_models import *
from ..models.notification_model import *
from datetime import date
import datetime
from django.core.paginator import Paginator

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def notification(request):
    if request.method == 'GET':
        notificationObj = {}
        emp_Obj = employeeDetails.objects.all().order_by('-id')

        if(request.session['userType'] == 'masteR'):
            notificationObj = Notification_Management.objects.filter(admin_trash_status = False).order_by('-id')[:15]
            total = Notification_Management.objects.all().order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id')[:15]
            trash = Notification_Management.objects.filter(admin_trash_status = True).order_by('-id')[:15] 
            starred = Notification_Management.objects.filter(admin_starred_status = True).order_by('-id')[:15]

            return render(request,'admin/notification/notifications.html',{'notificationObj':notificationObj,'datalength':len(Notification_Management.objects.all()),'emp_Obj':emp_Obj,'total':total,'sent':sent[:15],'trash':trash[:15],'starred':starred[:15]})

        if(request.session['userType'] == 'teacheR'):
            notificationObj = Notification_Management.objects.filter(notification_to = request.user,manager_trash_status = False).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_trash_status = False).order_by('-id')
            total = Notification_Management.objects.filter(notification_to = request.user).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user).order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id')[:15]  
            trash = Notification_Management.objects.filter(notification_to = request.user,manager_trash_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_trash_status = True).order_by('-id')  
            starred = Notification_Management.objects.filter(notification_to = request.user,manager_starred_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_starred_status = True).order_by('-id')
            return render(request,'admin/notification/notifications.html',{'notificationObj':notificationObj[:15],'emp_Obj':emp_Obj,'total':total,'sent':sent,'trash':trash[:15],'starred':starred[:15]})
            
        if(request.session['userType'] == 'studdenT'):
            notificationObj = Notification_Management.objects.filter(notification_to = request.user,emp_trash_status = False).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_trash_status = False).order_by('-id')
            total = Notification_Management.objects.filter(notification_to = request.user).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user).order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id')  
            trash = Notification_Management.objects.filter(notification_to = request.user,manager_trash_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_trash_status = True).order_by('-id')  
            starred = Notification_Management.objects.filter(notification_to = request.user,manager_starred_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_starred_status = True).order_by('-id')

            return render(request,'admin/notification/notifications.html',{'notificationObj':notificationObj[:15],'emp_Obj':emp_Obj,'total':total,'sent':sent[:15],'trash':trash[:15],'starred':starred[:15]})

    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            employee_All = request.POST.get('employee_all')
            employee_List = request.POST.getlist('employee_list[]')
            mail_Subject = request.POST.get('mailSubject')
            mail_Message = request.POST.get('mailMessage')

            print('employee_all >>>> ',employee_All)
            print('employee_list >>>> ',employee_List)
            print('mailSubject >>>> ',mail_Subject)
            print('mailMessage >>>> ',mail_Message)

            message = 'success'
            # ----------------------------------------------------------------------
            try:

                if(len(employee_List) == 1):
                    # 'single'
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(employee_List[0])).userFK,notification_from=request.user,
                                                                notification_subject=f'{mail_Subject}',
                                                                notification_message=f'{mail_Message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                    
                if(employee_All == 'All'):
                    # ######################################################################################################################
                    userObj = User.objects.filter(is_superuser=False,is_active=True)
                    for i in userObj:
                        notification_obj = Notification_Management(notification_to=i,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################

                if(len(employee_List) > 1):
                    # ######################################################################################################################
                    for i in employee_List:
                        notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(i)).userFK,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################


            except:
                message = 'fail'
            # ----------------------------------------------------------------------
            # ----------------------------------------------------------------------
            return JsonResponse({'response':message})
        

        if(request.session['userType'] == 'teacheR'):
             # notificationObj = Notification_Management.objects.all()
            employee_All = request.POST.get('employee_all')
            employee_List = request.POST.getlist('employee_list[]')
            mail_Subject = request.POST.get('mailSubject')
            mail_Message = request.POST.get('mailMessage')

            print('employee_all >>>> ',employee_All)
            print('employee_list >>>> ',employee_List)
            print('mailSubject >>>> ',mail_Subject)
            print('mailMessage >>>> ',mail_Message)

            message = 'success'
            # ----------------------------------------------------------------------
            try:

                if(len(employee_List) == 1):
                    # 'single'
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(employee_List[0])).userFK,notification_from=request.user,
                                                                notification_subject=f'{mail_Subject}',
                                                                notification_message=f'{mail_Message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                    
                if(employee_All == 'All'):
                    # ######################################################################################################################
                    userObj = User.objects.filter(is_superuser=False,is_active=True)
                    for i in userObj:
                        notification_obj = Notification_Management(notification_to=i,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################

                if(len(employee_List) > 1):
                    # ######################################################################################################################
                    for i in employee_List:
                        notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(i)).userFK,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################


            except:
                message = 'fail'
            # ----------------------------------------------------------------------
            # ----------------------------------------------------------------------
            return JsonResponse({'response':message})

            
        if(request.session['userType'] == 'studdenT'):
            # notificationObj = Notification_Management.objects.all()
            employee_All = request.POST.get('employee_all')
            employee_List = request.POST.getlist('employee_list[]')
            mail_Subject = request.POST.get('mailSubject')
            mail_Message = request.POST.get('mailMessage')

            print('employee_all >>>> ',employee_All)
            print('employee_list >>>> ',employee_List)
            print('mailSubject >>>> ',mail_Subject)
            print('mailMessage >>>> ',mail_Message)

            message = 'success'
            # ----------------------------------------------------------------------
            try:

                if(len(employee_List) == 1):
                    # 'single'
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(employee_List[0])).userFK,notification_from=request.user,
                                                                notification_subject=f'{mail_Subject}',
                                                                notification_message=f'{mail_Message}'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                    
                if(employee_All == 'All'):
                    # ######################################################################################################################
                    userObj = User.objects.filter(is_superuser=False,is_active=True)
                    for i in userObj:
                        notification_obj = Notification_Management(notification_to=i,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################

                if(len(employee_List) > 1):
                    # ######################################################################################################################
                    for i in employee_List:
                        notification_obj = Notification_Management(notification_to=employeeDetails.objects.get(id=int(i)).userFK,notification_from=request.user,
                                                                    notification_subject=f'{mail_Subject}',
                                                                    notification_message=f'{mail_Message}'
                                                                    )
                        notification_obj.save()
                    # ######################################################################################################################


            except:
                message = 'fail'
            # ----------------------------------------------------------------------
            # ----------------------------------------------------------------------
            return JsonResponse({'response':message})


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def delete_notification(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.delete()
            return redirect('notification')
        

        if(request.session['userType'] == 'teacheR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.notification_delete_status = True
            notificationObj.save()
            return redirect('notification')
            
        if(request.session['userType'] == 'studdenT'):
            return render(request,'admin/notification/notification.html',{})

    else:
        return redirect('/')


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def read_notification(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.notification_admin_read_status = True
            notificationObj.save()
            return redirect('notification')
        

        if(request.session['userType'] == 'teacheR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.notification_read_status = True
            notificationObj.save()
            return redirect('notification')
            
        if(request.session['userType'] == 'studdenT'):
            return render(request,'admin/notification/notification.html',{})

    else:
        return redirect('/')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def unread_notification(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.notification_admin_read_status = False
            notificationObj.save()
            return redirect('notification')
        

        if(request.session['userType'] == 'teacheR'):
            notificationObj = Notification_Management.objects.get(id=int(id))
            notificationObj.notification_read_status = False
            notificationObj.save()
            return redirect('notification')
            
        if(request.session['userType'] == 'studdenT'):
            return render(request,'admin/notification/notification.html',{})

    else:
        return redirect('/')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def view_notification(request,id):
    if request.method == 'GET':
        notificationObj = Notification_Management.objects.get(id=int(id))
        context = {
            'sender':notificationObj.notification_to.first_name,
            'receiver':notificationObj.notification_from.first_name,
            'title':notificationObj.notification_subject,
            'message':notificationObj.notification_message,
            'created_at':notificationObj.created_at.strftime("%d %b, %Y")
        }
        if(request.session['userType'] == 'masteR'):
            notificationObj.admin_read_status = True
            notificationObj.save()
        if(request.session['userType'] == 'teacheR'):
            notificationObj.manager_read_status = True
            notificationObj.save()
        if(request.session['userType'] == 'studdenT'):
            notificationObj.emp_read_status = True
            notificationObj.save()

        return JsonResponse({'response':context})
    else:
        return redirect('unautorizedaccess')



@login_required(login_url='/')
def move_to_trash(request,id):
    if request.method == 'POST':
        notificationObj = Notification_Management.objects.get(id=int(id))
        message = 'success'
        try:
            if(request.session['userType'] == 'masteR'):
                notificationObj.admin_trash_status = True
                notificationObj.save()
            if(request.session['userType'] == 'teacheR'):
                notificationObj.manager_trash_status = True
                notificationObj.save()
            if(request.session['userType'] == 'studdenT'):
                notificationObj.emp_trash_status = True
                notificationObj.save()
        except:
            message = 'fail'
        return JsonResponse({'response':message})
    else:
        return redirect('unautorizedaccess')


@login_required(login_url='/')
def move_to_starred(request,id):
    if request.method == 'POST':
        notificationObj = Notification_Management.objects.get(id=int(id))
        message = 'success'
        try:
            if(request.session['userType'] == 'masteR'):
                notificationObj.admin_starred_status = True
                notificationObj.save()
            if(request.session['userType'] == 'teacheR'):
                notificationObj.manager_starred_status = True
                notificationObj.save()
            if(request.session['userType'] == 'studdenT'):
                notificationObj.emp_starred_status = True
                notificationObj.save()
        except:
            message = 'fail'
        return JsonResponse({'response':message})
    else:
        return redirect('unautorizedaccess')



@login_required(login_url='/')
def remove_from_starred(request,id):
    if request.method == 'POST':
        notificationObj = Notification_Management.objects.get(id=int(id))
        message = 'success'
        try:
            if(request.session['userType'] == 'masteR'):
                notificationObj.admin_starred_status = False
                notificationObj.save()
            if(request.session['userType'] == 'teacheR'):
                notificationObj.manager_starred_status = False
                notificationObj.save()
            if(request.session['userType'] == 'studdenT'):
                notificationObj.emp_starred_status = False
                notificationObj.save()
        except:
            message = 'fail'
        return JsonResponse({'response':message})
    else:
        return redirect('unautorizedaccess')






# ##################################################################################################################################
# FETCH NOTIFICATIONS BY TYPE
# ##################################################################################################################################
@login_required(login_url='/')
def get_selected_notification(request):
    if request.method == 'GET':
        notType = request.GET['notification_type']
        message = 'success'
        try:

            if(request.session['userType'] == 'masteR'):
                if(notType == 'Sent'):
                    notObj = list(Notification_Management.objects.filter(notification_from=request.user).values())
                    print('notObj >>> ',notObj)






            if(request.session['userType'] == 'teacheR'):
                pass
            if(request.session['userType'] == 'studdenT'):
                pass
        
            return JsonResponse(notObj,safe = False)

        except:
            message = 'fail'
            return JsonResponse({'response':message})
    else:
        return JsonResponse({'response':'fail'})


# ############################################################################################################################
#  Notification pagination
# ############################################################################################################################
@login_required(login_url='/')
def notificationPagination(request):
    if request.session.has_key('auth_token'):
        username = request.session['auth_username']
        roleSearchString = request.GET['search_String']
        page = request.GET['page']


        # print('string : ',roleSearchString,'pgno : ',page)
        # apiSearchStudentDetails = getMethod(
        #         request=request,
        #         method='GET',
        #         task = 'SEARCHROLE',
        #         pathInfo=searchRole_URl+'?q='+str(roleSearchString)+'&page='+str(page).strip(),
        #         )
        # data = json.loads(apiSearchStudentDetails.text)
        # print('search role daa :: ',data)

        return render(request,'admin/notification/notification.html',{})
    else:
        return redirect('/')