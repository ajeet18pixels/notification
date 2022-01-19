import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ..models.master_models import designation_Master
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models.project_model import Project_Management,Module_management,Sub_module_management
from ..models.employee_model import employeeDetails
from ..models.master_models import project_sector_Master,project_type_Master,Project_Technology_Master
from ..models.task_model import Task_Management
import datetime 
from django.contrib.auth.models import User
from taskManagement_App.models.notification_model import Notification_Management

# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           Tasks List (ToDo/ Doing/ Done)
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def task_management(request):
    if request.method == 'GET':
        # #######################################################################################################################
        # #######################################################################################################################
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')

            todoTaskObj = Task_Management.objects.filter(task_status = 'To do').order_by('-id')
            for i in todoTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            doingTaskObj = Task_Management.objects.filter(task_status = 'Doing').order_by('-id')
            for i in doingTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            reviewTaskObj = Task_Management.objects.filter(task_status = 'Review').order_by('-id')
            for i in reviewTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            doneTaskObj = Task_Management.objects.filter(task_status = 'Done').order_by('-id')
            for i in doneTaskObj:
                dueData = str(i.due_date).split('-')
                print('due date >>> ',dueData)
                # ----------------------------------------------------------------------------------
                month = ''
                status = ''
                # ----------------------------------------------------------------------------------
                from datetime import date
                todays_date = i.completed_at
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

                if(int(dueData[2]) == int(datetime.datetime.now().day) and int(dueData[1]) == int(datetime.datetime.now().month) and int(dueData[0]) == int(datetime.datetime.now().year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
                
            return render(request,'admin/task/tasks-list.html',{'projectObj':projectObj,'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj,'todoTaskObj':todoTaskObj,'doingTaskObj':doingTaskObj,'reviewTaskObj':reviewTaskObj,'doneTaskObj':doneTaskObj})
        # #######################################################################################################################
        # #######################################################################################################################
        if(request.session['userType'] == 'teacheR'):
            user_FK = User.objects.get(email=request.user)
            print('userFK >>> ',user_FK)

            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            print('employeeFk >>> ',employeeFk,employeeFk.id)

            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))
            print('projectObj >>> ',projectObj)

            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')


            todoTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'To do').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'To do').order_by('-id')
            doingTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Doing').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Doing').order_by('-id')
            reviewTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Review').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Review').order_by('-id')
            doneTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Done').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Done').order_by('-id')

            # ======================================================================
            # todoTaskObj = Task_Management.objects.filter(task_status = 'To do').order_by('-id')
            for i in todoTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # doingTaskObj = Task_Management.objects.filter(task_status = 'Doing').order_by('-id')
            for i in doingTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # reviewTaskObj = Task_Management.objects.filter(task_status = 'Review').order_by('-id')
            for i in reviewTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            # doneTaskObj = Task_Management.objects.filter(task_status = 'Done').order_by('-id')
            for i in doneTaskObj:
                dueData = str(i.due_date).split('-')
                print('due date >>> ',dueData)
                # ----------------------------------------------------------------------------------
                month = ''
                status = ''
                # ----------------------------------------------------------------------------------
                from datetime import date
                todays_date = i.completed_at
                # print('todays_date.day >>>> ',todays_date.day)
                print('todays_date.day >>>> ',i.completed_at)


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
                    print('=========================================================================================================================')
                    print('=========================================================================================================================')
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
                    i.due_date = new_format
                    print('=========================================================================================================================')
                    print('=========================================================================================================================')


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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # ======================================================================
            return render(request,'admin/task/tasks-list.html',{'projectObj':projectObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj,'todoTaskObj':todoTaskObj,'doingTaskObj':doingTaskObj,'reviewTaskObj':reviewTaskObj,'doneTaskObj':doneTaskObj})
        # #######################################################################################################################
        # #######################################################################################################################
        if(request.session['userType'] == 'studdenT'):
            user_FK = User.objects.get(email=request.user)
            print('userFK >>> ',user_FK)

            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            print('employeeFk >>> ',employeeFk,employeeFk.id)

            projectObj = Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))
            print('projectObj >>> ',projectObj)

            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')


            todoTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'To do').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'To do').order_by('-id')
            doingTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Doing').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Doing').order_by('-id')
            reviewTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Review').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Review').order_by('-id')
            doneTaskObj = Task_Management.objects.filter(employeeFK=employeeFk,task_status = 'Done').order_by('-id')| Task_Management.objects.filter(created_by_user_email = request.user,task_status = 'Done').order_by('-id')

            # ======================================================================
            # todoTaskObj = Task_Management.objects.filter(task_status = 'To do').order_by('-id')
            for i in todoTaskObj:
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # doingTaskObj = Task_Management.objects.filter(task_status = 'Doing').order_by('-id')
            for i in doingTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # reviewTaskObj = Task_Management.objects.filter(task_status = 'Review').order_by('-id')
            for i in reviewTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            # doneTaskObj = Task_Management.objects.filter(task_status = 'Done').order_by('-id')
            for i in doneTaskObj:
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

                if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
                    new_format = 'Today'
                    i.status = 'today'
                    if(int(current_time.hour) > int(timeHr[0])):
                        i.status = 'delay'                        
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
                    i.delayed_by = diff.days                      
                    i.due_date = new_format
                # ----------------------------------------------------------------------------------
            # ======================================================================
            
            return render(request,'admin/task/tasks-list.html',{'projectObj':projectObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj,'todoTaskObj':todoTaskObj,'doingTaskObj':doingTaskObj,'doneTaskObj':doneTaskObj,'reviewTaskObj':reviewTaskObj,'employeeFk':employeeFk})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           Add New Tasks
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________

