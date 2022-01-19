from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from ..models.master_models import designation_Master
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models.employee_model import employeeDetails,employee_Password
from ..models.master_models import qualification_Master,passingYear_Master
from django.contrib.auth.models import User
from ..models.notification_model import *
from ..models.project_model import *
from ..models.events_model import *

from ..models.leave_model import *
from ..models.hr_models import *
from ..models.task_model import Task_Management

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
# ##########################################################################################################
def user_login(request):
    if request.method == 'GET':
        if 'userType' in request.session:
            if(request.session['userType'] == 'masteR'):
                return redirect('admin_dashboard')
            if(request.session['userType'] == 'teacheR'):
                return redirect('admin_dashboard')
            if(request.session['userType'] == 'studdenT'):
                return redirect('admin_dashboard')
        return render(request,'authentication/login.html')

    if request.method == 'POST':
        username = request.POST['emailaddress']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request, user)
                if(user.is_superuser):
                    request.session['userType'] = 'masteR'
                elif(user.is_staff):
                    request.session['userType'] = 'teacheR'
                    empObj = employeeDetails.objects.get(userFK=request.user)
                    request.session['profileImage'] = str(empObj.profile_image)
                elif(user.is_active):
                    request.session['userType'] = 'studdenT'
                    empObj = employeeDetails.objects.get(userFK=request.user)
                    request.session['profileImage'] = str(empObj.profile_image)
                return redirect('admin_dashboard')
        else:
            messages.success(request,'Invalid credentials')
            return redirect('user_login')
