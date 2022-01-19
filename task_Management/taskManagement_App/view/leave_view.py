from datetime import date
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from taskManagement_App.models.notification_model import Notification_Management
from taskManagement_App.view.notification_view import notification
from django.contrib.auth.decorators import login_required
from ..models.master_models import *
from ..models.employee_model import employeeDetails
from ..models.leave_model import leave_management,holiday_management,leave_allotment_management
from django.contrib.auth.models import User
import datetime
# #############################################################################################################
@login_required(login_url='/')
def get_leave_record(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            userObj = User.objects.filter(is_superuser=False,is_active=True).order_by('-id')
            for i in userObj:
                empObj = employeeDetails.objects.get(userFK=i)
                i.employee_name = empObj.employee_name
                i.profilePic = empObj.profile_image
                i.empID = empObj.id
                # =========================================================================================================================================
                # alloted_leaveObj = leave_allotment_management.objects.filter(employeeFK = empObj,created_at__gte=datetime.date(date.today().year, 4, 1),
                #                 created_at__lte=datetime.date(date.today().year+1, 3, 31))
                alloted_leaveObj = leave_allotment_management.objects.filter(employeeFK = empObj).order_by('-id')

                allot_count = 0
                for j in alloted_leaveObj:
                    allot_count = allot_count + int(j.no_of_days)
                i.allot_leave = allot_count
                # =========================================================================================================================================
                takenleaveObj = leave_management.objects.filter(employeeFK = empObj,created_at__gte=datetime.date(date.today().year, 1, 4),
                                created_at__lte=datetime.date(date.today().year+1, 3, 31),leave_approval_status='approved')
                taken_count = 0
                for k in takenleaveObj:
                    if(k.leave_date_to == None):
                        taken_count = taken_count + 1
                    else:
                        date1 = k.leave_date_from
                        date2 = k.leave_date_to
                        taken_count = taken_count + ((date2-date1).days + 1)
                i.taken_leave = taken_count
                i.remaining_leave = allot_count - taken_count                
                # =========================================================================================================================================
            return render(request,'admin/leaves/leave-record.html',{'userObj':userObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def deleteHoliday(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            holidayObj = holiday_management.objects.get(id=int(id))
            holidayObj.delete()
            return redirect('holiday_list')
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def fetchHoliday(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            import datetime
            try:
                holidayObj = holiday_management.objects.get(id=int(id))
                date_from = datetime.datetime.strptime(str(holidayObj.holiday_fromDate), '%Y-%M-%d').strftime('%d-%M-%Y')
                date_to = None
                if(holidayObj.holiday_toDate != None and holidayObj.holiday_toDate != ''):
                    date_to = datetime.datetime.strptime(str(holidayObj.holiday_toDate), '%Y-%M-%d').strftime('%d-%M-%Y')
                dataList = [   
                    {
                        'holiday_name' : holidayObj.holiday_name,
                        'from_date' : date_from,
                        'to_date' : date_to,
                        'holiday_year' : holidayObj.holiday_year,
                        'holiday_ID' : holidayObj.id,
                    }
                ]
                return JsonResponse({'response':dataList})
            except:
                dataList = []
                return JsonResponse({'response':dataList})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def edit_holiday(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            holiday_Year = request.POST['holidayYear']
            holidayfromDate = request.POST.get('holiday_fromDate').split('-')
            holidaytoDate = request.POST.get('holiday_toDate').split('-')
            holiday_Name = request.POST['holidayName']
            if(len(holidayfromDate) > 1):
                if(holidayfromDate[1] == 'Jan'):
                    holidayfromDate[1] = 1
                if(holidayfromDate[1] == 'Feb'):
                    holidayfromDate[1] = 2
                if(holidayfromDate[1] == 'Mar'):
                    holidayfromDate[1] = 3
                if(holidayfromDate[1] == 'Apr'):
                    holidayfromDate[1] = 4
                if(holidayfromDate[1] == 'May'):
                    holidayfromDate[1] = 5
                if(holidayfromDate[1] == 'Jun'):
                    holidayfromDate[1] = 6
                if(holidayfromDate[1] == 'Jul'):
                    holidayfromDate[1] = 7
                if(holidayfromDate[1] == 'Aug'):
                    holidayfromDate[1] = 8
                if(holidayfromDate[1] == 'Sep'):
                    holidayfromDate[1] = 9
                if(holidayfromDate[1] == 'Oct'):
                    holidayfromDate[1] = 10
                if(holidayfromDate[1] == 'Nov'):
                    holidayfromDate[1] = 11
                if(holidayfromDate[1] == 'Dec'):
                    holidayfromDate[1] = 12
                holidayfromDate = f"{holidayfromDate[2]}-{holidayfromDate[1]}-{holidayfromDate[0]}"
            else:
                holidayfromDate = None
            if(len(holidaytoDate) > 1):
                if(holidaytoDate[1] == 'Jan'):
                    holidaytoDate[1] = 1
                if(holidaytoDate[1] == 'Feb'):
                    holidaytoDate[1] = 2
                if(holidaytoDate[1] == 'Mar'):
                    holidaytoDate[1] = 3
                if(holidaytoDate[1] == 'Apr'):
                    holidaytoDate[1] = 4
                if(holidaytoDate[1] == 'May'):
                    holidaytoDate[1] = 5
                if(holidaytoDate[1] == 'Jun'):
                    holidaytoDate[1] = 6
                if(holidaytoDate[1] == 'Jul'):
                    holidaytoDate[1] = 7
                if(holidaytoDate[1] == 'Aug'):
                    holidaytoDate[1] = 8
                if(holidaytoDate[1] == 'Sep'):
                    holidaytoDate[1] = 9
                if(holidaytoDate[1] == 'Oct'):
                    holidaytoDate[1] = 10
                if(holidaytoDate[1] == 'Nov'):
                    holidaytoDate[1] = 11
                if(holidaytoDate[1] == 'Dec'):
                    holidaytoDate[1] = 12
                holidaytoDate = f"{holidaytoDate[2]}-{holidaytoDate[1]}-{holidaytoDate[0]}"
            else:
                holidaytoDate = None
            # ------------------------------------------------------------------
            no_of_days = 0
            if(holidaytoDate == None):
                no_of_days = no_of_days + 1
            else:
                date1 = holidayfromDate.split('-')
                date2 = holidaytoDate.split('-')
                date_1 = date(int(date1[0]),int(date1[1]),int(date1[2]))
                date_2 = date(int(date2[0]),int(date2[1]),int(date2[2]))

                no_of_days = int(no_of_days) + int((int((date_2-date_1).days) + int(1)))
            # ------------------------------------------------------------------
            message = 'success'
            # ---------------------------------------------------------------------------------
            try:
                holidayObj = holiday_management.objects.get(id=int(id))
                holidayObj.holiday_name = holiday_Name
                holidayObj.holiday_fromDate = holidayfromDate
                holidayObj.holiday_toDate = holidaytoDate
                holidayObj.holiday_year = holiday_Year
                holidayObj.holiday_number = no_of_days
                holidayObj.save()
            except:
                message = 'fail'
            # ---------------------------------------------------------------------------------
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
    if request.method == 'GET':
        return redirect('unautorizedaccess')
# 
# #############################################################################################################
@login_required(login_url='/')
def get_leave_record_history(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.get(id=int(id))
            leaveObj = leave_management.objects.filter(employeeFK = empObj)
            employeeData = [
                {
                    'employee_name' : empObj.employee_name,
                    'employee_image' : str(empObj.profile_image),
                }
            ]
            dataList = []
            for i in leaveObj:
                dataDict = {}
                if(i.leave_date_to == None):
                    dataDict['leave_date'] = str(datetime.datetime.strptime(str(i.leave_date_from), '%Y-%m-%d').strftime('%d %b'))
                    dataDict['leaveCount'] = 1
                else:
                    dataDict['leave_date'] = str(datetime.datetime.strptime(str(i.leave_date_from), '%Y-%m-%d').strftime('%d %b')) +' - ' + str(datetime.datetime.strptime(str(i.leave_date_to), '%Y-%m-%d').strftime('%d %b'))
                    date1 = i.leave_date_from
                    date2 = i.leave_date_to
                    dataDict['leaveCount'] = (date2-date1).days + 1
                dataDict['leaveReason'] = i.leave_reason
                dataDict['status'] = i.leave_approval_status
                dataList.append(dataDict)
            return JsonResponse({'response':dataList,'employeeData':employeeData})
        else:
            return redirect('unautorizedaccess')
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def get_leave_allotment(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            # allotObj = leave_allotment_management.objects.filter(created_at__gte=datetime.date(date.today().year, 4, 1),
            #                     created_at__lt=datetime.date(date.today().year+1, 3, 31)).order_by('-id')

            allotObj = leave_allotment_management.objects.all().order_by('-id')

            session = str(date.today().year)+"-"+str(date.today().year+1)
            return render(request,'admin/leaves/leave-allotment.html',{'empObj':empObj,'allotObj':allotObj,'session':session})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def get_alloted_leave_record(request):
    import datetime
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            return redirect('unautorizedaccess')
        else:
            empObj = employeeDetails.objects.get(userFK=request.user)
            allotObj = leave_allotment_management.objects.filter(employeeFK=empObj)
            dataArray = []
            for i in allotObj:
                context = {}
                dates = str(i.created_at).split('T')[0]
                context['no_of_leaves'] = i.no_of_days
                context['date'] = str(datetime.datetime.strptime(dates.split(' ')[0], '%Y-%m-%d').strftime('%d %b, %Y'))
                context['reason'] = i.leave_reason
                dataArray.append(context)
            return JsonResponse({'response':dataArray})
    if request.method == 'POST':
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def allot_leave(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/leaves/allot-leaves.html',{'empObj':empObj})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            emp_id = request.POST['empID']
            no_ofDays = request.POST['no_of_days']
            reason = request.POST['reason']
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(id=int(emp_id))
                allotObj = leave_allotment_management(
                    employeeFK = empObj,
                    no_of_days = no_ofDays,
                    leave_reason = reason
                )
                allotObj.save()
                # =======================================================================================
                # send notification of successfull allotment
                # =======================================================================================


                # =======================================================================================
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def delete_alloted_leave(request,id):
    if request.method == 'POST':
        return redirect('unautorizedaccess')
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            allotObj = leave_allotment_management.objects.get(id=int(id))
            empObj = employeeDetails.objects.get(id=int(allotObj.employeeFK.id))
            allotObj.delete()
            return redirect('get_leave_allotment')
        else:
            return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def get_leave_requests(request):
    from datetime import date
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            leaveObj = leave_management.objects.all().order_by('-id')
            for i in leaveObj:
                date1 = i.leave_date_from
                date2 = date.today()
                diff = (date1 - date2).days
                if(i.leave_date_to == None):
                    i.no_of_leaves = 1
                else:
                    date1 = i.leave_date_from
                    date2 = i.leave_date_to
                    i.no_of_leaves = (date2-date1).days + 1
                if(diff < 0):
                    i.view = 'no'
                else:
                    i.view = 'yes'
            return render(request,'admin/leaves/leave-requests.html',{'leaveObj':leaveObj,'empObj':empObj})
        else:
            return redirect('unautorizedaccess')
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def handle_leave_requests(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            response = request.POST['response']
            leaveObj = leave_management.objects.get(id=int(id))
            message = 'success'
            try:
                # --------------------------------------------------------
                if(response == 'approved'):
                    leaveObj.leave_approval_status = 'approved'
                else:
                    leaveObj.leave_approval_status = 'rejected'
                # # --------------------------------------------------------
                leaveObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def add_leave(request):
    if request.method == 'GET':
        from datetime import date
        import datetime
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/leaves/add-leaves.html',{'empObj':empObj})
        if(request.session['userType'] == 'teacheR' or request.session['userType'] == 'studdenT'):
            empObj = employeeDetails.objects.get(userFK=request.user)
            leaveObj = leave_management.objects.filter(employeeFK=empObj)
            for i in leaveObj:
                date1 = i.leave_date_from
                date2 = date.today()
                diff = (date1 - date2).days
                if(i.leave_date_to == None):
                    i.no_of_leaves = 1
                else:
                    date1 = i.leave_date_from
                    date2 = i.leave_date_to
                    i.no_of_leaves = (date2-date1).days + 1
                if(diff < 0):
                    i.view = 'no'
                else:
                    i.view = 'yes'
            # alloted_leaveObj = leave_allotment_management.objects.filter(employeeFK = empObj,created_at__gte=datetime.date(date.today().year, 1, 4),
            #                     created_at__lte=datetime.date(date.today().year+1, 3, 31))

            alloted_leaveObj = leave_allotment_management.objects.filter(employeeFK = empObj)
            allot_count = 0
            for j in alloted_leaveObj:
                allot_count = allot_count + int(j.no_of_days)
            # takenleaveObj = leave_management.objects.filter(employeeFK = empObj,created_at__gte=datetime.date(date.today().year, 1, 4),
            #                     created_at__lte=datetime.date(date.today().year+1, 3, 31),leave_approval_status='approved')
            takenleaveObj = leave_management.objects.filter(employeeFK = empObj,leave_approval_status='approved')
            taken_count = 0
            for k in takenleaveObj:
                if(k.leave_date_to == None):
                    taken_count = taken_count + 1
                else:
                    date1 = k.leave_date_from
                    date2 = k.leave_date_to
                    taken_count = taken_count + ((date2-date1).days + 1)       
            #########################################################################################################
            # notification generation
            #########################################################################################################
            # admin
            # notificationObj = Notification_Management()


            #########################################################################################################
            return render(request,'admin/leaves/user-leave-management.html',{'empObj':empObj,'leaveObj':leaveObj,'allot_leave':allot_count,'taken_leave':taken_count,'remaining_leave':allot_count - taken_count})
            
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            empID = request.POST['empID']
            fromDate = request.POST.get('fromDate').split('-')
            toDate = request.POST.get('toDate').split('-')
            reason = request.POST['reason']


            if(len(fromDate) > 1):
                if(fromDate[1] == 'Jan'):
                    fromDate[1] = 1
                if(fromDate[1] == 'Feb'):
                    fromDate[1] = 2
                if(fromDate[1] == 'Mar'):
                    fromDate[1] = 3
                if(fromDate[1] == 'Apr'):
                    fromDate[1] = 4
                if(fromDate[1] == 'May'):
                    fromDate[1] = 5
                if(fromDate[1] == 'Jun'):
                    fromDate[1] = 6
                if(fromDate[1] == 'Jul'):
                    fromDate[1] = 7
                if(fromDate[1] == 'Aug'):
                    fromDate[1] = 8
                if(fromDate[1] == 'Sep'):
                    fromDate[1] = 9
                if(fromDate[1] == 'Oct'):
                    fromDate[1] = 10
                if(fromDate[1] == 'Nov'):
                    fromDate[1] = 11
                if(fromDate[1] == 'Dec'):
                    fromDate[1] = 12
                fromDate = f"{fromDate[2]}-{fromDate[1]}-{fromDate[0]}"
            else:
                fromDate = None
            if(len(toDate) > 1):
                if(toDate[1] == 'Jan'):
                    toDate[1] = 1
                if(toDate[1] == 'Feb'):
                    toDate[1] = 2
                if(toDate[1] == 'Mar'):
                    toDate[1] = 3
                if(toDate[1] == 'Apr'):
                    toDate[1] = 4
                if(toDate[1] == 'May'):
                    toDate[1] = 5
                if(toDate[1] == 'Jun'):
                    toDate[1] = 6
                if(toDate[1] == 'Jul'):
                    toDate[1] = 7
                if(toDate[1] == 'Aug'):
                    toDate[1] = 8
                if(toDate[1] == 'Sep'):
                    toDate[1] = 9
                if(toDate[1] == 'Oct'):
                    toDate[1] = 10
                if(toDate[1] == 'Nov'):
                    toDate[1] = 11
                if(toDate[1] == 'Dec'):
                    toDate[1] = 12
                toDate = f"{toDate[2]}-{toDate[1]}-{toDate[0]}"
            else:
                toDate = None
            message = 'success'
            empObj = employeeDetails.objects.get(id=int(empID))
            leaveObj = leave_management(
                employeeFK = empObj,
                leave_date_from = fromDate,
                leave_date_to = toDate,
                leave_reason = reason,
                leave_approval_status = 'approved'
            )
            leaveObj.save()
            empObj = employeeDetails.objects.get(id=int(empID))
            try:
            # --------------------------------------------------------
                if(leaveObj.leave_date_to == None):
                        empObj.taken_leave = int(empObj.taken_leave) + 1
                        empObj.remaining_leave = int(empObj.alloted_leave) - int(empObj.remaining_leave) - 1
                else:
                    date1 = datetime.strptime(leaveObj.leave_date_from, '%Y-%m-%d')
                    date2 = datetime.strptime(leaveObj.leave_date_to, '%Y-%m-%d')
            except:
                message = 'fail'
            
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            fromDate = request.POST.get('fromDate').split('-')
            toDate = request.POST.get('toDate').split('-')
            reason = request.POST['reason']
            if(len(fromDate) > 1):
                if(fromDate[1] == 'Jan'):
                    fromDate[1] = 1
                if(fromDate[1] == 'Feb'):
                    fromDate[1] = 2
                if(fromDate[1] == 'Mar'):
                    fromDate[1] = 3
                if(fromDate[1] == 'Apr'):
                    fromDate[1] = 4
                if(fromDate[1] == 'May'):
                    fromDate[1] = 5
                if(fromDate[1] == 'Jun'):
                    fromDate[1] = 6
                if(fromDate[1] == 'Jul'):
                    fromDate[1] = 7
                if(fromDate[1] == 'Aug'):
                    fromDate[1] = 8
                if(fromDate[1] == 'Sep'):
                    fromDate[1] = 9
                if(fromDate[1] == 'Oct'):
                    fromDate[1] = 10
                if(fromDate[1] == 'Nov'):
                    fromDate[1] = 11
                if(fromDate[1] == 'Dec'):
                    fromDate[1] = 12

                fromDate = f"{fromDate[2]}-{fromDate[1]}-{fromDate[0]}"
            else:
                fromDate = None
            if(len(toDate) > 1):
                if(toDate[1] == 'Jan'):
                    toDate[1] = 1
                if(toDate[1] == 'Feb'):
                    toDate[1] = 2
                if(toDate[1] == 'Mar'):
                    toDate[1] = 3
                if(toDate[1] == 'Apr'):
                    toDate[1] = 4
                if(toDate[1] == 'May'):
                    toDate[1] = 5
                if(toDate[1] == 'Jun'):
                    toDate[1] = 6
                if(toDate[1] == 'Jul'):
                    toDate[1] = 7
                if(toDate[1] == 'Aug'):
                    toDate[1] = 8
                if(toDate[1] == 'Sep'):
                    toDate[1] = 9
                if(toDate[1] == 'Oct'):
                    toDate[1] = 10
                if(toDate[1] == 'Nov'):
                    toDate[1] = 11
                if(toDate[1] == 'Dec'):
                    toDate[1] = 12
                toDate = f"{toDate[2]}-{toDate[1]}-{toDate[0]}"
            else:
                toDate = None
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(userFK=request.user)
                leaveObj = leave_management(
                    employeeFK = empObj,
                    leave_date_from = fromDate,
                    leave_date_to = toDate,
                    leave_reason = reason,
                )
                leaveObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            fromDate = request.POST.get('fromDate').split('-')
            toDate = request.POST.get('toDate').split('-')
            reason = request.POST['reason']

            if(len(fromDate) > 1):
                if(fromDate[1] == 'Jan'):
                    fromDate[1] = 1
                if(fromDate[1] == 'Feb'):
                    fromDate[1] = 2
                if(fromDate[1] == 'Mar'):
                    fromDate[1] = 3
                if(fromDate[1] == 'Apr'):
                    fromDate[1] = 4
                if(fromDate[1] == 'May'):
                    fromDate[1] = 5
                if(fromDate[1] == 'Jun'):
                    fromDate[1] = 6
                if(fromDate[1] == 'Jul'):
                    fromDate[1] = 7
                if(fromDate[1] == 'Aug'):
                    fromDate[1] = 8
                if(fromDate[1] == 'Sep'):
                    fromDate[1] = 9
                if(fromDate[1] == 'Oct'):
                    fromDate[1] = 10
                if(fromDate[1] == 'Nov'):
                    fromDate[1] = 11
                if(fromDate[1] == 'Dec'):
                    fromDate[1] = 12
                fromDate = f"{fromDate[2]}-{fromDate[1]}-{fromDate[0]}"
            else:
                fromDate = None
            if(len(toDate) > 1):
                if(toDate[1] == 'Jan'):
                    toDate[1] = 1
                if(toDate[1] == 'Feb'):
                    toDate[1] = 2
                if(toDate[1] == 'Mar'):
                    toDate[1] = 3
                if(toDate[1] == 'Apr'):
                    toDate[1] = 4
                if(toDate[1] == 'May'):
                    toDate[1] = 5
                if(toDate[1] == 'Jun'):
                    toDate[1] = 6
                if(toDate[1] == 'Jul'):
                    toDate[1] = 7
                if(toDate[1] == 'Aug'):
                    toDate[1] = 8
                if(toDate[1] == 'Sep'):
                    toDate[1] = 9
                if(toDate[1] == 'Oct'):
                    toDate[1] = 10
                if(toDate[1] == 'Nov'):
                    toDate[1] = 11
                if(toDate[1] == 'Dec'):
                    toDate[1] = 12
                toDate = f"{toDate[2]}-{toDate[1]}-{toDate[0]}"
            else:
                toDate = None
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(userFK=request.user)
                leaveObj = leave_management(
                    employeeFK = empObj,
                    leave_date_from = fromDate,
                    leave_date_to = toDate,
                    leave_reason = reason,
                )
                leaveObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
# #############################################################################################################
@login_required(login_url='/')
def holiday_list(request):
    if request.method == 'GET':
        todays_date = date.today()
        holidayObj = holiday_management.objects.filter(holiday_year = todays_date.year)
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR' or request.session['userType'] == 'studdenT'):
            return render(request,'admin/leaves/list-of-holidays.html',{'holidayObj':holidayObj,})

    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            holiday_Year = request.POST['holidayYear']
            holidayfromDate = request.POST.get('holiday_fromDate').split('-')
            holidaytoDate = request.POST.get('holiday_toDate').split('-')
            holiday_Name = request.POST['holidayName']

            if(len(holidayfromDate) > 1):
                if(holidayfromDate[1] == 'Jan'):
                    holidayfromDate[1] = 1
                if(holidayfromDate[1] == 'Feb'):
                    holidayfromDate[1] = 2
                if(holidayfromDate[1] == 'Mar'):
                    holidayfromDate[1] = 3
                if(holidayfromDate[1] == 'Apr'):
                    holidayfromDate[1] = 4
                if(holidayfromDate[1] == 'May'):
                    holidayfromDate[1] = 5
                if(holidayfromDate[1] == 'Jun'):
                    holidayfromDate[1] = 6
                if(holidayfromDate[1] == 'Jul'):
                    holidayfromDate[1] = 7
                if(holidayfromDate[1] == 'Aug'):
                    holidayfromDate[1] = 8
                if(holidayfromDate[1] == 'Sep'):
                    holidayfromDate[1] = 9
                if(holidayfromDate[1] == 'Oct'):
                    holidayfromDate[1] = 10
                if(holidayfromDate[1] == 'Nov'):
                    holidayfromDate[1] = 11
                if(holidayfromDate[1] == 'Dec'):
                    holidayfromDate[1] = 12

                holidayfromDate = f"{holidayfromDate[2]}-{holidayfromDate[1]}-{holidayfromDate[0]}"
            else:
                holidayfromDate = None

            if(len(holidaytoDate) > 1):
                if(holidaytoDate[1] == 'Jan'):
                    holidaytoDate[1] = 1
                if(holidaytoDate[1] == 'Feb'):
                    holidaytoDate[1] = 2
                if(holidaytoDate[1] == 'Mar'):
                    holidaytoDate[1] = 3
                if(holidaytoDate[1] == 'Apr'):
                    holidaytoDate[1] = 4
                if(holidaytoDate[1] == 'May'):
                    holidaytoDate[1] = 5
                if(holidaytoDate[1] == 'Jun'):
                    holidaytoDate[1] = 6
                if(holidaytoDate[1] == 'Jul'):
                    holidaytoDate[1] = 7
                if(holidaytoDate[1] == 'Aug'):
                    holidaytoDate[1] = 8
                if(holidaytoDate[1] == 'Sep'):
                    holidaytoDate[1] = 9
                if(holidaytoDate[1] == 'Oct'):
                    holidaytoDate[1] = 10
                if(holidaytoDate[1] == 'Nov'):
                    holidaytoDate[1] = 11
                if(holidaytoDate[1] == 'Dec'):
                    holidaytoDate[1] = 12
                holidaytoDate = f"{holidaytoDate[2]}-{holidaytoDate[1]}-{holidaytoDate[0]}"
            else:
                holidaytoDate = None
            # ------------------------------------------------------------------
            no_of_days = 0
            if(holidaytoDate == None):
                no_of_days = no_of_days + 1
            else:
                date1 = holidayfromDate.split('-')
                date2 = holidaytoDate.split('-')
                date_1 = date(int(date1[0]),int(date1[1]),int(date1[2]))
                date_2 = date(int(date2[0]),int(date2[1]),int(date2[2]))

                no_of_days = int(no_of_days) + int((int((date_2-date_1).days) + int(1)))
            # ------------------------------------------------------------------
            message = 'success'
            # ---------------------------------------------------------------------------------
            holiObj = holiday_management.objects.filter(holiday_name = holiday_Name,
                holiday_fromDate = holidayfromDate,
                holiday_toDate = holidaytoDate,
                holiday_year = holiday_Year  
            )
            if(len(holiObj) > 0):
                return JsonResponse({'response':'Pair already exist'}) 

            holiObj = holiday_management.objects.filter(holiday_name = holiday_Name,
                holiday_year = holiday_Year  
            )
            if(len(holiObj) > 0):
                return JsonResponse({'response':'Pair1 already exist'}) 
            try:
                holidatObj = holiday_management(
                    holiday_name = holiday_Name,
                    holiday_fromDate = holidayfromDate,
                    holiday_toDate = holidaytoDate,
                    holiday_year = holiday_Year,
                    holiday_number = no_of_days
                )
                holidatObj.save()
            except:
                message = 'fail'
            # ---------------------------------------------------------------------------------
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
# #############################################################################################################
def allot_paid_leaves():
    from datetime import datetime
    empObj = employeeDetails.objects.all().order_by('-id')
    for i in empObj:
        date_format = "%m/%d/%Y"
        date_of_join = datetime.strptime(i.joiningDate, date_format)
        today_date = datetime.strptime(i.joiningDate, date_format)
        delta = today_date - date_of_join
# #############################################################################################################
@login_required(login_url='/')
def cancel_leave_request(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            leaveObj = leave_management.objects.get(id=int(id))
            date1 = leaveObj.leave_date_from
            date2 = date.today()
            diff = (date1 - date2).days
            if(leaveObj.leave_approval_status == 'pending' and diff > 0):
                leaveObj.delete()
            elif(leaveObj.leave_approval_status == 'approved' and diff > 0):
                leaveObj.delete()
            elif(leaveObj.leave_approval_status == 'rejected' and diff > 0):
                leaveObj.delete()

            return redirect('get_leave_requests')
        else:
            leaveObj = leave_management.objects.get(id=int(id))
            leaveObj.delete()
            return redirect('add_leave')
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def cancel_leave_request_to_admin(request,id):
    from datetime import date
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            return redirect('get_leave_requests')
        else:
            leaveObj = leave_management.objects.get(id=int(id))
            date1 = leaveObj.leave_date_from
            date2 = date.today()
            diff = (date1 - date2).days
            if(leaveObj.leave_approval_status == 'approved' and diff > 0):
                leaveObj.edit_leave_request = 'delete request'
                leaveObj.edit_date_from = None
                leaveObj.edit_date_to = None
                leaveObj.request_edit_date = date.today()
                leaveObj.save()
            return redirect('add_leave')
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def edit_leave_request(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            return redirect('get_leave_requests')
        else:
            # =================================================================================================
            fromDate = request.POST.get('fromDate').split('-')
            toDate = request.POST.get('toDate').split('-')
            reason = request.POST['reason']

            message = 'success'
            try:
                if(len(fromDate) > 1):
                    if(fromDate[1] == 'Jan'):
                        fromDate[1] = 1
                    if(fromDate[1] == 'Feb'):
                        fromDate[1] = 2
                    if(fromDate[1] == 'Mar'):
                        fromDate[1] = 3
                    if(fromDate[1] == 'Apr'):
                        fromDate[1] = 4
                    if(fromDate[1] == 'May'):
                        fromDate[1] = 5
                    if(fromDate[1] == 'Jun'):
                        fromDate[1] = 6
                    if(fromDate[1] == 'Jul'):
                        fromDate[1] = 7
                    if(fromDate[1] == 'Aug'):
                        fromDate[1] = 8
                    if(fromDate[1] == 'Sep'):
                        fromDate[1] = 9
                    if(fromDate[1] == 'Oct'):
                        fromDate[1] = 10
                    if(fromDate[1] == 'Nov'):
                        fromDate[1] = 11
                    if(fromDate[1] == 'Dec'):
                        fromDate[1] = 12
                    fromDate = f"{fromDate[2]}-{fromDate[1]}-{fromDate[0]}"
                else:
                    fromDate = None
                if(len(toDate) > 1):
                    if(toDate[1] == 'Jan'):
                        toDate[1] = 1
                    if(toDate[1] == 'Feb'):
                        toDate[1] = 2
                    if(toDate[1] == 'Mar'):
                        toDate[1] = 3
                    if(toDate[1] == 'Apr'):
                        toDate[1] = 4
                    if(toDate[1] == 'May'):
                        toDate[1] = 5
                    if(toDate[1] == 'Jun'):
                        toDate[1] = 6
                    if(toDate[1] == 'Jul'):
                        toDate[1] = 7
                    if(toDate[1] == 'Aug'):
                        toDate[1] = 8
                    if(toDate[1] == 'Sep'):
                        toDate[1] = 9
                    if(toDate[1] == 'Oct'):
                        toDate[1] = 10
                    if(toDate[1] == 'Nov'):
                        toDate[1] = 11
                    if(toDate[1] == 'Dec'):
                        toDate[1] = 12
                    toDate = f"{toDate[2]}-{toDate[1]}-{toDate[0]}"
                else:
                    toDate = None
                message = 'success'
                leaveObj = leave_management.objects.get(id=int(id))
                leaveObj.edit_date_from = fromDate
                leaveObj.edit_date_to = toDate
                leaveObj.leave_reason = reason
                leaveObj.edit_leave_request = 'edit request'
                leaveObj.request_edit_date = date.today()
                leaveObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def edit_leave(request,id):
    if request.method == 'POST':
        # =================================================================================================
        fromDate = request.POST.get('fromDate').split('-')
        toDate = request.POST.get('toDate').split('-')
        reason = request.POST['reason']
        message = 'success'
        try:
            if(len(fromDate) > 1):
                if(fromDate[1] == 'Jan'):
                    fromDate[1] = 1
                if(fromDate[1] == 'Feb'):
                    fromDate[1] = 2
                if(fromDate[1] == 'Mar'):
                    fromDate[1] = 3
                if(fromDate[1] == 'Apr'):
                    fromDate[1] = 4
                if(fromDate[1] == 'May'):
                    fromDate[1] = 5
                if(fromDate[1] == 'Jun'):
                    fromDate[1] = 6
                if(fromDate[1] == 'Jul'):
                    fromDate[1] = 7
                if(fromDate[1] == 'Aug'):
                    fromDate[1] = 8
                if(fromDate[1] == 'Sep'):
                    fromDate[1] = 9
                if(fromDate[1] == 'Oct'):
                    fromDate[1] = 10
                if(fromDate[1] == 'Nov'):
                    fromDate[1] = 11
                if(fromDate[1] == 'Dec'):
                    fromDate[1] = 12
                fromDate = f"{fromDate[2]}-{fromDate[1]}-{fromDate[0]}"
            else:
                fromDate = None
            if(len(toDate) > 1):
                if(toDate[1] == 'Jan'):
                    toDate[1] = 1
                if(toDate[1] == 'Feb'):
                    toDate[1] = 2
                if(toDate[1] == 'Mar'):
                    toDate[1] = 3
                if(toDate[1] == 'Apr'):
                    toDate[1] = 4
                if(toDate[1] == 'May'):
                    toDate[1] = 5
                if(toDate[1] == 'Jun'):
                    toDate[1] = 6
                if(toDate[1] == 'Jul'):
                    toDate[1] = 7
                if(toDate[1] == 'Aug'):
                    toDate[1] = 8
                if(toDate[1] == 'Sep'):
                    toDate[1] = 9
                if(toDate[1] == 'Oct'):
                    toDate[1] = 10
                if(toDate[1] == 'Nov'):
                    toDate[1] = 11
                if(toDate[1] == 'Dec'):
                    toDate[1] = 12
                toDate = f"{toDate[2]}-{toDate[1]}-{toDate[0]}"
            else:
                toDate = None
            message = 'success'
            leaveObj = leave_management.objects.get(id=int(id))
            leaveObj.leave_date_from = fromDate
            leaveObj.leave_date_to = toDate
            leaveObj.leave_reason = reason
            leaveObj.edit_leave_request = 'edit request done'
            leaveObj.save()
        except:
            message = 'fail'
        return JsonResponse({'response':message})
    else:
        return redirect('unautorizedaccess')
# #############################################################################################################
@login_required(login_url='/')
def fetch_leave(request,id):
    if request.method == 'GET':
        leaveObj = leave_management.objects.get(id=int(id))
        dataDict = {}
        try:
            date_format = "%Y-%m-%d"
            if(leaveObj.edit_date_from == None):
                if(leaveObj.leave_date_to == None):
                    dataDict['from'] = datetime.strptime(str(leaveObj.leave_date_from), date_format).strftime('%d-%b-%Y')
                    dataDict['to'] = ''
                else:
                    dataDict['from'] = datetime.strptime(str(leaveObj.leave_date_from), date_format).strftime('%d-%b-%Y')
                    dataDict['to'] = datetime.strptime(str(leaveObj.leave_date_to), date_format).strftime('%d-%b-%Y')
            else:
                if(leaveObj.edit_date_from == None and leaveObj.edit_date_to == None):
                    dataDict['from'] = ''
                    dataDict['to'] = ''
                elif(leaveObj.edit_date_to == None):
                    dataDict['from'] = datetime.strptime(str(leaveObj.edit_date_from), date_format).strftime('%d-%b-%Y')
                    dataDict['to'] = ''
                else:
                    dataDict['from'] = datetime.strptime(str(leaveObj.edit_date_from), date_format).strftime('%d-%b-%Y')
                    dataDict['to'] = datetime.strptime(str(leaveObj.edit_date_to), date_format).strftime('%d-%b-%Y')
            dataDict['reason'] = leaveObj.leave_reason
        except:
            dataDict = {}
        return JsonResponse({'response':dataDict})
    else:
        return redirect('unautorizedaccess')