from django.shortcuts import redirect, render
from django.http import JsonResponse
from taskManagement_App.models.hr_models import jobs,job_application,message_archieve
from ..models.master_models import Location_master, designation_Master, experience_Master,secretKey
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# ##########################################################################################
# RECEIVED APPLICATION LIST
# ##########################################################################################
@login_required(login_url='/')
def received_application_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            applicantObj = job_application.objects.all().order_by('-id')
            hired_applicantObj = job_application.objects.filter(status='Hired').count()
            rejected_applicantObj = job_application.objects.filter(status='Rejected').count()
            absent_applicantObj = job_application.objects.filter(status='Absent').count()
            shortlisted_applicantObj = job_application.objects.filter(status='Shortlisted').count()
            interviewSched_applicantObj = job_application.objects.filter(status='Scheduled').count()
            return render(request,'admin/HR/received-applications.html',{'applicantObj':applicantObj,'hired_applicantObj':hired_applicantObj,'rejected_applicantObj':rejected_applicantObj,'absent_applicantObj':absent_applicantObj,'shortlisted_applicantObj':shortlisted_applicantObj,'interviewSched_applicantObj':interviewSched_applicantObj,})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# ADD NEW APPLICATION
# ##########################################################################################
@login_required(login_url='/')
def add_applications(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = jobs.objects.filter(visibility_status=True).order_by('-id')
            experObj = experience_Master.objects.all().order_by('-id')
            return render(request,'admin/HR/add-applications.html',{'jobObj':jobObj,'experObj':experObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            job_role = request.POST['job_role']
            candidateName = request.POST['candidate_name']
            candidate_email = request.POST['candidate_email']
            candidate_contact = request.POST['candidate_contact']
            candidate_experience = request.POST['candidate_experience']
            hiring_status = request.POST['hiring_status']
            application_date =  request.POST.get('application_date').split('-')
            if(len(application_date) > 1):
                if(application_date[1] == 'Jan'):
                    application_date[1] = 1
                if(application_date[1] == 'Feb'):
                    application_date[1] = 2
                if(application_date[1] == 'Mar'):
                    application_date[1] = 3
                if(application_date[1] == 'Apr'):
                    application_date[1] = 4
                if(application_date[1] == 'May'):
                    application_date[1] = 5
                if(application_date[1] == 'Jun'):
                    application_date[1] = 6
                if(application_date[1] == 'Jul'):
                    application_date[1] = 7
                if(application_date[1] == 'Aug'):
                    application_date[1] = 8
                if(application_date[1] == 'Sep'):
                    application_date[1] = 9
                if(application_date[1] == 'Oct'):
                    application_date[1] = 10
                if(application_date[1] == 'Nov'):
                    application_date[1] = 11
                if(application_date[1] == 'Dec'):
                    application_date[1] = 12
                application_date = f"{application_date[2]}-{application_date[1]}-{application_date[0]}"
            else:
                application_date = None
            candidate_resume = request.FILES.get('candidate_resume')
            message = 'success'
            try:
                jobObj = jobs.objects.get(id=int(job_role))
                expObj = experience_Master.objects.get(id=int(candidate_experience))
                applicationObj = job_application(job_FK = jobObj,
                                                 candidate_name = candidateName,
                                                 email = candidate_email,
                                                 contact = candidate_contact,
                                                 experienceFK = expObj,
                                                 status = hiring_status,
                                                 applicationData = application_date,
                                                 resume_doc = candidate_resume
                                                )
                applicationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# CHANGE JOB APPLICATION STATUS
# ##########################################################################################
@login_required(login_url='/')
def edit_application_status(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            message = 'success'
            try:
                app_status = request.POST['status']
                jobObj = job_application.objects.get(id=int(id))
                message = 'success'
                jobObj.status = app_status
                jobObj.save()
            except:
                message = 'Fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# SCHEDULE JOB INTERVIEW
# ##########################################################################################
@login_required(login_url='/')
def schedule_interview(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            message = 'success'
            try:
                interview_Date =  request.POST.get('interviewDate')
                interviewerName = request.POST['interviewerName']
                import datetime
                interview_Date = datetime.datetime.strptime(str(interview_Date), '%m/%d/%Y').strftime('%Y-%m-%d')
                jobObj = job_application.objects.get(id=int(id))
                message = 'success'
                jobObj.interviewDate = interview_Date
                jobObj.interviewer_name = interviewerName
                jobObj.status = 'Scheduled'
                jobObj.save()
            except:
                message = 'Fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# SEND MESSAGE TO THE APPLICANT
# ##########################################################################################
@login_required(login_url='/')
def send_message(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            message = 'success'
            try:
                jobApplicationObj = job_application.objects.get(id=int(id))
                messageData = request.POST['messageData']
                message = 'success'
                messageObj = message_archieve(applicationFK = jobApplicationObj,message_text = messageData)
                messageObj.save()
            except:
                message = 'Fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# GET JOB APPLICATION INFO
# ##########################################################################################
@login_required(login_url='/')
def get_application_info(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = []
            try:
                jobObj = job_application.objects.get(id=int(id))
                import datetime
                context = {
                    'applicationID':jobObj.id,
                    'role': jobObj.job_FK.position.designation_name,
                    'candidate_name': jobObj.candidate_name,
                    'candidate_email': jobObj.email,
                }
                if(jobObj.interviewDate != None):
                    context['interviewDate'] = datetime.datetime.strptime(str(jobObj.interviewDate), '%Y-%m-%d').strftime('%m/%d/%Y')
                    context['interviewer'] = jobObj.interviewer_name
                else:
                    context['interviewDate'] = ''
                    context['interviewer'] = ''
                data.append(context)
            except:
                data = []
            return JsonResponse({'response':data})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# DELETE APPLICATION
# ##########################################################################################
@login_required(login_url='/')
def delete_application(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = job_application.objects.get(id=int(id))
            jobObj.delete()
            return redirect('received_application_list')
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# JOB LIST
# ##########################################################################################
@login_required(login_url='/')
def job_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = jobs.objects.all().order_by('-id')
            for i in jobObj:
                data = ''
                if(i.job_location != None):
                    locData = i.job_location.split(',')
                    for j in locData:
                        locObj = Location_master.objects.get(id=int(j))
                        data = data + locObj.location +'. '
                else:
                    data = '-'
                i.locations = data
            return render(request,'admin/HR/job-list.html',{'jobObj':jobObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# JOB ENABLE/DISABLE
# ##########################################################################################
@login_required(login_url='/')
def edit_job_visibility(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            message = 'success'
            try:
                status = request.POST['status']
                jobObj = jobs.objects.get(id=int(id))
                message = 'success'
                if(status == 'activate'):
                    jobObj.visibility_status = False
                    jobObj.save()
                elif(status == 'deactivate'):
                    jobObj.visibility_status = True
                    jobObj.save()
                else:
                    message = 'Fail'
            except:
                message = 'Fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# POST NEW JOBS (API)
# ##########################################################################################
@login_required(login_url='/')
def add_new_job(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            designObj = designation_Master.objects.all().order_by('-id')
            locObj = Location_master.objects.all().order_by('-id')
            return render(request,'admin/HR/add-new-job.html',{'designObj':designObj,'locObj':locObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designation = request.POST['profileID']
            jobLocation = request.POST['location']
            job_desc = request.POST['text']
            designObj = designation_Master.objects.get(id=int(designation))
            message = 'success'
            try:
                jobObj = jobs(position=designObj,job_description=job_desc,job_location=jobLocation)
                jobObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# EDIT JOB
# ##########################################################################################
@login_required(login_url='/')
def edit_job_detail(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = jobs.objects.get(id=int(id))
            designObj = designation_Master.objects.all().order_by('-id')
            locObj = Location_master.objects.all().order_by('-id')
            id_data = str(jobObj.position.id)
            if(jobObj.job_location != None):
                locArray = jobObj.job_location.split(',')
            else:
                locArray=[]
            return render(request,'admin/HR/edit-job-detail.html',{'jobObj_id':id_data,'jobObj_data':jobObj.job_description,'designObj':designObj,'locObj':locObj,'locArray':locArray})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designation = request.POST['profileID']
            jobLocation = request.POST['location']
            job_desc = request.POST['text']
            designObj = designation_Master.objects.get(id=int(designation))
            message = 'success'
            try:
                jobObj = jobs.objects.get(id=int(id))
                jobObj.position = designObj
                jobObj.job_location = jobLocation
                jobObj.job_description = job_desc
                jobObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# DELETE JOB
# ##########################################################################################
@login_required(login_url='/')
def delete_job(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = jobs.objects.get(id=int(id))
            jobObj.delete()
            return redirect('job_list')
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# FETCH JOB
# ##########################################################################################
@login_required(login_url='/')
def fetch_job(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = jobs.objects.get(id=int(id))
            jobData = []
            context = {}
            context['position'] = jobObj.position.designation_name
            context['job_desc'] = jobObj.job_description
            jobData.append(context)
            return JsonResponse({'response':jobData})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# SENT MESSAGE ARCHIVES
# ##########################################################################################
@login_required(login_url='/')
def sent_message_archives(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            messageObj = message_archieve.objects.all().order_by('-id')
            return render(request,'admin/HR/message-archive.html',{'messageObj':messageObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# DELETE MESSAGE ARCHIEVE
# ##########################################################################################
@login_required(login_url='/')
def delete_message(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobObj = message_archieve.objects.get(id=int(id))
            jobObj.delete()
            return redirect('sent_message_archives')
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# INTERVIEW ARCHIVES
# ##########################################################################################
@login_required(login_url='/')
def interview_archives(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            applicantObj = job_application.objects.filter(status='Hired').order_by('-id') | job_application.objects.filter(status='Rejected').order_by('-id')
            return render(request,'admin/HR/interview-archive.html',{'applicantObj':applicantObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ###############################################################################################################################################
# ###############################################################################################################################################
# APIS FOR JOBS
# ###############################################################################################################################################
# ###############################################################################################################################################
'''Fetch All active Jobs'''
@api_view(['GET'])
def latest_job_list(request):
    jobObj = jobs.objects.filter(visibility_status=True).order_by('-id')
    data = []
    for i in jobObj:
        locarray = []
        if(i.job_location != None):
            locData = i.job_location.split(',')
            for j in locData:
                locObj = Location_master.objects.get(id=int(j))
                locarray.append(locObj.location)
        i.locations = data
        context = {}
        context['Job_ID'] = i.id
        context['Designation_Name'] = designation_Master.objects.get(id=i.position.id).designation_name
        context['Job_Location'] = locarray
        context['job_description'] = i.job_description
        context['visibility_status'] = i.visibility_status
        data.append(context)
    return JsonResponse({'data':data,'Total_Jobs':len(data),'Status':True})
# ===============================================================================================================================================
# ===============================================================================================================================================
'''Fetch all experience objects from master'''
@api_view(['GET'])
def get_experience(request):
    expObj = experience_Master.objects.all().order_by('id')
    data = []
    for i in expObj:
        context = {}
        context['Experience_ID'] = i.id
        context['Experience'] = i.experience
        data.append(context)
    return JsonResponse({'data':data,'Total_Records':len(data),'Status':True})
# ===============================================================================================================================================
# ===============================================================================================================================================
'''add job application from 18 pixels website
1. Job ID (ID)
2. Applicant Name
3. Applicant Email
4. Applicant Mobile
5. Applicant Experience (ID)
6. Resume Doc (File :{doc/pdf})
'''
from datetime import date
@api_view(['POST'])
@csrf_exempt
def job_application_apply(request):
    formData = request.data
    try:
        secret_token = request.headers['Authorization'].split(' ')[1]
        if(secretKey.objects.filter(secret_key = secret_token)): 
            try:
                jobID = formData['job_id']
                app_name = formData['applicant_name']
                app_email = formData['applicant_email']
                app_contact = formData['applicant_contact']
                app_experience = formData['applicant_experience']
                resume = formData['resume']
                try:
                    jobObj = jobs.objects.get(id=int(jobID))
                except:
                    return JsonResponse({'Error' : 'Invalid Job ID.','Status':False})
                try:
                    expObj = experience_Master.objects.get(id=int(app_experience))
                except:
                    return JsonResponse({'Error' : 'Invalid Experience.','Status':False})
                if(job_application.objects.filter(job_FK = jobObj,email = app_email,contact = app_contact)):
                    status = job_application.objects.filter(job_FK = jobObj,email = app_email,contact = app_contact)[0].status
                    return JsonResponse({'Message' : 'Already Applied for this Role.','Application Status' : status,'Status':False})
                if(job_application.objects.filter(job_FK = jobObj,email = app_email)):
                    status = job_application.objects.filter(job_FK = jobObj,email = app_email)[0].status
                    return JsonResponse({'Message' : 'Already Applied for this Role.','Application Status' : status,'Status':False})
                if(job_application.objects.filter(job_FK = jobObj,contact = app_contact)):
                    status = job_application.objects.filter(job_FK = jobObj,contact = app_contact)[0].status
                    return JsonResponse({'Message' : 'Already Applied for this Role.','Application Status' : status,'Status':False})
                try:
                    jobApplicationObj = job_application(job_FK = jobObj,
                                                        candidate_name = app_name,
                                                        email = app_email,
                                                        contact = app_contact,
                                                        experienceFK = expObj,
                                                        applicationData = date.today(),
                                                        resume_doc = resume
                                                        )
                    jobApplicationObj.save()
                    return JsonResponse({'Message':"Application saved successfully.Our HR department will contact you Soon.",'Status':True})
                except:
                    return JsonResponse({'Message' : 'API FAILED. Contact Developer','Status':False})
            except KeyError as e:
                return JsonResponse({'Error' : str(e) + " Key Missing.",'Status':False})
        else:
            return JsonResponse({'Error' : 'Invalid Authorization Key.','Status':False})
    except KeyError as e:
        return JsonResponse({'Error' : 'Authorization Key Missing.','Status':False})
# ###############################################################################################################################################
# ###############################################################################################################################################