@login_required(login_url='/')
def add_task(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            projectFk = request.POST['projectFk']
            moduleFk = request.POST['moduleFk']
            subModuleFk = request.POST.get('subModuleFk')
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            employeeFK = request.POST['employeeFK']
            taskDescription = request.POST['taskDescription']

            message = 'success'
            print('subModuleFk >>> ',subModuleFk)
            try:
                projectObj = Project_Management.objects.get(id=int(projectFk))
                moduleObbj = Module_management.objects.get(id=int(moduleFk))
                if(subModuleFk!=''):
                    subModuleObj = Sub_module_management.objects.get(id=int(subModuleFk))
                else:
                    subModuleObj = None
                empObj = employeeDetails.objects.get(id=int(employeeFK))

                Task_ManagementObj = Task_Management(
                    task_title = taskTitle,
                    task_description = taskDescription,
                    projectFK = projectObj,
                    moduleFK = moduleObbj,
                    submoduleFK = subModuleObj,
                    employeeFK = empObj,
                    due_date = datetime.datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d'),
                    due_time = dueTime,
                    priority = priority,
                    created_by = 'Admin',
                    created_by_user_email = request.user
                )
                Task_ManagementObj.save()

                # ######################################################################################################################
                # new notification for newly added task by the admin
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=empObj.userFK,notification_from=request.user,
                                                            notification_subject='New task Assigned.',notification_message='Admin added new task for project : '+projectObj.project_name+' .Check the assigned task and finish it before given deadline for ontime delivery of the product.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            projectFk = request.POST['projectFk']
            moduleFk = request.POST['moduleFk']
            subModuleFk = request.POST.get('subModuleFk')
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            employeeFK = request.POST['employeeFK']
            taskDescription = request.POST['taskDescription']

            message = 'success'
            try:
                projectObj = Project_Management.objects.get(id=int(projectFk))
                moduleObbj = Module_management.objects.get(id=int(moduleFk))
                if(subModuleFk!=''):
                    subModuleObj = Sub_module_management.objects.get(id=int(subModuleFk))
                else:
                    subModuleObj = None
                empObj = employeeDetails.objects.get(id=int(employeeFK))

                Task_ManagementObj = Task_Management(
                    task_title = taskTitle,
                    task_description = taskDescription,
                    projectFK = projectObj,
                    moduleFK = moduleObbj,
                    submoduleFK = subModuleObj,
                    employeeFK = empObj,
                    due_date = datetime.datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d'),
                    due_time = dueTime,
                    priority = priority,
                    created_by = 'Manager',
                    created_by_user_email = request.user
                )
                Task_ManagementObj.save()

                if(empObj.userFK == request.user):
                    # ######################################################################################################################
                    # new notification for newly added task by the manager
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=User.objects.get(username='admin@gmail.com'),notification_from=request.user,
                                                                notification_subject=f'New task Added by {empObj.employee_name}.',
                                                                notification_message=f'{empObj.employee_name} added new task for project : {projectObj.project_name}.\n\n\nThank You'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                else:
                    # ######################################################################################################################
                    # new notification for newly added task by the manager to employee
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=empObj.userFK,notification_from=request.user,
                                                                notification_subject=f'New task Assigned by Manager,{request.user.first_name}.',
                                                                notification_message='Manager added new task for project : '+projectObj.project_name+' .Check the assigned task and finish it before given deadline for ontime delivery of the product.\n\n\nThank You'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################


            except:
                message = 'fail'
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            projectFk = request.POST['projectFk']
            moduleFk = request.POST['moduleFk']
            subModuleFk = request.POST.get('subModuleFk')
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            employeeFK = request.POST['employeeFK']
            taskDescription = request.POST['taskDescription']

            message = 'success'
            try:
                projectObj = Project_Management.objects.get(id=int(projectFk))
                moduleObbj = Module_management.objects.get(id=int(moduleFk))
                if(subModuleFk!=''):
                    subModuleObj = Sub_module_management.objects.get(id=int(subModuleFk))
                else:
                    subModuleObj = None
                userObj = User.objects.get(email=request.user.email)
                empObj = employeeDetails.objects.get(userFK=userObj)

                Task_ManagementObj = Task_Management(
                    task_title = taskTitle,
                    task_description = taskDescription,
                    projectFK = projectObj,
                    moduleFK = moduleObbj,
                    submoduleFK = subModuleObj,
                    employeeFK = empObj,
                    due_date = datetime.datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d'),
                    due_time = dueTime,
                    priority = priority,
                    created_by = 'Employee',
                    created_by_user_email = request.user
                )
                Task_ManagementObj.save()

                if(empObj.userFK == request.user):
                    # ######################################################################################################################
                    # new notification for newly added task by the employee
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=User.objects.get(username='admin@gmail.com'),notification_from=request.user,
                                                                notification_subject=f'New task Added by {empObj.employee_name}.',
                                                                notification_message=f'{empObj.employee_name} added new task for project : {projectObj.project_name}.\n\n\nThank You'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           GET PROJECT WISE MODULE and EMPLOYEE LIST
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def get_project_module_employee_list(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            project_fk = Project_Management.objects.get(id=int(id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []

            for i in moduleObj:
                context = {}
                context['id'] = i.id
                context['moduleName'] = i.moduleName
                context['moduleDescription'] = i.module_desc
                context['projectName'] = project_fk.project_name

                listObj.append(context)
            # empList =eval(project_fk.project_team_member)[0].split(',')
            managerList =eval(project_fk.project_manager)[0].split(',')
            empList = []

            empArray = set(empList + managerList)

            print('empArray >>> ',empArray)

            empDataArray = []
            for e in empArray:
                con = {}
                data = employeeDetails.objects.get(id=int(e))
                con['id'] = data.id
                con['emp_name'] = data.employee_name
                empDataArray.append(con)

            return JsonResponse({'response':listObj,'empDataArray':empDataArray,'userType':'Admin'})

        if(request.session['userType'] == 'teacheR'):
            project_fk = Project_Management.objects.get(id=int(id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []
            for i in moduleObj:
                context = {}
                context['id'] = i.id
                context['moduleName'] = i.moduleName
                context['moduleDescription'] = i.module_desc
                context['projectName'] = project_fk.project_name

                listObj.append(context)
            empList =eval(project_fk.project_team_member)[0].split(',')
            managerList =eval(project_fk.project_manager)[0].split(',')

            empArray = set(empList + managerList)

            print('empArray >>> ',empArray)

            empDataArray = []
            for e in empArray:
                con = {}
                data = employeeDetails.objects.get(id=int(e))
                con['id'] = data.id
                con['emp_name'] = data.employee_name
                empDataArray.append(con)
            return JsonResponse({'response':listObj,'empDataArray':empDataArray,'userType':'Manager'})
            
        if(request.session['userType'] == 'studdenT'):
            project_fk = Project_Management.objects.get(id=int(id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []
            for i in moduleObj:
                context = {}
                context['id'] = i.id
                context['moduleName'] = i.moduleName
                context['moduleDescription'] = i.module_desc
                context['projectName'] = project_fk.project_name

                listObj.append(context)
            # empList =eval(project_fk.project_team_member)[0].split(',')
            # managerList =eval(project_fk.project_manager)[0].split(',')

            # empArray = set(empList + managerList)

            # print('empArray >>> ',empArray)

            empDataArray = []
            # for e in empArray:
            #     con = {}
            #     data = employeeDetails.objects.get(id=int(e))
            #     con['id'] = data.id
            #     con['emp_name'] = data.employee_name
            #     empDataArray.append(con)
            
            userObj = User.objects.get(email=request.user.email)
            empObject = employeeDetails.objects.get(userFK=userObj)
            userDataArray = {}
            userDataArray['userID'] = empObject.id
            userDataArray['userName'] = empObject.employee_name
            return JsonResponse({'response':listObj,'empDataArray':empDataArray,'userType':'Employee','userDataArray':userDataArray})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           UPDATE TASk STATUS
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def update_task_status(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            taskID = request.POST['taskID']
            taskStatus = request.POST['taskStatus']

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                taskObj.task_status = taskStatus
                if(taskStatus == 'Done'):
                    # =========================================================
                    dueData = str(taskObj.due_date).split('-')
                    # ----------------------------------------------------------------------------------
                    month = ''
                    status = ''
                    # ----------------------------------------------------------------------------------
                    from datetime import date
                    todays_date = date.today()
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
                    timeHr = str(taskObj.due_time).split(':')
                    current_time = datetime.datetime.now() 

                    from datetime import datetime
                    if(dueData[2] < str(todays_date.day) and dueData[1] == str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = str(taskObj.due_date) 
                        date_2 = str(todays_date)
                        start = datetime.strptime(date_1, "%Y-%m-%d")
                        end =   datetime.strptime(date_2, "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] <= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] >= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = todays_date
                        taskObj.delayed_by_diff = diff.days
                    
                    if(dueData[2] >= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] >= str(todays_date.day) and dueData[1] >= str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        print('date 1 >>> ',date_1)
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)
                        # =========================================================
                        taskObj.completed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                elif(taskStatus == 'Review'):
                    # =========================================================
                    dueData = str(taskObj.due_date).split('-')
                    # ----------------------------------------------------------------------------------
                    month = ''
                    status = ''
                    # ----------------------------------------------------------------------------------
                    from datetime import date
                    todays_date = date.today()
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
                    timeHr = str(taskObj.due_time).split(':')
                    current_time = datetime.datetime.now() 

                    from datetime import datetime
                    if(dueData[2] < str(todays_date.day) and dueData[1] == str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = str(taskObj.due_date) 
                        date_2 = str(todays_date)
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = None
                        taskObj.reviewed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] <= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = None
                        taskObj.reviewed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] >= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = None
                        taskObj.reviewed_at = todays_date
                        taskObj.delayed_by_diff = diff.days
                    
                    if(dueData[2] >= str(todays_date.day) and dueData[1] < str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)

                        taskObj.completed_at = None
                        taskObj.reviewed_at = todays_date
                        taskObj.delayed_by_diff = diff.days

                    if(dueData[2] >= str(todays_date.day) and dueData[1] >= str(todays_date.month)):
                        new_format = taskObj.due_date 
                        # ---------------------------------
                        date_1 = taskObj.due_date 
                        print('date 1 >>> ',date_1)
                        date_2 = todays_date
                        start = datetime.strptime(str(date_1), "%Y-%m-%d")
                        end =   datetime.strptime(str(date_2), "%Y-%m-%d")
                        # get the difference between wo dates as timedelta object
                        diff = end.date() - start.date()
                        print('Difference between dates in days:')
                        print(diff.days)
                        # =========================================================
                        taskObj.completed_at = None
                        taskObj.reviewed_at = todays_date
                        taskObj.delayed_by_diff = diff.days
                        # else:
                        #     taskObj.completed_at = todays_date
                        #     taskObj.delayed_by_diff = None
                else:
                    taskObj.completed_at = None
                    taskObj.reviewed_at = None
                    taskObj.delayed_by_diff = None
                from datetime import date,datetime
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()
            except:
                message = 'fail'

            return JsonResponse({'response':message})

        # ###################################################################################
        if(request.session['userType'] == 'teacheR'):
            taskID = request.POST['taskID']
            taskStatus = request.POST['taskStatus']

            message = 'success'
            try:
                from datetime import date
                todays_date = date.today()
                taskObj = Task_Management.objects.get(id=int(taskID))
                print('created_by >>> ',taskObj.created_by)
                print('created_by_user_email >>> ',taskObj.created_by_user_email)
                print('user.email >>> ',request.user.email)
                print('employee email >>> ',taskObj.employeeFK.userFK.email)

                if(taskStatus == 'Done'):
                    if(taskObj.created_by == 'Admin'):
                        taskObj.task_status = taskStatus
                        taskObj.updated_by = 'Manager'
                        taskObj.updated_by_user_email = request.user.email
                        taskObj.completed_at = todays_date
                        taskObj.save()
                        return JsonResponse({'response':message})
                        # return JsonResponse({'response':'You are not authorized to change Task Status to Done!'})


                if(taskObj.created_by == 'Manager' and taskObj.created_by_user_email == request.user.email):
                    print('======================== 01')
                    taskObj.task_status = taskStatus
                    taskObj.updated_by = 'Manager'
                    taskObj.updated_by_user_email = request.user.email
                    taskObj.completed_at = todays_date
                    from datetime import date,datetime
                    todays_date = date.today()
                    taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                    taskObj.save()
                    return JsonResponse({'response':message})

                elif(taskObj.created_by == 'Admin' and taskObj.employeeFK.userFK.email == request.user.email):
                    print('======================== 02')
                    taskObj.task_status = taskStatus
                    taskObj.updated_by = 'Manager'
                    taskObj.updated_by_user_email = request.user.email
                    taskObj.completed_at = todays_date
                    from datetime import date,datetime
                    todays_date = date.today()
                    taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                    taskObj.save()
                    return JsonResponse({'response':message})

                elif(taskObj.created_by == 'Manager' and taskObj.created_by_user_email != request.user.email):
                    print('======================== 03')
                    taskObj.task_status = taskStatus
                    taskObj.updated_by = 'Manager'
                    taskObj.updated_by_user_email = request.user.email
                    taskObj.completed_at = todays_date
                    from datetime import date,datetime
                    todays_date = date.today()
                    taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                    taskObj.save()
                    return JsonResponse({'response':message})
                    # return JsonResponse({'response':'You are not authorized to change Task Status!'})
                
                elif(taskObj.created_by == 'Admin' or taskObj.created_by == 'Employee'):
                    print('======================== 04')
                    taskObj.task_status = taskStatus
                    taskObj.updated_by = 'Manager'
                    taskObj.updated_by_user_email = request.user.email
                    taskObj.completed_at = todays_date
                    from datetime import date,datetime
                    todays_date = date.today()
                    taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                    taskObj.save()
                    return JsonResponse({'response':message})
                    # return JsonResponse({'response':'You are not authorized to change Task Status!'})

            except:
                message = 'fail'
            
            
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            taskID = request.POST['taskID']
            taskStatus = request.POST['taskStatus']

            message = 'success'
            try:
                from datetime import date
                todays_date = date.today()
                taskObj = Task_Management.objects.get(id=int(taskID))
                if(taskStatus == 'Done'):
                    print('======================== 04')
                    taskObj.task_status = taskStatus
                    taskObj.updated_by = 'Manager'
                    taskObj.updated_by_user_email = request.user.email
                    taskObj.completed_at = todays_date
                    from datetime import date,datetime
                    todays_date = date.today()
                    taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                    taskObj.save()
                    return JsonResponse({'response':message})
                    # return JsonResponse({'response':'You are not authorized to change Task Status to Done!'})

                taskObj.task_status = taskStatus
                taskObj.updated_by = 'Employee'
                taskObj.updated_by_user_email = request.user.email
                taskObj.completed_at = todays_date
                from datetime import date,datetime
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()
                return JsonResponse({'response':message})

            except:
                message = 'fail'
                return JsonResponse({'response':message})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           GET SPECIFIC TASK DETAILS
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def get_task_details(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):

            message = 'success'
            taskList =  []
            context = {}
            # try:
            taskData = Task_Management.objects.get(id=int(id))

            context['id'] = taskData.id
            context['task_title'] = taskData.task_title
            context['task_description'] = taskData.task_description


            context['projectFK'] = taskData.projectFK.id
            # ==================================================================================
            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []

            for i in moduleObj:
                context1 = {}
                context1['id'] = i.id
                context1['moduleName'] = i.moduleName
                context1['moduleDescription'] = i.module_desc
                context1['projectName'] = project_fk.project_name

                listObj.append(context1)
            empList =eval(project_fk.project_team_member)[0].split(',')
            managerList =eval(project_fk.project_manager)[0].split(',')

            empArray = set(empList + managerList)

            print('empArray >>> ',empArray)

            empDataArray = []
            for e in empArray:
                con = {}
                data = employeeDetails.objects.get(id=int(e))
                con['id'] = data.id
                con['emp_name'] = data.employee_name
                empDataArray.append(con)
            # ==================================================================================
            context['projectData'] = taskData.projectFK.project_name

            context['moduleFK'] = taskData.moduleFK.moduleName
            if(taskData.submoduleFK == None):
                context['submoduleFK'] = '-'
                context['submoduleID'] = '-'
            else:
                context['submoduleID'] = taskData.submoduleFK.id
                context['submoduleFK'] = taskData.submoduleFK.subModuleName
            context['employeeFK'] = taskData.employeeFK.employee_name
            context['empID'] = taskData.employeeFK.id

            # context['employeePic'] = taskData.employeeFK.profile_image


            dueData = str(taskData.due_date).split('-')
            # new_format = dueData.strftime('%m-%b-%y')
            month = ''
            # ----------------------------------------------------------------------------------
            # importing date class from datetime module
            from datetime import date
            
            # creating the date object of today's date
            todays_date = date.today()
            
            # printing todays date
            print("Current date: ", todays_date)
            
            # fetching the current year, month and day of today
            print("Current year:", todays_date.year)
            print("Current month:", todays_date.month)
            print("Current day:", todays_date.day)
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

            new_format = dueData[2]+'-'+month
            # ----------------------------------------------------------------------------------
            # check for Today date format
            if(dueData[2] == str(todays_date.day) and dueData[1] == str(todays_date.month) and dueData[0] == str(todays_date.year)):
                new_format = 'Today'

            # check for Tommorow date format
            import datetime
            NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
            print (NextDay_Date)
            if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
                new_format = 'Tommorow'
            
            # check for yesterday date format
            # import datetime
            # NextDay_Date = datetime.datetime.today() - datetime.timedelta(days=1)
            # print (NextDay_Date)
            # if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
            #     new_format = 'Delay'
            # ----------------------------------------------------------------------------------

            print('new_format >>> ',dueData)
            print('new_format >>> ',new_format)


            context['due_date'] = new_format

            context['review_date'] = taskData.reviewed_at
            context['completion_date'] = taskData.completed_at


            context['due_date_original'] = datetime.datetime.strptime(str(taskData.due_date), '%Y-%m-%d').strftime('%m/%d/%Y')
            context['due_time_original'] = taskData.due_time


            context['due_time'] = taskData.due_time.strftime("%I:%M %p")
            context['priority'] = taskData.priority
            context['task_status'] = taskData.task_status
            context['dependencies'] = taskData.dependencies

            created_at_date = taskData.created_at.strftime('%d-%b-%y')
            updated_at_date = taskData.updated_at.strftime('%d-%b-%y')

            # ================================================================
            print('data 1>>> ',created_at_date, updated_at_date)

            # print(taskData.due_time.strftime("%I:%M %p"))
            # ================================================================

            context['created_at'] = created_at_date
            context['updated_at'] = updated_at_date
            taskList.append(context)

            # except:
            #     taskList =  []

            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.get(id = int(taskData.moduleFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)


            listObj1 = []
            for i in subModule_obj:
                context2 = {}
                context2['mod_id'] = i.moduleFK.id
                context2['mod_name'] = i.moduleFK.moduleName.capitalize()
                context2['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context2['subMod_id'] = i.id
                context2['subModuleName'] = i.subModuleName.capitalize()
                context2['subModuleDescription'] = i.subModule_desc.capitalize()
                context2['projectName'] = project_fk.project_name.capitalize()
                context2['projectid'] = project_fk.id


                listObj1.append(context2)


            return JsonResponse({'response':context,'projectData':listObj,'empDataArray':empDataArray,'subModuleData':listObj1,'userType':'Admin'})

        if(request.session['userType'] == 'teacheR'):
            message = 'success'
            taskList =  []
            context = {}
            # try:
            taskData = Task_Management.objects.get(id=int(id))

            context['id'] = taskData.id
            context['task_title'] = taskData.task_title
            context['task_description'] = taskData.task_description


            context['projectFK'] = taskData.projectFK.id
            # ==================================================================================
            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []

            for i in moduleObj:
                context1 = {}
                context1['id'] = i.id
                context1['moduleName'] = i.moduleName
                context1['moduleDescription'] = i.module_desc
                context1['projectName'] = project_fk.project_name

                listObj.append(context1)
            empList =eval(project_fk.project_team_member)[0].split(',')
            managerList =eval(project_fk.project_manager)[0].split(',')

            empArray = set(empList + managerList)

            print('empArray >>> ',empArray)

            empDataArray = []
            for e in empArray:
                con = {}
                data = employeeDetails.objects.get(id=int(e))
                con['id'] = data.id
                con['emp_name'] = data.employee_name
                empDataArray.append(con)
            # ==================================================================================
            context['projectData'] = taskData.projectFK.project_name

            context['moduleFK'] = taskData.moduleFK.moduleName
            if(taskData.submoduleFK == None):
                context['submoduleFK'] = '-'
                context['submoduleID'] = '-'
            else:
                context['submoduleID'] = taskData.submoduleFK.id
                context['submoduleFK'] = taskData.submoduleFK.subModuleName
            context['employeeFK'] = taskData.employeeFK.employee_name
            context['empID'] = taskData.employeeFK.id

            # context['employeePic'] = taskData.employeeFK.profile_image


            dueData = str(taskData.due_date).split('-')
            # new_format = dueData.strftime('%m-%b-%y')
            month = ''
            # ----------------------------------------------------------------------------------
            # importing date class from datetime module
            from datetime import date
            
            # creating the date object of today's date
            todays_date = date.today()
            
            # printing todays date
            print("Current date: ", todays_date)
            
            # fetching the current year, month and day of today
            print("Current year:", todays_date.year)
            print("Current month:", todays_date.month)
            print("Current day:", todays_date.day)
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

            new_format = dueData[2]+'-'+month
            # ----------------------------------------------------------------------------------
            # check for Today date format
            if(dueData[2] == str(todays_date.day) and dueData[1] == str(todays_date.month) and dueData[0] == str(todays_date.year)):
                new_format = 'Today'

            # check for Tommorow date format
            import datetime
            NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
            print (NextDay_Date)
            if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
                new_format = 'Tommorow'
            
            # check for yesterday date format
            # import datetime
            # NextDay_Date = datetime.datetime.today() - datetime.timedelta(days=1)
            # print (NextDay_Date)
            # if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
            #     new_format = 'Delay'
            # ----------------------------------------------------------------------------------

            print('new_format >>> ',dueData)
            print('new_format >>> ',new_format)


            context['due_date'] = new_format
            context['review_date'] = taskData.reviewed_at
            context['completion_date'] = taskData.completed_at

            context['due_date_original'] = datetime.datetime.strptime(str(taskData.due_date), '%Y-%m-%d').strftime('%m/%d/%Y')
            context['due_time_original'] = taskData.due_time


            context['due_time'] = taskData.due_time.strftime("%I:%M %p")
            context['priority'] = taskData.priority
            context['task_status'] = taskData.task_status
            context['dependencies'] = taskData.dependencies

            new_format1 = taskData.created_at.strftime('%m-%b-%y')
            new_format2 = taskData.updated_at.strftime('%m-%b-%y')

            # ================================================================
            print('data >>> ',new_format == new_format1,new_format == new_format2)
            print('data 1>>> ',new_format, new_format1,new_format2)

            # print(taskData.due_time.strftime("%I:%M %p"))
            # ================================================================

            context['created_at'] = new_format1
            context['updated_at'] = new_format2
            taskList.append(context)

            # except:
            #     taskList =  []

            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.get(id = int(taskData.moduleFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)


            listObj1 = []
            for i in subModule_obj:
                context2 = {}
                context2['mod_id'] = i.moduleFK.id
                context2['mod_name'] = i.moduleFK.moduleName.capitalize()
                context2['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context2['subMod_id'] = i.id
                context2['subModuleName'] = i.subModuleName.capitalize()
                context2['subModuleDescription'] = i.subModule_desc.capitalize()
                context2['projectName'] = project_fk.project_name.capitalize()
                context2['projectid'] = project_fk.id


                listObj1.append(context2)

            
            return JsonResponse({'response':context,'projectData':listObj,'empDataArray':empDataArray,'subModuleData':listObj1,'userType':'Manager'})
            
        if(request.session['userType'] == 'studdenT'):
            message = 'success'
            taskList =  []
            context = {}
            # try:
            taskData = Task_Management.objects.get(id=int(id))

            context['id'] = taskData.id
            context['task_title'] = taskData.task_title
            context['task_description'] = taskData.task_description


            context['projectFK'] = taskData.projectFK.id
            # ==================================================================================
            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.filter(projectFK = project_fk)
            listObj = []

            for i in moduleObj:
                context1 = {}
                context1['id'] = i.id
                context1['moduleName'] = i.moduleName
                context1['moduleDescription'] = i.module_desc
                context1['projectName'] = project_fk.project_name

                listObj.append(context1)
            empList =eval(project_fk.project_team_member)[0].split(',')
            managerList =eval(project_fk.project_manager)[0].split(',')

            empArray = set(empList + managerList)

            print('empArray >>> ',empArray)

            empDataArray = []
            for e in empArray:
                con = {}
                data = employeeDetails.objects.get(id=int(e))
                con['id'] = data.id
                con['emp_name'] = data.employee_name
                empDataArray.append(con)
            # ==================================================================================
            context['projectData'] = taskData.projectFK.project_name

            context['moduleFK'] = taskData.moduleFK.moduleName
            if(taskData.submoduleFK == None):
                context['submoduleFK'] = '-'
                context['submoduleID'] = '-'
            else:
                context['submoduleID'] = taskData.submoduleFK.id
                context['submoduleFK'] = taskData.submoduleFK.subModuleName
            context['employeeFK'] = taskData.employeeFK.employee_name
            context['empID'] = taskData.employeeFK.id

            # context['employeePic'] = taskData.employeeFK.profile_image


            dueData = str(taskData.due_date).split('-')
            # new_format = dueData.strftime('%m-%b-%y')
            month = ''
            # ----------------------------------------------------------------------------------
            # importing date class from datetime module
            from datetime import date
            
            # creating the date object of today's date
            todays_date = date.today()
            
            # printing todays date
            print("Current date: ", todays_date)
            
            # fetching the current year, month and day of today
            print("Current year:", todays_date.year)
            print("Current month:", todays_date.month)
            print("Current day:", todays_date.day)
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

            new_format = dueData[2]+'-'+month
            # ----------------------------------------------------------------------------------
            # check for Today date format
            if(dueData[2] == str(todays_date.day) and dueData[1] == str(todays_date.month) and dueData[0] == str(todays_date.year)):
                new_format = 'Today'

            # check for Tommorow date format
            import datetime
            NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
            print (NextDay_Date)
            if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
                new_format = 'Tommorow'
            
            # check for yesterday date format
            # import datetime
            # NextDay_Date = datetime.datetime.today() - datetime.timedelta(days=1)
            # print (NextDay_Date)
            # if(dueData[2] == str(NextDay_Date.day) and dueData[1] == str(NextDay_Date.month) and dueData[0] == str(NextDay_Date.year)):
            #     new_format = 'Delay'
            # ----------------------------------------------------------------------------------

            print('new_format >>> ',dueData)
            print('new_format >>> ',new_format)


            context['due_date'] = new_format
            context['review_date'] = taskData.reviewed_at
            context['completion_date'] = taskData.completed_at

            context['due_date_original'] = datetime.datetime.strptime(str(taskData.due_date), '%Y-%m-%d').strftime('%m/%d/%Y')
            context['due_time_original'] = taskData.due_time


            context['due_time'] = taskData.due_time.strftime("%I:%M %p")
            context['priority'] = taskData.priority
            context['task_status'] = taskData.task_status
            context['dependencies'] = taskData.dependencies

            new_format1 = taskData.created_at.strftime('%m-%b-%y')
            new_format2 = taskData.updated_at.strftime('%m-%b-%y')

            # ================================================================
            print('data >>> ',new_format == new_format1,new_format == new_format2)
            print('data 1>>> ',new_format, new_format1,new_format2)

            # print(taskData.due_time.strftime("%I:%M %p"))
            # ================================================================

            context['created_at'] = new_format1
            context['updated_at'] = new_format2
            taskList.append(context)

            # except:
            #     taskList =  []

            project_fk = Project_Management.objects.get(id=int(taskData.projectFK.id))
            moduleObj = Module_management.objects.get(id = int(taskData.moduleFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)


            listObj1 = []
            for i in subModule_obj:
                context2 = {}
                context2['mod_id'] = i.moduleFK.id
                context2['mod_name'] = i.moduleFK.moduleName.capitalize()
                context2['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context2['subMod_id'] = i.id
                context2['subModuleName'] = i.subModuleName.capitalize()
                context2['subModuleDescription'] = i.subModule_desc.capitalize()
                context2['projectName'] = project_fk.project_name.capitalize()
                context2['projectid'] = project_fk.id


                listObj1.append(context2)

            userObj = User.objects.get(email=request.user.email)
            empObject = employeeDetails.objects.get(userFK=userObj)
            userDataArray = {}
            userDataArray['userID'] = empObject.id
            userDataArray['userName'] = empObject.employee_name

            
            return JsonResponse({'response':context,'projectData':listObj,'empDataArray':empDataArray,'subModuleData':listObj1,'userType':'Employee','userDataArray':userDataArray})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           UPDATE SPECIFIC TASK
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def update_task_info(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            taskID = request.POST['taskID']
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            employeeFK = request.POST['employeeFK']
            taskDescription = request.POST['taskDescription']
            

            print(taskID)
            print(taskTitle)
            print(dueDate)
            print(dueTime)
            print(priority)
            print(employeeFK)
            print(taskDescription)

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                emp_Obj = employeeDetails.objects.get(id=int(employeeFK))
                print('emp obj >>>> ',emp_Obj,type(emp_Obj))

                from datetime import date,datetime
                taskObj.task_title = taskTitle
                taskObj.task_description = taskDescription
                taskObj.employeeFK = employeeDetails.objects.get(id=int(employeeFK))
                taskObj.due_date = datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d')
                taskObj.due_time = dueTime
                taskObj.priority = priority
                taskObj.updated_by = 'Admin'
                taskObj.updated_by_user_email = request.user.email
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d')
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the admin
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=emp_Obj.userFK,notification_from=request.user,
                                                            notification_subject=f'Task updated by Admin.',
                                                            notification_message=f'Admin updated existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            taskID = request.POST['taskID']
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            employeeFK = request.POST['employeeFK']
            taskDescription = request.POST['taskDescription']
            

            print(taskID)
            print(taskTitle)
            print(dueDate)
            print(dueTime)
            print(priority)
            print(employeeFK)
            print(taskDescription)

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                if(taskObj.created_by == 'Admin'):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                if(taskObj.created_by_user_email !=  request.user.email):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                emp_Obj = employeeDetails.objects.get(id=int(employeeFK))
                print('emp obj >>>> ',emp_Obj,type(emp_Obj))

                from datetime import date,datetime
                taskObj.task_title = taskTitle
                taskObj.task_description = taskDescription
                taskObj.employeeFK = employeeDetails.objects.get(id=int(employeeFK))
                taskObj.due_date = datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d')
                taskObj.due_time = dueTime
                taskObj.priority = priority
                taskObj.updated_by = 'Employee'
                taskObj.updated_by_user_email = request.user.email
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the manager
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=emp_Obj.userFK,notification_from=request.user,
                                                            notification_subject=f'Task updated by Manager,{request.user.first_name}.',
                                                            notification_message=f'{request.user.first_name} updated existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            taskID = request.POST['taskID']
            taskTitle = request.POST['taskTitle']
            dueDate = request.POST['dueDate']
            dueTime = request.POST['dueTime']
            priority = request.POST['priority']
            # employeeFK = request.POST.get('employeeFK')
            taskDescription = request.POST['taskDescription']
            

            print(taskID)
            print(taskTitle)
            print(dueDate)
            print(dueTime)
            print(priority)
            # print(employeeFK)
            print(taskDescription)

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                if(taskObj.created_by == 'Admin' or taskObj.created_by == 'Manager'):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                if(taskObj.created_by_user_email !=  request.user.email):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                userObj = User.objects.get(email=request.user.email)

                from datetime import date,datetime
                taskObj.task_title = taskTitle
                taskObj.task_description = taskDescription
                taskObj.employeeFK = employeeDetails.objects.get(userFK=userObj)
                taskObj.due_date = datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d')
                taskObj.due_time = dueTime
                taskObj.priority = priority
                taskObj.updated_by = 'Employee'
                taskObj.updated_by_user_email = request.user.email
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the employee
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=User.objects.get(username='admin@gmail.com'),notification_from=request.user,
                                                            notification_subject=f'Task updated by Employee.',
                                                            notification_message=f'{request.user.first_name} updated existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})


# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                           UPDATE TASK DEPENDENCES
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def update_task_dependencies(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            taskID = request.POST['taskID']
            taskDependencies = request.POST['taskDependencies']
            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                taskObj.dependencies = taskDependencies
                taskObj.updated_by = 'Admin'
                taskObj.updated_by_user_email = request.user.email
                from datetime import date,datetime
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the admin
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                            notification_subject=f'Task dependencies updated by Admin.',
                                                            notification_message=f'Admin updated existing task : {taskObj.task_title} dependencies for project : {taskObj.projectFK.project_name} for the rason of : {taskDependencies}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})
        
        if(request.session['userType'] == 'teacheR'):
            taskID = request.POST['taskID']
            taskDependencies = request.POST['taskDependencies']

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                if(taskObj.created_by == 'Admin'):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                if(taskObj.created_by_user_email !=  request.user.email):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                taskObj.dependencies = taskDependencies
                taskObj.updated_by = 'Manager'
                taskObj.updated_by_user_email = request.user.email
                from datetime import date,datetime
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the manager
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                            notification_subject=f'Task dependencies updated by Manager,{request.user.first_name}.',
                                                            notification_message=f'{request.user.first_name} updated existing task : {taskObj.task_title} dependencies for project : {taskObj.projectFK.project_name} for the rason of : {taskDependencies}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            taskID = request.POST['taskID']
            taskDependencies = request.POST['taskDependencies']

            message = 'success'
            try:
                taskObj = Task_Management.objects.get(id=int(taskID))
                if(taskObj.created_by == 'Admin' or taskObj.created_by == 'Manager'):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                if(taskObj.created_by_user_email !=  request.user.email):
                    return JsonResponse({'response':'You are not authorized to update this task!'})

                taskObj.dependencies = taskDependencies
                taskObj.updated_by = 'Employee'
                taskObj.updated_by_user_email = request.user.email
                from datetime import date,datetime
                todays_date = date.today()
                taskObj.updated_at = datetime.strptime(str(todays_date), '%Y-%m-%d').strftime('%Y-%m-%d'),
                taskObj.save()

                # ######################################################################################################################
                # new notification for update added task by the employee
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                            notification_subject=f'Task dependencies updated by {request.user.first_name}.',
                                                            notification_message=f'{request.user.first_name} updated existing task : {taskObj.task_title} dependencies for project : {taskObj.projectFK.project_name} for the rason of : {taskDependencies}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################

            except:
                message = 'fail'
            return JsonResponse({'response':message})

# ________________________________________________________________________________________________________________________________________________________________________________________________
# ================================================================================================================================================================================================
#                                                                          DELETE SPECIFIC TASK
# ================================================================================================================================================================================================
# ________________________________________________________________________________________________________________________________________________________________________________________________
@login_required(login_url='/')
def delete_task(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            taskObj = Task_Management.objects.get(id=int(id))
            message = 'success'
            try:
                # ######################################################################################################################
                # new notification for update added task by the employee
                # ######################################################################################################################
                notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                            notification_subject=f'Task deleted by Admin.',
                                                            notification_message=f'Admin deleted existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                            )
                notification_obj.save()
                # ######################################################################################################################
                taskObj.delete()
            except:
                message = 'fail'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            taskObj = Task_Management.objects.get(id=int(id))
            message = 'success'
            try:
                if(taskObj.created_by == 'Manager' and taskObj.created_by_user_email == request.user.email):
                    taskObj.delete()

                elif(taskObj.created_by == 'Employee'):
                    # ######################################################################################################################
                    # new notification for update added task by the employee
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                                notification_subject=f'Task deleted by Manager,{request.user.first_name}.',
                                                                notification_message=f'{request.user.first_name} deleted existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                    taskObj.delete()

                else:
                    message = 'fail'
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'studdenT'):
            taskObj = Task_Management.objects.get(id=int(id))
            message = 'success'
            try:
                if(taskObj.created_by == 'Employee' and taskObj.created_by_user_email == request.user.email):
                    # ######################################################################################################################
                    # new notification for update added task by the employee
                    # ######################################################################################################################
                    notification_obj = Notification_Management(notification_to=taskObj.employeeFK.userFK,notification_from=request.user,
                                                                notification_subject=f'Task deleted by {request.user.first_name}.',
                                                                notification_message=f'{request.user.first_name} deleted existing task : {taskObj.task_title} for project : {taskObj.projectFK.project_name}.\n\n\nThank You'
                                                                )
                    notification_obj.save()
                    # ######################################################################################################################
                    taskObj.delete()
                else:
                    message = 'fail'
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            message = 'fail'
            return JsonResponse({'response':message})







@login_required(login_url='/')
def get_module_list(request,id):
    if request.method == 'GET':
        project_fk = Project_Management.objects.get(id=int(id))
        moduleObj = Module_management.objects.filter(projectFK = project_fk)
        listObj = []
        for i in moduleObj:
            context = {}
            context['id'] = i.id
            context['moduleName'] = i.moduleName
            context['moduleDescription'] = i.module_desc
            context['projectName'] = project_fk.project_name

            listObj.append(context)
        # ------------------------------------------------------------------------------------------
        #                                    Task Dashboard Data
        # ------------------------------------------------------------------------------------------
        taskDashDict = {}
        taskDashList =  []
        totalTask = Task_Management.objects.filter(projectFK = project_fk)
        print('totalTask >>> ',totalTask,len(totalTask))
        if(len(totalTask) > 0 ):
            taskDashDict['project_totalTask'] = len(totalTask)
            completedTask = Task_Management.objects.filter(projectFK = project_fk,task_status='Done')
            ongoingTask = Task_Management.objects.filter(projectFK = project_fk,task_status='Doing')
            toDoTask = Task_Management.objects.filter(projectFK = project_fk,task_status='To do')
            from datetime import date
            startdate = date.today()
            print("Current year:", startdate.year)
            print("Current month:", startdate.month)
            print("Current day:", startdate.day)
            delayTask = Task_Management.objects.filter(projectFK = project_fk,due_date__lt=startdate)


            print('completedTask >>> ',completedTask)
            print('ongoingTask >>> ',ongoingTask)
            print('toDoTask >>> ',toDoTask)
            print('delayTask >>> ',delayTask)


            taskDashDict['project_completedTask'] = len(completedTask)
            taskDashDict['project_ongoingTask'] = len(ongoingTask)
            taskDashDict['project_todoTask'] = len(toDoTask)
            taskDashDict['project_delayTask'] = len(delayTask)

            if(len(completedTask) == 0):
                taskDashDict['project_completedTaskPercentage'] = 0
            else:
                taskDashDict['project_completedTaskPercentage'] = int(len(completedTask)/len(totalTask)*100)
                
            taskDashDict['project_ongoingTaskPercentage'] = int((((len(totalTask))-(len(totalTask) - len(ongoingTask)))/len(totalTask))*100)
            taskDashDict['project_todoTaskPercentage'] = int((((len(totalTask))-(len(totalTask) - len(toDoTask)))/len(totalTask))*100)
            taskDashDict['project_delayedTaskPercentage'] = int((((len(totalTask))-(len(totalTask) - len(delayTask)))/len(totalTask))*100
)
            taskDashList.append(taskDashDict)

        else:
            taskDashDict['project_totalTask'] = len(totalTask)
            taskDashDict['project_completedTask'] = 0
            taskDashDict['project_ongoingTask'] = 0
            taskDashDict['project_todoTask'] = 0
            taskDashDict['project_delayTask'] = 0


            taskDashDict['project_totalTaskPercentage'] = 0
            taskDashDict['project_completedTaskPercentage'] = 0
            taskDashDict['project_ongoingTaskPercentage'] = 0
            taskDashDict['project_todoTaskPercentage'] = 0
            taskDashDict['project_delayedTaskPercentage'] = 0

            taskDashList.append(taskDashDict)

        # ------------------------------------------------------------------------------------------
        #                                    Task Overview (Module wise progress) Data
        # ------------------------------------------------------------------------------------------
        moduleWiseList = []
        for k in moduleObj:
            moduleWiseDict = {}
            moduleWiseDict['moduleName'] = k.moduleName
            totalTaskObj = Task_Management.objects.filter(projectFK = project_fk,moduleFK=k)
            doneTaskObj = Task_Management.objects.filter(projectFK = project_fk,moduleFK=k,task_status='Done')
            progress_percent = 0
            if(len(totalTaskObj)!=0):
                progress_percent = int((len(doneTaskObj)/len(totalTaskObj))*100)
                moduleWiseDict['progress'] = progress_percent
                moduleWiseList.append(moduleWiseDict)
            else:
                moduleWiseDict['progress'] = progress_percent
                moduleWiseList.append(moduleWiseDict)

        
        # ------------------------------------------------------------------------------------------
        #                                    Task Overview Data
        # ------------------------------------------------------------------------------------------
        projectDetailsList = []
        project_fk = Project_Management.objects.get(id=int(id))

        projectInfoDict = {}

        module_obj = Module_management.objects.filter(projectFK = project_fk)
        print('modules >> ',module_obj,len(module_obj))
        for j in module_obj:
            subModList = []
            submoduleData = Sub_module_management.objects.filter(moduleFK = j)
            for m in submoduleData:
                subModList.append(m.subModuleName)
            print('sub mod >>> ',subModList)
            j.subModules = subModList


        # exit()
        projectTeam = eval(project_fk.project_team_member)
        if(len(projectTeam) > 0):
            projectTeam = projectTeam[0].split(',')

        print('projectTeam >>> ',projectTeam)
        teamList = []
        for j in projectTeam:
            dataContext = {}
            data = employeeDetails.objects.get(id=j)
            dataContext['empName'] = data.employee_name
            dataContext['empImg'] = str(data.profile_image)
            teamList.append(dataContext)

        print('teamList >>> ',teamList)




        projectInfoDict['projectName'] = project_fk.project_name
        projectInfoDict['projectDesc'] = project_fk.project_overview
        projectInfoDict['projectURL'] = "/project-management/project-detail/"+str(id)
        projectInfoDict['projectProgress'] = project_fk.project_progress
        projectInfoDict['projectStatus'] = project_fk.project_status

        projectInfoDict['projectStartData'] = project_fk.project_start_date.strftime("%d %b, %Y")
        projectInfoDict['projectDueDate'] = project_fk.project_due_date.strftime("%d %b, %Y")

        # projectInfoDict['projectManager'] = project_fk.project_progress
        projectInfoDict['projectTeam'] = teamList
        projectDetailsList.append(projectInfoDict)
        # ------------------------------------------------------------------------------------------

        return JsonResponse({'response':listObj,'taskDashList':taskDashList,'moduleWiseList':moduleWiseList,'projectDetailsList':projectDetailsList})




@login_required(login_url='/')
def filter_task(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectID = request.GET.get('projectID')
            moduleID = request.GET.get('moduleID')
            subModuleID = request.GET.get('subModuleID')
            employeeID = request.GET.get('employeeID')
            dueDate = request.GET.get('dueDate')
            status = request.GET.get('status')

            print('projectID >>>> ', projectID)
            print('moduleID >>>> ', moduleID)
            print('subModuleID >>>> ', subModuleID)
            print('employeeID >>>> ', employeeID)
            print('dueDate >>>> ', dueDate)
            print('status >>>> ', status)
            from datetime import date
            from datetime import timedelta
            from datetime import datetime, timedelta

            date_var = ''
            if(dueDate == 'today'):
                date_var = date.today()
            elif(dueDate == 'tommorow'):
                date_var = date.today()+timedelta(days=1)
            elif(dueDate == 'future-week'):
                date_today = date.today()
                startdate = date_today - timedelta(days=1)
                enddate = date_today - timedelta(days=7)
                # startdate = date.today()
                # enddate = startdate + timedelta(days=7)
                date_var = datetime.strftime(enddate,'%Y-%m-%d')
                futuredate = Task_Management.objects.filter(created_at__range=[startdate, enddate])
                # date_from = datetime.strptime(str(futuredate), '%Y-%m-%d').strftime('%d-%m-%y')
                # due_date=datetime.datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d')
                # print('date_from >>>>',date_from)
                # exit()

            elif(dueDate == 'past'):
                date_today = date.today()
                startdate = date_today - timedelta(days=1)
                enddate = date_today - timedelta(days=30)
                date_var = datetime.strftime(enddate, '%Y-%m-%d')
                pastdate = Task_Management.objects.filter(created_at__range=[startdate, enddate])


            # ======================================================================================
            #                                Filter Conditions
            # ======================================================================================
            if(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.all().order_by('-id')
                todoTaskObj = Task_Management.objects.filter(task_status = 'To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(task_status = 'Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(task_status = 'Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(task_status = 'Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # all to employee
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == ''):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # all to date
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == ''):
                todoTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # all to status

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'To do'):
                todoTaskObj = Task_Management.objects.filter(task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Doing'):
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Review'):
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(task_status='Review').order_by('-id')
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Done'):
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)


            # ===================================================================================================================================
            #  Second condition Employee & date

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == ''):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(
                    todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # Employee to status

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'To do'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Doing'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Review'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj =[]
                reviewTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Done'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(employeeFK=projectObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # date to status

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'To do'):
                todoTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Doing'):
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Review'):
                todoTaskObj = []
                doingTaskObj =[]
                reviewTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Done'):
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # third condition  Employee & Date & Status

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'To do'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Doing'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj =  Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Review'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Done'):
                projectObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(employeeFK=projectObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            
            

            # =======================================================================================================================
            # Select  project all data

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # project to employee

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(
                    todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # project to module
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(
                    todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

           

            # project to date

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(
                    todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # project to status

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Review').order_by('-id')
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # =======================================================================================================================
            # project to module & submodule
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, submoduleFK=submoduleObj,moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,submoduleFK=submoduleObj,moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,submoduleFK=submoduleObj,moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,submoduleFK=submoduleObj,moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & Employee

            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # module & Duedate
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            
            # module & status

            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj =[]
                doingTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)



            #  Employee to date
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            #  Employee & status
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj =[]
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)


            # Due date & status
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj =  Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # Third condition module & Submodule & Employee
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # module & submodule & date
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & submodule & status

            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)


            
            # module & Employee & Due date
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID)) 
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, moduleFK=moduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & Employe & status
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj,  task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj,  task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj =  Task_Management.objects.filter(projectFK=projectObj,employeeFK=employeeObj, moduleFK=moduleObj,  task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, employeeFK=employeeObj, moduleFK=moduleObj,  task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            
            # module & date & status
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID == '' and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # fourth condition module & submodule & Employee & date

            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & submodule & date & status
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj =[]
                doingTaskObj =  Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID == '' and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & Employee & date & status(status pending)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, employeeFK=employeeObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and employeeID != '' and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # five condition module & submodule & employee & date & status
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and employeeID != '' and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                employeeObj = employeeDetails.objects.get(id=int(employeeID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, employeeFK=employeeObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

        # ------------------------------------Admin filter end---------------------------------------------------------------------------------------------


        # ---------------------- Employee filter ---------------------------------------------------------------------------------------------------------

        if(request.session['userType'] == 'studdenT'):
            projectID = request.GET.get('projectID')
            moduleID = request.GET.get('moduleID')
            subModuleID = request.GET.get('subModuleID')
            # employeeID = request.GET.get('employeeID')
            dueDate = request.GET.get('dueDate')
            status = request.GET.get('status')

            print('projectID >>>> ', projectID)
            print('moduleID >>>> ', moduleID)
            print('subModuleID >>>> ', subModuleID)
            # print('employeeID >>>> ', employeeID)
            print('dueDate >>>> ', dueDate)
            print('status >>>> ', status)
            from datetime import date
            from datetime import timedelta
            from datetime import datetime
            date_var = ''
            if(dueDate == 'today'):
                date_var = date.today()
            elif(dueDate == 'tommorow'):
                date_var = date.today()+timedelta(days=1)

            elif(dueDate == 'future-week'):
                date_today = date.today()
                startdate = date_today + timedelta(days=1)
                enddate = date_today + timedelta(days=7)
                # startdate = date.today()
                # enddate = startdate + timedelta(days=7)
                futuredate = Task_Management.objects.filter(created_at__range=[startdate, enddate])
                date_var = datetime.strftime(enddate, '%Y-%m-%d')
                # date_var = datetime.strftime(futuredate,'%Y-%m-%d')
                # date_from = datetime.strptime(str(futuredate), '%m-%d-%Y')
                # due_date=datetime.datetime.strptime(dueDate, '%m/%d/%Y').strftime('%Y-%m-%d')
                # print('date_from >>>>',date_from)
                # exit()

            elif(dueDate == 'past'):
                date_today = date.today()
                startdate = date_today + timedelta(days=1)
                enddate = date_today + timedelta(days=30)
                pastdate = Task_Management.objects.filter(created_at__range=[startdate, enddate])
                # print('pastdate >>>>>>>', pastdate)
                # exit()
                date_var = datetime.strftime(enddate, '%Y-%m-%d')


            # =======================================================================================================================
            if(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.all().order_by('-id')
                todoTaskObj = Task_Management.objects.filter(task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # dueDate

            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == ''):
                todoTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # status
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == 'To do'):
                todoTaskObj = Task_Management.objects.filter(task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and  status == 'Doing'):
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == 'Review'):
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == 'Done'):
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # dueDate & Status
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == 'To do'):
                todoTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj =[]
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == 'Doing'):
                todoTaskObj =[]
                doingTaskObj =  Task_Management.objects.filter(due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj =[]
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == 'Review'):
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID == 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == 'Done'):
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj =[]
                doneTaskObj =  Task_Management.objects.filter(due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # ------------------------------------------------------------------------------------------------------------------------------------------------
            # project Wise

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == ''):

                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # module Wise
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # Due date

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # Status
            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == ''  and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Review').order_by('-id')
                doneTaskObj = [] 
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID == '' and subModuleID == ''  and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)



            # module & submodule
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and dueDate == '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj,submoduleFK=submoduleObj, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj,submoduleFK=submoduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj,submoduleFK=submoduleObj, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj,submoduleFK=submoduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & date
            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & status
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID != '' and subModuleID == '' and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj =[]
                doingTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            

            # third condition module & submodule & date
            elif(projectID != 'All' and moduleID != '' and subModuleID != '' and dueDate != '' and status == ''):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # module & submodule & status

            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate == '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate == '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate == '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate == '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)

            # module & date & status
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID == ''  and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            # fourth condition module & submodule & date & status

            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate != '' and status == 'To do'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='To do').order_by('-id')
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate != '' and status == 'Doing'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj =[]
                doingTaskObj =  Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Doing').order_by('-id')
                reviewTaskObj = []
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate != '' and status == 'Review'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj = []
                doingTaskObj = []
                reviewTaskObj = Task_Management.objects.filter(projectFK=projectObj,moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Review').order_by('-id')
                doneTaskObj = []
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)
            elif(projectID != 'All' and moduleID != '' and subModuleID != ''  and dueDate != '' and status == 'Done'):
                projectObj = Project_Management.objects.get(id=int(projectID))
                moduleObj = Module_management.objects.get(id=int(moduleID))
                submoduleObj = Sub_module_management.objects.get(id=int(subModuleID))
                todoTaskObj =[]
                doingTaskObj = []
                reviewTaskObj = []
                doneTaskObj =  Task_Management.objects.filter(projectFK=projectObj, moduleFK=moduleObj, submoduleFK=submoduleObj,  due_date=date_var, task_status='Done').order_by('-id')
                responseList = []

                responseList = generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj)
                print('responseList >>> ', responseList)




            # ================================================================================================================================================
        return JsonResponse({'response': responseList})


def generalFilterFunction(todoTaskObj, doingTaskObj, reviewTaskObj, doneTaskObj):
    todoList = []
    doingList = []
    reviewList = []
    doneList = []
    # ======================================================================================
    for i in todoTaskObj:
        todoDict = {}
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

        if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
            new_format = 'Today'
            i.status = 'today'
            if(int(current_time.hour) > int(timeHr[0])):
                i.status = 'delay'                        
                todoDict['status'] = 'delay'
            else:
                todoDict['status'] = ''
            i.due_date = new_format
            
            todoDict['due_date'] = new_format
            todoDict['delayed_by'] = 0

        NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
        tommotowDate = str(NextDay_Date)
        print('NextDay_Date.day >>>> ',NextDay_Date.day)
        if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
            new_format = 'Tommorow'
            i.status = 'tommorow'                        
            i.due_date = new_format 
            todoDict['due_date'] = new_format
            todoDict['status'] = 'tommorow' 
            todoDict['delayed_by'] = 0              
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            todoDict['due_date'] = new_format
            todoDict['status'] = 'delay'
            todoDict['delayed_by'] = diff.days


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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            todoDict['due_date'] = new_format
            todoDict['status'] = 'delay'
            todoDict['delayed_by'] = diff.days

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            todoDict['due_date'] = new_format
            todoDict['status'] = 'delay'
            todoDict['delayed_by'] = diff.days
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            todoDict['due_date'] = new_format
            todoDict['status'] = 'delay'
            todoDict['delayed_by'] = diff.days

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
            todoDict['due_date'] = new_format
            todoDict['status'] = ''
            todoDict['delayed_by'] = diff.days
        
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
            todoDict['due_date'] = new_format
            todoDict['status'] = ''
            todoDict['delayed_by'] = diff.days

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
            todoDict['due_date'] = new_format
            todoDict['status'] = ''
            todoDict['delayed_by'] = diff.days
        

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            todoDict['due_date'] = new_format
            todoDict['status'] = 'delay'
            todoDict['delayed_by'] = diff.days
        # ==================================================================================
        todoDict['taskID'] = i.id
        todoDict['projectName'] = i.projectFK.project_name
        todoDict['taskTitile'] = i.task_title
        todoDict['assignedTo'] = i.employeeFK.employee_name
        todoDict['profile_image'] = str(i.employeeFK.profile_image)
        todoDict['due_date'] = i.due_date
        todoDict['due_time'] = i.due_time
        todoDict['priority'] = i.priority
        todoDict['created_by'] = i.created_by
        
        todoList.append(todoDict)
        # ----------------------------------------------------------------------------------
    # doingTaskObj = Task_Management.objects.filter(task_status = 'Doing').order_by('-id')
    for i in doingTaskObj:
        doingDict = {}
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

        if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
            new_format = 'Today'
            i.status = 'today'
            if(int(current_time.hour) > int(timeHr[0])):
                i.status = 'delay'                        
                doingDict['status'] = 'delay'
            else:
                doingDict['status'] = ''
            i.due_date = new_format
            
            doingDict['due_date'] = new_format
            doingDict['delayed_by'] = 0

        NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
        tommotowDate = str(NextDay_Date)
        print('NextDay_Date.day >>>> ',NextDay_Date.day)
        if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
            new_format = 'Tommorow'
            i.status = 'tommorow'                        
            i.due_date = new_format 
            doingDict['due_date'] = new_format
            doingDict['status'] = 'tommorow' 
            doingDict['delayed_by'] = 0              
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doingDict['due_date'] = new_format
            doingDict['status'] = 'delay'
            doingDict['delayed_by'] = diff.days


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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doingDict['due_date'] = new_format
            doingDict['status'] = 'delay'
            doingDict['delayed_by'] = diff.days

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doingDict['due_date'] = new_format
            doingDict['status'] = 'delay'
            doingDict['delayed_by'] = diff.days
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doingDict['due_date'] = new_format
            doingDict['status'] = 'delay'
            doingDict['delayed_by'] = diff.days

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
            doingDict['due_date'] = new_format
            doingDict['status'] = ''
            doingDict['delayed_by'] = diff.days
        
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
            doingDict['due_date'] = new_format
            doingDict['status'] = ''
            doingDict['delayed_by'] = diff.days

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
            doingDict['due_date'] = new_format
            doingDict['status'] = ''
            doingDict['delayed_by'] = diff.days
        

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doingDict['due_date'] = new_format
            doingDict['status'] = 'delay'
            doingDict['delayed_by'] = diff.days
        # ==================================================================================
        doingDict['taskID'] = i.id
        doingDict['projectName'] = i.projectFK.project_name
        doingDict['taskTitile'] = i.task_title
        doingDict['assignedTo'] = i.employeeFK.employee_name
        doingDict['profile_image'] = str(i.employeeFK.profile_image)
        doingDict['due_date'] = i.due_date
        doingDict['due_time'] = i.due_time
        doingDict['priority'] = i.priority
        doingDict['created_by'] = i.created_by
        doingList.append(doingDict)
        # ----------------------------------------------------------------------------------
    # reviewTaskObj = Task_Management.objects.filter(task_status = 'Review').order_by('-id')
    for i in reviewTaskObj:
        reviewDict = {}
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

        if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
            new_format = 'Today'
            i.status = 'today'
            if(int(current_time.hour) > int(timeHr[0])):
                i.status = 'delay'                        
                reviewDict['status'] = 'delay'
            else:
                reviewDict['status'] = ''
            i.due_date = new_format
            
            reviewDict['due_date'] = new_format
            reviewDict['delayed_by'] = 0

        NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
        tommotowDate = str(NextDay_Date)
        print('NextDay_Date.day >>>> ',NextDay_Date.day)
        if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
            new_format = 'Tommorow'
            i.status = 'tommorow'                        
            i.due_date = new_format 
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'tommorow' 
            reviewDict['delayed_by'] = 0              
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'delay'
            reviewDict['delayed_by'] = diff.days


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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'delay'
            reviewDict['delayed_by'] = diff.days

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'delay'
            reviewDict['delayed_by'] = diff.days
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'delay'
            reviewDict['delayed_by'] = diff.days

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
            reviewDict['due_date'] = new_format
            reviewDict['status'] = ''
            reviewDict['delayed_by'] = diff.days
        
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
            reviewDict['due_date'] = new_format
            reviewDict['status'] = ''
            reviewDict['delayed_by'] = diff.days

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
            reviewDict['due_date'] = new_format
            reviewDict['status'] = ''
            reviewDict['delayed_by'] = diff.days
        

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            reviewDict['due_date'] = new_format
            reviewDict['status'] = 'delay'
            reviewDict['delayed_by'] = diff.days
        # ==================================================================================
        reviewDict['taskID'] = i.id
        reviewDict['projectName'] = i.projectFK.project_name
        reviewDict['taskTitile'] = i.task_title
        reviewDict['assignedTo'] = i.employeeFK.employee_name
        reviewDict['profile_image'] = str(i.employeeFK.profile_image)
        reviewDict['due_date'] = i.due_date
        reviewDict['due_time'] = i.due_time
        reviewDict['priority'] = i.priority
        reviewDict['created_by'] = i.created_by
        reviewList.append(reviewDict)
        # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------
    # doneTaskObj = Task_Management.objects.filter(task_status = 'Done').order_by('-id')
    for i in doneTaskObj:
        doneDict = {}
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

        if(int(dueData[2]) == int(todays_date.day) and int(dueData[1]) == int(todays_date.month) and int(dueData[0]) == int(todays_date.year)):
            new_format = 'Today'
            i.status = 'today'
            if(int(current_time.hour) > int(timeHr[0])):
                i.status = 'delay'                        
                doneDict['status'] = 'delay'
            else:
                doneDict['status'] = ''
            i.due_date = new_format
            
            doneDict['due_date'] = new_format
            doneDict['delayed_by'] = 0

        NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
        tommotowDate = str(NextDay_Date)
        print('NextDay_Date.day >>>> ',NextDay_Date.day)
        if(int(dueData[2]) == int(NextDay_Date.day) and int(dueData[1]) == int(NextDay_Date.month) and int(dueData[0]) == int(NextDay_Date.year)):
            new_format = 'Tommorow'
            i.status = 'tommorow'                        
            i.due_date = new_format 
            doneDict['due_date'] = new_format
            doneDict['status'] = 'tommorow' 
            doneDict['delayed_by'] = 0              
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doneDict['due_date'] = new_format
            doneDict['status'] = 'delay'
            doneDict['delayed_by'] = diff.days


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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doneDict['due_date'] = new_format
            doneDict['status'] = 'delay'
            doneDict['delayed_by'] = diff.days

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doneDict['due_date'] = new_format
            doneDict['status'] = 'delay'
            doneDict['delayed_by'] = diff.days
        
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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doneDict['due_date'] = new_format
            doneDict['status'] = 'delay'
            doneDict['delayed_by'] = diff.days

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
            doneDict['due_date'] = new_format
            doneDict['status'] = ''
            doneDict['delayed_by'] = diff.days
        
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
            doneDict['due_date'] = new_format
            doneDict['status'] = ''
            doneDict['delayed_by'] = diff.days

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
            doneDict['due_date'] = new_format
            doneDict['status'] = ''
            doneDict['delayed_by'] = diff.days
        

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
            i.delayed_by = diff.days                      
            i.due_date = new_format
            doneDict['due_date'] = new_format
            doneDict['status'] = 'delay'
            doneDict['delayed_by'] = diff.days
        # ==================================================================================
        doneDict['taskID'] = i.id
        doneDict['projectName'] = i.projectFK.project_name
        doneDict['taskTitile'] = i.task_title
        doneDict['assignedTo'] = i.employeeFK.employee_name
        doneDict['profile_image'] = str(i.employeeFK.profile_image)
        doneDict['due_date'] = i.due_date
        doneDict['due_time'] = i.due_time
        doneDict['priority'] = i.priority
        doneDict['created_by'] = i.created_by
        doneList.append(doneDict)
        # ----------------------------------------------------------------------------------
    return todoList,doingList,reviewList,doneList