# ##########################################################################################################
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list)
# ##########################################################################################################
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list)
# -------------------------------------------------------------------------------------------------------------
@login_required(login_url='/')
def admin_dashboard(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            # ==============================================================================================
            from datetime import date,timedelta
            today = date.today()
            date_today = date.today()
            
            context = {}
            # =================================   admin dashboard   ========================================
            total_project = Project_Management.objects.filter(project_status='Ongoing',project_status_force_update='In Progress') | Project_Management.objects.filter(project_status='Just Created',project_status_force_update='In Progress')
            total_emp = User.objects.filter(is_superuser=False,is_active=True)
            total_upcoming_event = event_bday_annivarsary_management.objects.filter(event_date__range=[date_today + timedelta(days=1), date_today + timedelta(days=30)],event_year = today.year).order_by('event_date')
            total_pending_leave_request = leave_management.objects.filter(leave_approval_status='pending',leave_date_from__range=[date_today, date_today + timedelta(days=10)]).order_by('leave_date_from')
            total_job_applications = job_application.objects.all()
            
            if(len(total_project)>4):
                context['total_project'] = total_project[:4]
            else:
                context['total_project'] = total_project
                
            context['total_project_count'] = Project_Management.objects.all()
            context['total_emp'] = total_emp
            context['total_online_emp'] = get_current_users()
            context['total_upcoming_event'] = total_upcoming_event
            context['total_pending_leave_request'] = total_pending_leave_request
            context['total_job_applications'] = total_job_applications
            # ==============================================================================================
            TaskObj = Task_Management.objects.all().order_by('-id')[:20]

            todo = Task_Management.objects.filter(task_status = 'To do').count()
            doing = Task_Management.objects.filter(task_status = 'Doing').count()
            done = Task_Management.objects.filter(task_status = 'Done').count()
            delay = 0

            for i in TaskObj:
                dueData = str(i.due_date).split('-')
                print('due date >>> ',dueData)
                # ----------------------------------------------------------------------------------
                month = ''
                status = ''
                # ----------------------------------------------------------------------------------
                from datetime import date
                todays_date = date.today()
                print('todays_date.day >>>> ',todays_date.day)

                if(dueData[1] == '1'):
                    month = 'Jan'
                if(dueData[1] == '2'):
                    month = 'Feb'
                if(dueData[1] == '3'):
                    month = 'Mar'
                if(dueData[1] == '4'):
                    month = 'Apr'
                if(dueData[1] == '5'):
                    month = 'May'
                if(dueData[1] == '6'):
                    month = 'Jun'
                if(dueData[1] == '7'):
                    month = 'Jul'
                if(dueData[1] == '8'):
                    month = 'Aug'
                if(dueData[1] == '9'):
                    month = 'Sep'
                if(dueData[1] == '10'):
                    month = 'Oct'
                if(dueData[1] == '11'):
                    month = 'Nov'
                if(dueData[1] == '12'):
                    month = 'Dec'

                import datetime 
                timeHr = str(i.due_time).split(':')
                current_time = datetime.datetime.now() 

                if(int(dueData[2]) == int(date.today().day) and int(dueData[1]) == int(date.today().month) and int(dueData[0]) == int(date.today().year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'   
                        delay = delay + 1                     
                    i.due_date = new_format

                NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
                tommotowDate = str(NextDay_Date)
                print('NextDay_Date.day >>>> ',NextDay_Date.day)
                if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
                    new_format = 'Tommorow'
                    i.status = 'tommorow'                        
                    i.due_date = new_format                
                
                current_time = datetime.datetime.now() 

                from datetime import datetime
                if(int(dueData[2]) > int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == str(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) <= int(todays_date.day) and int(dueData[1]) <= int(todays_date.month) and int(dueData[0]) > int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 >>> ',i.due_date)
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date)
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                

                else:
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
                context['TaskObj'] = TaskObj

                context['todo'] = todo
                context['doing'] = doing
                context['done'] = done
                context['delay'] = delay

            # ==============================================================================================
            return render(request,'admin/dashboard.html',context)
        
        from datetime import date,timedelta
        today = date.today()
        date_today = date.today()
        eventsObj = event_bday_annivarsary_management.objects.filter(event_date__range=[date_today + timedelta(days=1), date_today + timedelta(days=30)],event_year = today.year).order_by('event_date')
        if(request.session['userType'] == 'teacheR'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id)) | Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))

            # =======================================================================================
            TaskObj = Task_Management.objects.filter(employeeFK=employeeFk).order_by('-id')[:20]

            todo = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'To do').count()
            doing = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Doing').count()
            done = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Done').count()
            delay = 0
            context = {}

            for i in TaskObj:
                dueData = str(i.due_date).split('-')
                print('due date >>> ',dueData)
                # ----------------------------------------------------------------------------------
                month = ''
                status = ''
                # ----------------------------------------------------------------------------------
                from datetime import date
                todays_date = date.today()
                print('todays_date.day >>>> ',todays_date.day)

                if(dueData[1] == '1'):
                    month = 'Jan'
                if(dueData[1] == '2'):
                    month = 'Feb'
                if(dueData[1] == '3'):
                    month = 'Mar'
                if(dueData[1] == '4'):
                    month = 'Apr'
                if(dueData[1] == '5'):
                    month = 'May'
                if(dueData[1] == '6'):
                    month = 'Jun'
                if(dueData[1] == '7'):
                    month = 'Jul'
                if(dueData[1] == '8'):
                    month = 'Aug'
                if(dueData[1] == '9'):
                    month = 'Sep'
                if(dueData[1] == '10'):
                    month = 'Oct'
                if(dueData[1] == '11'):
                    month = 'Nov'
                if(dueData[1] == '12'):
                    month = 'Dec'

                import datetime 
                timeHr = str(i.due_time).split(':')
                current_time = datetime.datetime.now() 

                if(int(dueData[2]) == int(date.today().day) and int(dueData[1]) == int(date.today().month) and int(dueData[0]) == int(date.today().year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'   
                        delay = delay + 1                     
                    i.due_date = new_format

                NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
                tommotowDate = str(NextDay_Date)
                print('NextDay_Date.day >>>> ',NextDay_Date.day)
                if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
                    new_format = 'Tommorow'
                    i.status = 'tommorow'                        
                    i.due_date = new_format                
                
                current_time = datetime.datetime.now() 

                from datetime import datetime
                if(int(dueData[2]) > int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == str(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) <= int(todays_date.day) and int(dueData[1]) <= int(todays_date.month) and int(dueData[0]) > int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 >>> ',i.due_date)
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date)
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                

                else:
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
                context['TaskObj'] = TaskObj

                context['todo'] = todo
                context['doing'] = doing
                context['done'] = done
                context['delay'] = delay
            # =======================================================================================
            return render(request,'admin/user-dashboard.html',{"projectObj":projectObj,'employeeFk':employeeFk,'eventsObj':eventsObj,'context':context})

        if(request.session['userType'] == 'studdenT'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))
            # =======================================================================================
            TaskObj = Task_Management.objects.filter(employeeFK=employeeFk).order_by('-id')[:20]

            todo = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'To do').count()
            doing = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Doing').count()
            done = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Done').count()
            delay = 0
            context = {}

            for i in TaskObj:
                dueData = str(i.due_date).split('-')
                print('due date >>> ',dueData)
                # ----------------------------------------------------------------------------------
                month = ''
                status = ''
                # ----------------------------------------------------------------------------------
                from datetime import date
                todays_date = date.today()
                print('todays_date.day >>>> ',todays_date.day)

                if(dueData[1] == '1'):
                    month = 'Jan'
                if(dueData[1] == '2'):
                    month = 'Feb'
                if(dueData[1] == '3'):
                    month = 'Mar'
                if(dueData[1] == '4'):
                    month = 'Apr'
                if(dueData[1] == '5'):
                    month = 'May'
                if(dueData[1] == '6'):
                    month = 'Jun'
                if(dueData[1] == '7'):
                    month = 'Jul'
                if(dueData[1] == '8'):
                    month = 'Aug'
                if(dueData[1] == '9'):
                    month = 'Sep'
                if(dueData[1] == '10'):
                    month = 'Oct'
                if(dueData[1] == '11'):
                    month = 'Nov'
                if(dueData[1] == '12'):
                    month = 'Dec'

                import datetime 
                timeHr = str(i.due_time).split(':')
                current_time = datetime.datetime.now() 

                if(int(dueData[2]) == int(date.today().day) and int(dueData[1]) == int(date.today().month) and int(dueData[0]) == int(date.today().year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'   
                        delay = delay + 1                     
                    i.due_date = new_format

                NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
                tommotowDate = str(NextDay_Date)
                print('NextDay_Date.day >>>> ',NextDay_Date.day)
                if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
                    new_format = 'Tommorow'
                    i.status = 'tommorow'                        
                    i.due_date = new_format                
                
                current_time = datetime.datetime.now() 

                from datetime import datetime
                if(int(dueData[2]) > int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == str(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) < int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) < int(todays_date.month) and int(dueData[0]) < int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) <= int(todays_date.day) and int(dueData[1]) <= int(todays_date.month) and int(dueData[0]) > int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 >>> ',i.due_date)
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                
                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date)
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format

                if(int(dueData[2]) >= int(todays_date.day) and int(dueData[1]) >= int(todays_date.month) and int(dueData[0]) >= int(todays_date.year)):
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = ''
                    if(i.due_date  == 'Today'):
                        date_1 = str(todays_date) 
                    elif(i.due_date  == 'Tommorow'):
                        print('tommotowDate >>>> ',str(tommotowDate))
                        date_1 = str(tommotowDate).split(' ')[0] 
                    else:
                        date_1 = str(i.due_date) 

                    print('date_1 001>>> ',i.due_date)
                    print('date_1 002>>> ',date_1)

                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    # i.status = 'delay'
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                

                else:
                    new_format = i.due_date 
                    # ---------------------------------
                    date_1 = str(i.due_date) 
                    date_2 = str(todays_date)
                    start = datetime.strptime(date_1, "%Y-%m-%d")
                    end =   datetime.strptime(date_2, "%Y-%m-%d")
                    # get the difference between wo dates as timedelta object
                    diff = end.date() - start.date()
                    print('Difference between dates in days:')
                    print(diff.days)
                    # ---------------------------------
                    i.status = 'delay'
                    delay = delay + 1   
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
                context['TaskObj'] = TaskObj

                context['todo'] = todo
                context['doing'] = doing
                context['done'] = done
                context['delay'] = delay
            # =======================================================================================
            return render(request,'admin/user-dashboard.html',{"projectObj":projectObj,'employeeFk':employeeFk,'eventsObj':eventsObj,'context':context})
