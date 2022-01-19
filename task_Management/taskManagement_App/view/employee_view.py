from datetime import date
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from taskManagement_App.models.notification_model import Notification_Management
from ..models.master_models import designation_Master
from django.contrib.auth.decorators import login_required
from ..models.master_models import *
from ..models.employee_model import employeeDetails,employee_Password,employee_request_edit
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# ##########################################################################################################
@login_required(login_url='/')
def send_credentials(request,id):
    empObj = employeeDetails.objects.get(id=int(id))
    empName = empObj.employee_name
    Id = empObj.userFK.email
    Password = ''
    try:
        e = employee_Password.objects.get(userFK = empObj.userFK)
        Password = e.user_password
    except:
        Password = empObj.contact
    html_content = render_to_string('admin/emailTemplates/password-send-email.html',{'empName':empName,'Id':Id,'Password':Password})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(f"Login Credentials",text_content,settings.EMAIL_HOST_USER,[Id])
    email.attach_alternative(html_content,'text/html')
    email.send()
    empObj.send_credentials = 'sent'
    empObj.save()
    return redirect('employee_list')
# ##########################################################################################################
@login_required(login_url='/')
def add_employee(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            qualification = qualification_Master.objects.all().order_by('-id')
            experience = experience_Master.objects.all().order_by('id')
            passing_year = passingYear_Master.objects.all().order_by('id')
            employee_type = employeeType_Master.objects.all().order_by('-id')
            designation = designation_Master.objects.all().order_by('-id')
            document = document_Master.objects.all().order_by('-id')
            qualificatiIdList = []
            qualificationValueList = []
            for i in qualification:
                qualificatiIdList.append(i.id)
                qualificationValueList.append(i.qualification_type)
            documentID = []
            documentValue = []
            for i in document:
                documentID.append(i.id)
                documentValue.append(i.document_type)
            yearID = []
            yearValue = []
            for i in passing_year:
                yearID.append(i.id)
                yearValue.append(i.passingYear)
            context = {}
            context['qualification'] = qualification
            context['experience'] = experience
            context['passing_year'] = passing_year
            context['employee_type'] = employee_type
            context['designation'] = designation
            context['document'] = document
            context['qualificatiIdList'] = qualificatiIdList
            context['qualificationValueList'] = qualificationValueList
            context['documentID'] = documentID
            context['documentValue'] = documentValue
            context['yearID'] = yearID
            context['yearValue'] = yearValue
            return render(request,'admin/employee/add-employee.html',context)
        else:
            return redirect('unautorizedaccess')
    
    if request.method == 'POST':
        # try:
        if(request.session['userType'] == 'masteR'):
            empID =  request.POST.get('empID')
            fullname =  request.POST.get('fullname')
            email =  request.POST.get('email')
            contact =  request.POST.get('contact')
            alternateContact =  request.POST.get('alternateContact')
            datOfBirth =  request.POST.get('dateOfBirth')
            if(len(str(datOfBirth)) != 0):
                import datetime
                datOfBirth = datetime.datetime.strptime(str(datOfBirth), '%d-%b-%Y').strftime('%Y-%m-%d')
            else:
                datOfBirth = None
            fathersName =  request.POST.get('fathersName')
            address =  request.POST.get('address')
            pincode =  request.POST.get('pincode')
            state =  request.POST.get('state')
            city =  request.POST.get('city')
            empType =  request.POST.get('empType')
            experience =  request.POST.get('experience')
            current_Designation =  request.POST.get('current_Designation')
            dateOfJoin =  request.POST.get('dateOfJoin').split('-')
            if(len(dateOfJoin) > 1):
                if(dateOfJoin[1] == 'Jan'):
                    dateOfJoin[1] = 1
                if(dateOfJoin[1] == 'Feb'):
                    dateOfJoin[1] = 2
                if(dateOfJoin[1] == 'Mar'):
                    dateOfJoin[1] = 3
                if(dateOfJoin[1] == 'Apr'):
                    dateOfJoin[1] = 4
                if(dateOfJoin[1] == 'May'):
                    dateOfJoin[1] = 5
                if(dateOfJoin[1] == 'Jun'):
                    dateOfJoin[1] = 6
                if(dateOfJoin[1] == 'Jul'):
                    dateOfJoin[1] = 7
                if(dateOfJoin[1] == 'Aug'):
                    dateOfJoin[1] = 8
                if(dateOfJoin[1] == 'Sep'):
                    dateOfJoin[1] = 9
                if(dateOfJoin[1] == 'Oct'):
                    dateOfJoin[1] = 10
                if(dateOfJoin[1] == 'Nov'):
                    dateOfJoin[1] = 11
                if(dateOfJoin[1] == 'Dec'):
                    dateOfJoin[1] = 12
                dateOfJoin = f"{dateOfJoin[2]}-{dateOfJoin[1]}-{dateOfJoin[0]}"
            else:
                dateOfJoin = None
            last_experience =  request.POST.get('last_experience')
            Company =  request.POST.get('Company')
            Duration =  request.POST.get('Duration')
            QualificationDetails =  request.POST.get('QualificationDetails')
            profilePic =  request.FILES.get('profile_image')
            uploadType =  request.POST.get('upload_docs_type_0')
            UploadData =  request.FILES.get('upload_docs_0')
            uploadType_1 =  request.POST.get('upload_docs_type_1')
            UploadData_1 =  request.FILES.get('upload_docs_1')
            uploadType_2 =  request.POST.get('upload_docs_type_2')
            UploadData_2 =  request.FILES.get('upload_docs_2')
            uploadType_3 =  request.POST.get('upload_docs_type_3')
            UploadData_3 =  request.FILES.get('upload_docs_4')
            uploadType_4 =  request.POST.get('upload_docs_type_4')
            UploadData_4 =  request.FILES.get('upload_docs_4')
            message = 'success'
            try:
                if(employeeDetails.objects.filter(employee_id = empID)):
                    message='User With this Employee ID Already Exist!'
                    return JsonResponse({'response':message})
                if(User.objects.filter(email=email)):
                    message='User With this Email Already Exist!'
                    return JsonResponse({'response':message})
                if(employeeDetails.objects.filter(contact=contact)):
                    message='User With this Contact Already Exist!'
                    return JsonResponse({'response':message})
                if(empType == '1'):
                    user_fk = User.objects.create_user(username=email,password=contact,email=email,first_name=fullname)
                    user_fk.is_staff=True
                    user_fk.save()
                else:
                    user_fk = User.objects.create_user(username=email,password=contact,email=email,first_name=fullname)
                    user_fk.save()

                userObj = User.objects.get(email=email)
                designation_fk = None
                if(current_Designation != 'None'):
                    designation_fk = designation_Master.objects.get(id=current_Designation)
                employeeType_fk = None
                if(empType != 'Select Employee Type'):
                    employeeType_fk = employeeType_Master.objects.get(id=empType)
                experience_year_fk = None
                if(experience != 'None'):
                    experience_year_fk = experience_Master.objects.get(id=experience)
                employeeObj = employeeDetails(
                            userFK = userObj,
                            employee_name = fullname,
                            employee_id = empID,
                            father_name = fathersName,
                            state = state,
                            city = city,
                            pincode = pincode,
                            contact = contact,
                            alternate_contact = alternateContact,
                            DOB = datOfBirth,
                            address = address,
                            designationFK = designation_fk,
                            employeeTypeFK = employeeType_fk,
                            joiningDate = dateOfJoin,
                            qualification = QualificationDetails,
                            experience_year = experience_year_fk,
                            work_experience = f"{last_experience} | {Company} | {Duration}",
                            profile_image = profilePic,

                            upload_docs_type = uploadType,
                            upload_docs = UploadData,
                            upload_docs_type_2 = uploadType_1,
                            upload_docs_2 = UploadData_1,
                            upload_docs_type_3 = uploadType_2,
                            upload_docs_3 = UploadData_2,
                            upload_docs_type_4 = uploadType_3,
                            upload_docs_4 = UploadData_3,
                            upload_docs_type_5 = uploadType_4,
                            upload_docs_5 = UploadData_4,
                        )
                employeeObj.save()
                return JsonResponse({'response':message})
            except:
                obj = User.objects.latest('id')
                obj.delete()
            return JsonResponse({'response':'Error'})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def employee_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            employeeObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/employee/employee-list.html',{'employeeObj':employeeObj})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
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

from datetime import datetime
@login_required(login_url='/')
def filter_users(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            # searchFilter = User.objects.filter(is_superuser=False)
            # employeeObj = employeeDetails.objects.all().order_by('-id')
            context = []
            queryset = get_current_users()
            empObj = employeeDetails.objects.all() 
            never_logged_in_count = 0
            for i in empObj:
                userObj = AuditEntry.objects.filter(username = i.userFK.username).order_by('-id')
                if(len(userObj) == 0):
                    never_logged_in_count = never_logged_in_count + 1
            for i in empObj:
                dictData = {}
                dictData['emp'] = i.employee_name
                dictData['emp_img'] = str(i.profile_image)

                i.active = False
                dictData['active_status'] = False

                for j in queryset:
                    if(str(i.userFK.email) == str(j.email)):
                        i.active = True
                        dictData['active_status'] = True

                    else:
                        userObj = AuditEntry.objects.filter(username = i.userFK.username).order_by('-id')
                        if(len(userObj) == 0):
                            i.last_logged_in = 'Never logged in'
                            dictData['logged_in'] = 'Never logged in'
                        else:
                            i.last_logged_in = '-'
                              
                            data = i.userFK.last_login.strftime("%Y-%m-%d, %H:%M:%S")
                            dictData['logged_in'] = str(data)

                context.append(dictData)
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def update_employee_active_status(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            status = request.POST['status']
            employeeObj = employeeDetails.objects.get(id=int(id))
            userObj = User.objects.get(id = int(employeeObj.userFK.id))
            message = 'success'
            if(status == 'activate'):
                userObj.is_active = False
                userObj.save()
            elif(status == 'deactivate'):
                userObj.is_active = True
                userObj.save()
            else:
                message = 'Fail'
            return JsonResponse({'response':message})
        else:
            message = 'Unauthorized Personal'
# ##########################################################################################################
@login_required(login_url='/')
def view_employee_detail(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            employeeObj = employeeDetails.objects.get(id=id)
            work_experience = employeeObj.work_experience.split('|')
            last_designation = None
            company = None
            duration = None
            if((work_experience[0].strip() != 'None') and (work_experience[0].strip() != 'null')):
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
            return render(request,'admin/employee/view-employee-detail.html',{'employeeObj':employeeObj,'last_designation':last_designation,'company':company,'duration':duration,"qualificationList":qualificationList})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def update_employee_detail(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            qualification = qualification_Master.objects.all().order_by('-id')
            experience = experience_Master.objects.all().order_by('id')
            passing_year = passingYear_Master.objects.all().order_by('id')
            employee_type = employeeType_Master.objects.all().order_by('-id')
            designation = designation_Master.objects.all().order_by('-id')
            document = document_Master.objects.all().order_by('-id')
            qualificatiIdList = []
            qualificationValueList = []
            for i in qualification:
                qualificatiIdList.append(i.id)
                qualificationValueList.append(i.qualification_type)
            documentID = []
            documentValue = []
            for i in document:
                documentID.append(i.id)
                documentValue.append(i.document_type)
            yearID = []
            yearValue = []
            for i in passing_year:
                yearID.append(i.id)
                yearValue.append(i.passingYear)
            context = {}
            context['qualification'] = qualification
            context['experience'] = experience
            context['passing_year'] = passing_year
            context['employee_type'] = employee_type
            context['designation'] = designation
            context['document'] = document
            context['qualificatiIdList'] = qualificatiIdList
            context['qualificationValueList'] = qualificationValueList
            context['documentID'] = documentID
            context['documentValue'] = documentValue
            context['yearID'] = yearID
            context['yearValue'] = yearValue
            empObj = employeeDetails.objects.get(id=int(id))
            context['empObj'] = empObj
            count = 1
            if(empObj.upload_docs_type !=None):
                count = count + 1
            if(empObj.upload_docs_type_2 !=None):
                count = count + 1
            if(empObj.upload_docs_type_3 !=None):
                count = count + 1
            if(empObj.upload_docs_type_4 !=None):
                count = count + 1
            if(empObj.upload_docs_type_5 !=None):
                count = count + 1
            context['count'] = count
            return render(request,'admin/employee/edit-employee-detail.html',context)
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            empID =  request.POST.get('empID')
            fullname =  request.POST.get('fullname')
            email =  request.POST.get('email')
            contact =  request.POST.get('contact')
            alternateContact =  request.POST.get('alternateContact')
            DOB =  request.POST.get('DOB').split('/')
            dob = ''
            if(len(DOB) > 1):
                dob = f"{DOB[2]}-{DOB[0]}-{DOB[1]}"
            else:
                dob = None
            fathersName =  request.POST.get('fathersName')
            address =  request.POST.get('address')
            pincode =  request.POST.get('pincode')
            state =  request.POST.get('state')
            city =  request.POST.get('city')
            empType =  request.POST.get('empType')
            experience =  request.POST.get('experience')
            current_Designation =  request.POST.get('current_Designation')
            dateOfJoin =  request.POST.get('dateOfJoin').split('-')
            if(len(dateOfJoin) > 1):
                if(dateOfJoin[1] == 'Jan'):
                    dateOfJoin[1] = 1
                if(dateOfJoin[1] == 'Feb'):
                    dateOfJoin[1] = 2
                if(dateOfJoin[1] == 'Mar'):
                    dateOfJoin[1] = 3
                if(dateOfJoin[1] == 'Apr'):
                    dateOfJoin[1] = 4
                if(dateOfJoin[1] == 'May'):
                    dateOfJoin[1] = 5
                if(dateOfJoin[1] == 'Jun'):
                    dateOfJoin[1] = 6
                if(dateOfJoin[1] == 'Jul'):
                    dateOfJoin[1] = 7
                if(dateOfJoin[1] == 'Aug'):
                    dateOfJoin[1] = 8
                if(dateOfJoin[1] == 'Sep'):
                    dateOfJoin[1] = 9
                if(dateOfJoin[1] == 'Oct'):
                    dateOfJoin[1] = 10
                if(dateOfJoin[1] == 'Nov'):
                    dateOfJoin[1] = 11
                if(dateOfJoin[1] == 'Dec'):
                    dateOfJoin[1] = 12
                dateOfJoin = f"{dateOfJoin[2]}-{dateOfJoin[1]}-{dateOfJoin[0]}"
            else:
                dateOfJoin = None
            last_experience =  request.POST.get('last_experience')
            Company =  request.POST.get('Company')
            Duration =  request.POST.get('Duration')
            QualificationDetails =  request.POST.get('QualificationDetails')
            profilePic =  request.FILES.get('profile_image')
            uploadType =  request.POST.get('upload_docs_type_0')
            UploadData =  request.FILES.get('upload_docs_0')
            uploadType_1 =  request.POST.get('upload_docs_type_1')
            UploadData_1 =  request.FILES.get('upload_docs_1')
            uploadType_2 =  request.POST.get('upload_docs_type_2')
            UploadData_2 =  request.FILES.get('upload_docs_2')
            uploadType_3 =  request.POST.get('upload_docs_type_3')
            UploadData_3 =  request.FILES.get('upload_docs_4')
            uploadType_4 =  request.POST.get('upload_docs_type_4')
            UploadData_4 =  request.FILES.get('upload_docs_4')
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(id=int(id))
                userObj = User.objects.get(email = empObj.userFK.email)    
                userObj.username = email
                userObj.email = email
                userObj.set_password(contact)
                if(empType == '1'):
                    userObj.is_staff=True
                else:
                    userObj.is_staff=False
                userObj.save()
                designation_fk = None
                if(current_Designation.strip() != 'null'):
                    designation_fk = designation_Master.objects.get(id=current_Designation)
                employeeType_fk = None
                if(empType != 'null'):
                    employeeType_fk = employeeType_Master.objects.get(id=empType)
                experience_year_fk = None
                if(experience != 'null'):
                    experience_year_fk = experience_Master.objects.get(id=experience)
                empObj.employee_name = fullname
                empObj.employee_id = empID
                empObj.father_name = fathersName
                empObj.state = state
                empObj.city = city
                empObj.pincode = pincode
                empObj.contact = contact
                empObj.alternate_contact = alternateContact
                if(dob != None):
                    empObj.DOB = dob
                empObj.address = address
                empObj.designationFK = designation_fk
                empObj.employeeTypeFK = employeeType_fk
                if(dateOfJoin != None):
                    empObj.joiningDate = dateOfJoin
                empObj.qualification = QualificationDetails
                empObj.experience_year = experience_year_fk
                empObj.work_experience = f"{last_experience} | {Company} | {Duration}"
                if(profilePic != None):
                    empObj.profile_image = profilePic   
                if(uploadType != None):
                    empObj.upload_docs_type = uploadType
                if(UploadData != None):
                    empObj.upload_docs = UploadData
                if(uploadType_1 != None):
                    empObj.upload_docs_type_2 = uploadType_1
                if(UploadData_1 != None):
                    empObj.upload_docs_2 = UploadData_1
                if(uploadType_2 != None):
                    empObj.upload_docs_type_3 = uploadType_2
                if(UploadData_2 != None):
                    empObj.upload_docs_3 = UploadData_2
                if(uploadType_3 != None):
                    empObj.upload_docs_type_4 = uploadType_3
                if(UploadData_3 != None):
                    empObj.upload_docs_4 = UploadData_3
                if(uploadType_4 != None):
                    empObj.upload_docs_type_5 = uploadType_4
                if(UploadData_4 != None):
                    empObj.upload_docs_5 = UploadData_4
                empObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def delete_employee(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.get(id=id)
            user = User.objects.get(email=empObj.userFK.email)
            user.delete()
            return redirect('employee_list')
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def check_emp_email(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchData = request.GET['searchData']
            message = 'success'
            if(User.objects.filter(email=searchData)):
                message = 'User exist'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def check_emp_contact(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchData = request.GET['searchData']
            message = 'success'
            if(employeeDetails.objects.filter(contact=searchData)):
                message = 'User exist'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################################
@login_required(login_url='/')
def update_profile(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            return redirect('/')
        if(request.session['userType'] == 'teacheR'):
            profilePic =  request.FILES.get('profile_image')
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(userFK=request.user)
                empObj.profile_image = profilePic
                empObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'studdenT'):
            profilePic =  request.FILES.get('profile_image')
            message = 'success'
            try:
                empObj = employeeDetails.objects.get(userFK=request.user)
                empObj.profile_image = profilePic
                empObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
    # ##########################################################################################################
@login_required(login_url='/')
def request_edit(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            return redirect('/')
        if(request.session['userType'] == 'teacheR'):
            requestEdit =  request.POST.get('requestEdit')
            message = 'success'
            try:
                empRequestObj = employee_request_edit(userFK=request.user,request_edit = requestEdit)
                empRequestObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'studdenT'):
            requestEdit =  request.POST.get('requestEdit')
            message = 'success'
            try:
                empRequestObj = employee_request_edit(userFK=request.user,request_edit = requestEdit)
                empRequestObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
    # ##########################################################################################################
