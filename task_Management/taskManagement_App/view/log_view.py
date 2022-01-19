from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.employee_model import employeeDetails
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from ..models.logs_model import AuditEntry
from django.contrib.sessions.models import Session

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list)
# -------------------------------------------------------------------------------------------------------------
@login_required(login_url='/')
def online_employess(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            queryset = get_current_users()
            empObj = employeeDetails.objects.all() 
            never_logged_in_count = 0
            for i in empObj:
                userObj = AuditEntry.objects.filter(username = i.userFK.username).order_by('-id')
                if(len(userObj) == 0):
                    never_logged_in_count = never_logged_in_count + 1
            for i in empObj:
                i.active = False
                for j in queryset:
                    if(str(i.userFK.email) == str(j.email)):
                        i.active = True
                    else:
                        userObj = AuditEntry.objects.filter(username = i.userFK.username).order_by('-id')
                        if(len(userObj) == 0):
                            i.last_logged_in = 'Never logged in'
                        else:
                            i.last_logged_in = '-'
            return render(request,'admin/logs/online-users.html',{'queryset':queryset,'empObj':empObj,'never_logged_in_count':never_logged_in_count,'offlineUser_length':len(empObj)-(len(queryset)-1),'queryset_length':len(queryset)-1})
        else:
            return render(request,'unauthorizedAccess.html')
    else:
        return render(request,'unauthorizedAccess.html')
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
@login_required(login_url='/')
def logs(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            logObj = AuditEntry.objects.all().order_by('-id')
            return render(request,'admin/logs/logs.html',{'logObj':logObj})
        else:
            return render(request,'unauthorizedAccess.html')
    else:
        return render(request,'unauthorizedAccess.html')