# ##########################################################################################################
@login_required(login_url='/')
def profile(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            return redirect('/')
        else:
            user_fk = User.objects.get(email=request.user.email)
            employeeObj = employeeDetails.objects.get(userFK=user_fk)
            work_experience = employeeObj.work_experience.split('|')
            last_designation = None
            company = None
            duration = None
            if((work_experience[0].strip() != 'None') and (work_experience[0].strip() != '') and (work_experience[0].strip() != 'null')):
                last_designation = designation_Master.objects.get(id=int(work_experience[0].strip()))
                company = work_experience[1]
                duration = work_experience[2]
            qualificationList = []
            try:
                for j in employeeObj.qualification.split('|'):
                    data = j.split('$')
                    qualificationDict = {}
                    qualificationDict['qualification'] = '-'
                    qualificationDict['passing_year'] = '-'
                    if(data[0] != ''):
                        qualificationDict['qualification'] = qualification_Master.objects.get(id=data[0]).qualification_type
                    qualificationDict['from'] = data[1]
                    if(data[2] != ''):
                        qualificationDict['passing_year'] = passingYear_Master.objects.get(id=data[2]).passingYear
                    qualificationList.append(qualificationDict)
            except:
                qualificationList = []
        return render(request,'authentication/profile.html',{'employeeObj':employeeObj,'last_designation':last_designation,'company':company,'duration':duration,"qualificationList":qualificationList})

# ##########################################################################################################
@login_required(login_url='/')
def change_password(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            return render(request,'authentication/change-password.html',{})
        if(request.session['userType'] == 'teacheR'):
            return render(request,'authentication/change-password.html',{})
        if(request.session['userType'] == 'studdenT'):
            return render(request,'authentication/change-password.html',{})

    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            message = 'success'
            old_pass = request.POST['old_password']
            new_pass = request.POST['new_password']
            user = authenticate(username=request.user.username, password=old_pass)
            if(user is not None):
                try:
                    u = User.objects.get(username__exact=request.user.username)
                    u.set_password(new_pass)
                    u.save()

                    try:
                        e = employee_Password.objects.get(userFK = request.user)
                        e.user_password = new_pass
                    except:
                        e = employee_Password(
                            userFK = request.user,
                            user_password = new_pass
                        )
                    e.save()
                except:
                    message = 'fail'
            else:
                message = 'authFailed'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            message = 'success'
            old_pass = request.POST['old_password']
            new_pass = request.POST['new_password']
            user = authenticate(username=request.user.username, password=old_pass)
            if(user is not None):
                try:
                    u = User.objects.get(username__exact=request.user.username)
                    u.set_password(new_pass)
                    u.save()

                    try:
                        e = employee_Password.objects.get(userFK = request.user)
                        e.user_password = new_pass
                    except:
                        e = employee_Password(
                            userFK = request.user,
                            user_password = new_pass
                        )
                    e.save()
                except:
                    message = 'fail'
            else:
                message = 'authFailed'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'studdenT'):
            message = 'success'
            old_pass = request.POST['old_password']
            new_pass = request.POST['new_password']
            user = authenticate(username=request.user.username, password=old_pass)
            if(user is not None):
                try:
                    u = User.objects.get(username__exact=request.user.username)
                    u.set_password(new_pass)
                    u.save()

                    try:
                        e = employee_Password.objects.get(userFK = request.user)
                        e.user_password = new_pass
                    except:
                        e = employee_Password(
                            userFK = request.user,
                            user_password = new_pass
                        )
                    e.save()
                except:
                    message = 'fail'
            else:
                message = 'authFailed'
            return JsonResponse({'response':message})
# ##########################################################################################################
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('user_login')
# ##########################################################################################################
def unautorizedaccess(request):
    if request.method == 'GET':
        return render(request,'unauthorizedAccess.html')
# ##########################################################################################################
def get_notifications(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            notificationObj = Notification_Management.objects.filter(admin_read_status = False,admin_trash_status = False).order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id') 
            trash = Notification_Management.objects.filter(admin_trash_status = True).order_by('-id') 
            starred = Notification_Management.objects.filter(admin_starred_status = True).order_by('-id')

        if(request.session['userType'] == 'teacheR'):
            notificationObj = Notification_Management.objects.filter(notification_to = request.user,manager_read_status = False,manager_trash_status = False).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,manager_read_status = False,manager_trash_status = False).order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id')
            trash = Notification_Management.objects.filter(notification_to = request.user,emp_trash_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_trash_status = True).order_by('-id')  
            starred = Notification_Management.objects.filter(notification_to = request.user,emp_starred_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_starred_status = True).order_by('-id')
        if(request.session['userType'] == 'studdenT'):
            notificationObj = Notification_Management.objects.filter(notification_to = request.user,emp_read_status = False,emp_trash_status = False).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_read_status = False,emp_trash_status = False).order_by('-id')
            sent = Notification_Management.objects.filter(notification_from = request.user).order_by('-id')
            trash = Notification_Management.objects.filter(notification_to = request.user,emp_trash_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_trash_status = True).order_by('-id')  
            starred = Notification_Management.objects.filter(notification_to = request.user,emp_starred_status = True).order_by('-id') | Notification_Management.objects.filter(notification_from = request.user,emp_starred_status = True).order_by('-id')

        return JsonResponse({'response':len(notificationObj),'sent':len(sent),'trash':len(trash),'starred':len(starred)})