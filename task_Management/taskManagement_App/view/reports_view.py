from django.shortcuts import redirect, render
from django.http import HttpResponse
from ..models.master_models import designation_Master, employeeType_Master
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models.project_model import Project_Management,Module_management,Sub_module_management
from ..models.employee_model import employeeDetails
from ..models.master_models import project_sector_Master,project_type_Master,Project_Technology_Master
from ..models.task_model import Task_Management
from django.contrib.auth.models import User
from ..models.leave_model import leave_management,holiday_management,leave_allotment_management
from ..models.events_model import event_bday_annivarsary_management
from ..models.hr_models import job_application

import xlwt
# ##########################################################################################
# EMPLOYEE REPORT
# ##########################################################################################
@login_required(login_url='/')
def employee_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/reports/employee-report.html',{'empObj':empObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# EXPORT EMPLOYEE DATA AS EXCEL
# ##########################################################################################
@login_required(login_url='/')
def download_excel_data(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="Employee_reports.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['S.NO.', 'Employee ID', 'Employee Name', 'Designation', 'Employee Type','Email', 'Contact', 'Alternate Contact', 'DOB',"Father's Name", 'Address', 'Date of Joining' ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
    

	#get your data, from database or from a text file...
	data = employeeDetails.objects.all().order_by('-id')

	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, row_num, font_style)
		ws.write(row_num, 1, "Emp-ID-X0"+str(my_row.id), font_style)
		ws.write(row_num, 2, my_row.employee_name, font_style)
		ws.write(row_num, 3, my_row.designationFK.designation_name, font_style)
		ws.write(row_num, 4, my_row.employeeTypeFK.employee_type_name, font_style)
		ws.write(row_num, 5, my_row.userFK.email, font_style)
		ws.write(row_num, 6, my_row.contact, font_style)
		ws.write(row_num, 7, my_row.alternate_contact, font_style)
		ws.write(row_num, 8, my_row.DOB, font_style)
		ws.write(row_num, 9, my_row.father_name, font_style)
		ws.write(row_num, 10, my_row.address, font_style)
		# ws.write(row_num, 11, my_row.experience_year, font_style)
		ws.write(row_num, 11, my_row.joiningDate, font_style)

	wb.save(response)
	return response
# ##########################################################################################
# HOLIDAY REPORT
# ##########################################################################################
@login_required(login_url='/')
def holiday_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            from datetime import date
            todays_date = date.today()
            holidayObj = holiday_management.objects.filter(holiday_year = todays_date.year)
            return render(request,'admin/reports/holiday-list-report.html',{'holidayObj':holidayObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# PROJECT REPORT
# ##########################################################################################
@login_required(login_url='/')
def project_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')
            for i in projectObj:
                i.moduleCount = len(Module_management.objects.filter(projectFK = i))
            
            for i in projectObj:
                # ==========================================================================================
                # ========================= UPDATE PROJECT (progress & status) =============================
                # ==========================================================================================
                totalTask = Task_Management.objects.filter(projectFK = i)
                compltedTask = Task_Management.objects.filter(projectFK = i,task_status='Done')
                doingTask = Task_Management.objects.filter(projectFK = i,task_status='Doing')
                todoTask = Task_Management.objects.filter(projectFK = i,task_status='To do')

                i.totalTask = len(totalTask)
                if(len(totalTask) != 0):
                    i.project_progress = int(((len(totalTask) - (len(doingTask) + len(todoTask)))/len(totalTask))*100)
                    if(int(int(((len(totalTask) - (len(doingTask) + len(todoTask)))/len(totalTask))*100)) == 100):
                        i.project_status = 'Completed'
                    else:
                        i.project_status = 'Ongoing'
                else:
                   i.project_progress  = int(0)
                   i.project_status = 'Just Created'

                print('due_date >>>> ',i.project_due_date)
                import datetime

                CurrentDate = datetime.datetime.now()
                print(CurrentDate)

                ExpectedDate = str(i.project_due_date)
                print('ExpectedDate >>>> ',ExpectedDate)

                if(ExpectedDate != 'None'):
                    ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%Y-%m-%d")
                print(ExpectedDate)


                if(ExpectedDate != 'None'):
                    if (CurrentDate > ExpectedDate and i.project_progress != 100):
                        i.project_status = 'Delayed'
                    elif(i.project_progress == 0 and len(totalTask) == 0):
                        i.project_status = 'Just Created'
                    elif(i.project_progress != 100):
                        i.project_status = 'Ongoing'
                    else:
                        i.project_status = 'Completed'
                
                else:
                    i.project_status = 'Just Created'

                i.save()
                # ==========================================================================================
                # ==========================================================================================
                teamList = []
                projectManagerData = eval(i.project_manager)
                if(len(projectManagerData) > 0):
                    projectManagerData = projectManagerData[0].split(',')
                print('projectManagerData >>> ',projectManagerData)
                data = ''
                for j in projectManagerData:
                    data = data + str(employeeDetails.objects.get(id=j).employee_name)+', '
                print('data >>> ',data)
                i.projectManagerName = data

                projectTeam = eval(i.project_team_member)
                if(len(projectTeam) > 0):
                    projectTeam = projectTeam[0].split(',')
                for j in projectTeam:
                    context = {}
                    data = employeeDetails.objects.get(id=j)
                    context['empName'] = data.employee_name
                    context['empImg'] = data.profile_image
                    teamList.append(context)

                print('teamList >>> ',teamList)
                i.teamList = teamList

                # ==========================================================================================
                # ==========================================================================================
                project_type = []
                projectTypeData = eval(i.project_type_fk)
                if(len(projectTypeData) > 0):
                    projectTypeData = projectTypeData[0].split(',')
                print('projectTypeData >>> ',projectTypeData)
                data = ''
                for j in projectTypeData:
                    data = data + str(project_type_Master.objects.get(id=j).projectType)+', '
                print('data >>> ',data)
                i.projectTypeName = data

                projectTechData = eval(i.project_technology_fk)
                if(len(projectTechData) > 0):
                    projectTechData = projectTechData[0].split(',')
                print('projectTechData >>> ',projectTechData)
                data = ''
                for j in projectTechData:
                    data = data + str(Project_Technology_Master.objects.get(id=j).Technology)+', '
                print('data >>> ',data)
                i.projectTechName = data

            return render(request,'admin/reports/project-report.html',{'projectObj':projectObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# LEAVE REPORT
# ##########################################################################################
@login_required(login_url='/')
def leave_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            empObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/reports/leave-report.html',{'empObj':empObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# EVENT REPORT
# ##########################################################################################
@login_required(login_url='/')
def event_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            eventObj = event_bday_annivarsary_management.objects.all().order_by('-event_date')
            return render(request,'admin/reports/event-report.html',{'eventObj':eventObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# JOB APPLICATION REPORT
# ##########################################################################################
@login_required(login_url='/')
def job_application_report(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            jobAppObj = job_application.objects.all().order_by('-id')
            return render(request,'admin/reports/job-application-report.html',{'jobAppObj':jobAppObj})
        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')
# ##########################################################################################
# ##########################################################################################
