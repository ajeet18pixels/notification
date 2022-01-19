from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from ..models.master_models import designation_Master, employeeType_Master
from django.contrib.auth.decorators import login_required

from ..models.project_model import Project_Management,Module_management,Sub_module_management
from ..models.employee_model import employeeDetails
from ..models.master_models import project_sector_Master,project_type_Master,Project_Technology_Master
from ..models.task_model import Task_Management
from django.contrib.auth.models import User


@login_required(login_url='/')
def add_project(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            managerObj = employeeType_Master.objects.get(employee_type_name='Manager')
            empObj = employeeType_Master.objects.get(employee_type_name='Employee')

            employeeObj = employeeDetails.objects.filter(employeeTypeFK=empObj).order_by('-id')
            managerObj = employeeDetails.objects.filter(employeeTypeFK=managerObj).order_by('-id')

            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')
            return render(request,'admin/project/add-new-project.html',{'managerObj':managerObj,'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj})
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
    
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            projectName = request.POST['ProjectName']
            projectsSector = request.POST['ProjectSector']
            projectType = request.POST.getlist('ProjectTypeArray')
            projectTech = request.POST.getlist('ProjectTechnoloyArray')
            projectStartDate = request.POST.get('startDate').split('-')
            if(len(projectStartDate) > 1):
                if(projectStartDate[1] == 'Jan'):
                    projectStartDate[1] = 1
                if(projectStartDate[1] == 'Feb'):
                    projectStartDate[1] = 2
                if(projectStartDate[1] == 'Mar'):
                    projectStartDate[1] = 3
                if(projectStartDate[1] == 'Apr'):
                    projectStartDate[1] = 4
                if(projectStartDate[1] == 'May'):
                    projectStartDate[1] = 5
                if(projectStartDate[1] == 'Jun'):
                    projectStartDate[1] = 6
                if(projectStartDate[1] == 'Jul'):
                    projectStartDate[1] = 7
                if(projectStartDate[1] == 'Aug'):
                    projectStartDate[1] = 8
                if(projectStartDate[1] == 'Sep'):
                    projectStartDate[1] = 9
                if(projectStartDate[1] == 'Oct'):
                    projectStartDate[1] = 10
                if(projectStartDate[1] == 'Nov'):
                    projectStartDate[1] = 11
                if(projectStartDate[1] == 'Dec'):
                    projectStartDate[1] = 12
                projectStartDate = f"{projectStartDate[2]}-{projectStartDate[1]}-{projectStartDate[0]}"
            else:
                projectStartDate = None
            projectDueDate = request.POST.get('endDate').split('-')
            if(len(projectDueDate) > 1):
                if(projectDueDate[1] == 'Jan'):
                    projectDueDate[1] = 1
                if(projectDueDate[1] == 'Feb'):
                    projectDueDate[1] = 2
                if(projectDueDate[1] == 'Mar'):
                    projectDueDate[1] = 3
                if(projectDueDate[1] == 'Apr'):
                    projectDueDate[1] = 4
                if(projectDueDate[1] == 'May'):
                    projectDueDate[1] = 5
                if(projectDueDate[1] == 'Jun'):
                    projectDueDate[1] = 6
                if(projectDueDate[1] == 'Jul'):
                    projectDueDate[1] = 7
                if(projectDueDate[1] == 'Aug'):
                    projectDueDate[1] = 8
                if(projectDueDate[1] == 'Sep'):
                    projectDueDate[1] = 9
                if(projectDueDate[1] == 'Oct'):
                    projectDueDate[1] = 10
                if(projectDueDate[1] == 'Nov'):
                    projectDueDate[1] = 11
                if(projectDueDate[1] == 'Dec'):
                    projectDueDate[1] = 12

                projectDueDate = f"{projectDueDate[2]}-{projectDueDate[1]}-{projectDueDate[0]}"
            else:
                projectDueDate = None

            project_overview = request.POST['ProjectOverview']
            projectManagers = request.POST.getlist('ProjectManagersArray')
            projectTeamMember = request.POST.getlist('ProjectTeamArray')
            if(projectManagers == ['']):
                projectManagers = []

            if(projectTeamMember == ['']):
                projectTeamMember = []
            ProjectLogo =  request.FILES.get('ProjectLogo')
            UploadData =  request.FILES.get('upload_docs_0')
            UploadData_1 =  request.FILES.get('upload_docs_1')
            UploadData_2 =  request.FILES.get('upload_docs_2')
            UploadData_3 =  request.FILES.get('upload_docs_3')
            UploadData_4 =  request.FILES.get('upload_docs_4')
            urlType =  request.POST.get('upload_url_type_0')
            UrlData =  request.POST.get('upload_url_0')
            urlType_1 =  request.POST.get('upload_url_type_1')
            UrlData_1 =  request.POST.get('upload_url_1')
            urlType_2 =  request.POST.get('upload_url_type_2')
            UrlData_2 =  request.POST.get('upload_url_2')
            urlType_3 =  request.POST.get('upload_url_type_3')
            UrlData_3 =  request.POST.get('upload_url_4')
            urlType_4 =  request.POST.get('upload_url_type_4')
            UrlData_4 =  request.POST.get('upload_url_4')
            message = 'success'
            
            projectSector_fk = project_sector_Master.objects.get(id=int(projectsSector))
            projectObj = Project_Management(
                        project_name = projectName,
                        project_sector_FK = projectSector_fk,
                        project_type_fk = projectType,
                        project_technology_fk = projectTech,
                        project_start_date = projectStartDate,
                        project_due_date = projectDueDate,
                        project_overview = project_overview,
                        project_manager = projectManagers,
                        project_team_member = projectTeamMember,
                        project_logo = ProjectLogo,

                        upload_files = UploadData,
                        upload_files_1 = UploadData_1,
                        upload_files_2 = UploadData_2,
                        upload_files_3 = UploadData_3,
                        upload_files_4 = UploadData_4,

                        project_url_for = urlType,
                        project_url = UrlData,
                        project_url_for_1 = urlType_1,
                        project_url_1 = UrlData_1,
                        project_url_for_2 = urlType_2,
                        project_url_2 = UrlData_2,
                        project_url_for_3 = urlType_3,
                        project_url_3 = UrlData_3,
                        project_url_for_4 = urlType_4,
                        project_url_4 = UrlData_4,
                    )
            projectObj.save()
            # except:
            #     message = 'fail'

            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')

@login_required(login_url='/')
def project_list(request):
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

                # print('due_date >>>> ',i.project_due_date)
                import datetime

                CurrentDate = datetime.datetime.now()
                # print(CurrentDate)

                ExpectedDate = str(i.project_due_date)
                # print('ExpectedDate >>>> ',ExpectedDate)

                if(ExpectedDate != 'None'):
                    ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%Y-%m-%d")
                # print(ExpectedDate)


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
                    if(i.project_progress > 0):
                        i.project_status = 'Ongoing'
                    else:
                        i.project_status = 'Just Created'

                i.save()
                # ==========================================================================================
                # ==========================================================================================
                teamList = []
                projectManagerData = eval(i.project_manager)
                if(len(projectManagerData) > 0):
                    projectManagerData = projectManagerData[0].split(',')
                # print('projectManagerData >>> ',projectManagerData)
                data = ''
                for j in projectManagerData:
                    data = data + str(employeeDetails.objects.get(id=j).employee_name.split(' ')[0])+' | '
                # print('data >>> ',data)
                i.projectManagerName = data

                projectTeam = eval(i.project_team_member)
                if(len(projectTeam) > 0):
                    projectTeam = projectTeam[0].split(',')
                for j in projectTeam:
                    context = {}
                    print('j data >>>>>>>>>>>>>>>>>>>>>>>> ',j)
                    data = employeeDetails.objects.get(id=j)
                    context['empName'] = data.employee_name
                    context['empImg'] = data.profile_image
                    teamList.append(context)

                print('teamList >>> ',teamList)
                i.teamList = teamList



            return render(request,'admin/project/project-list.html',{'projectObj':projectObj,'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj})

        if(request.session['userType'] == 'teacheR'):
            # projectObj = Project_Management.objects.all().order_by('-id')
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')
            
            user_FK = User.objects.get(email=request.user)
            print('userFK >>> ',user_FK)

            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            print('employeeFk >>> ',employeeFk,employeeFk.id)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id)) | Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))

            for i in projectObj:
                i.moduleCount = len(Module_management.objects.filter(projectFK = i))
            
            for i in projectObj:
                teamList = []
                if(len(eval(i.project_manager)) > 0):
                    projectManagerData = eval(i.project_manager)[0].split(',')
                    print('projectManagerData >>> ',projectManagerData)
                    data = ''
                    for j in projectManagerData:

                        data = data + str(employeeDetails.objects.get(id=j).employee_name.split(' ')[0])+' | '
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



            return render(request,'admin/project/project-list.html',{'projectObj':projectObj,'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj})
            
        if(request.session['userType'] == 'studdenT'):
            # projectObj = Project_Management.objects.all().order_by('-id')
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')

            user_FK = User.objects.get(email=request.user)
            print('userFK >>> ',user_FK)

            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            print('employeeFk >>> ',employeeFk,employeeFk.id)
            projectObj = Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))

            for i in projectObj:
                i.moduleCount = len(Module_management.objects.filter(projectFK = i))
            
            for i in projectObj:
                data = ''
                if(i.project_manager != '[]'):
                    projectManagerData = eval(i.project_manager)[0].split(',')
                    print('projectManagerData >>> ',projectManagerData)
                    for j in projectManagerData:
                        data = data + str(employeeDetails.objects.get(id=j).employee_name.split(' ')[0])+' | '
                    print('data >>> ',data)
                i.projectManagerName = data
                
                
                teamList = []
                if(i.project_team_member != '[]'):
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



            return render(request,'admin/project/project-list.html',{'projectObj':projectObj,'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj})



@login_required(login_url='/')
def project_detail(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR' or request.session['userType'] == 'studdenT'):
            Project_obj = Project_Management.objects.get(id=id)
            # ===========================================================================
            if(request.session['userType'] == 'teacheR'):
                empObj = employeeDetails.objects.get(userFK=request.user)

                teamList = []
                if(Project_obj.project_manager != '[]'):
                    projectTeam = eval(Project_obj.project_manager)
                    if(len(projectTeam) > 0):
                        projectTeam = projectTeam[0].split(',')
                    for j in projectTeam:
                        context = {}
                        teamList.append(j)
                    if(str(empObj.id) not in teamList):
                        return redirect('unautorizedaccess')
                
                teamArray = []
                if(request.session['userType'] == 'studdenT'):
                    if(Project_obj.project_team_member != '[]'):
                        projectTeam = eval(Project_obj.project_team_member)
                        if(len(projectTeam) > 0):
                            projectTeam = projectTeam[0].split(',')
                        for j in projectTeam:
                            context = {}
                            teamArray.append(j)
                        if(str(empObj.id) not in teamArray):
                            return redirect('unautorizedaccess')

                

                print('teamList >>> ',teamList)
                print('teamArray >>> ',teamArray)


                # if((empObj.id not in teamArray) and (empObj.id not in teamList)):
                #     return redirect('unautorizedaccess')

            # ===========================================================================
            module_obj = Module_management.objects.filter(projectFK = Project_obj)
            for j in module_obj:
                subModList = []
                submoduleData = Sub_module_management.objects.filter(moduleFK = j)
                for m in submoduleData:
                    subModList.append(m.subModuleName + ' :- ' + m.subModule_desc)
                j.subModules = subModList


            projectTeam = eval(Project_obj.project_team_member)
            if(len(projectTeam) > 0):
                projectTeam = projectTeam[0].split(',')

            teamList = []
            for j in projectTeam:
                context = {}
                data = employeeDetails.objects.get(id=j)
                context['empName'] = data.employee_name
                context['empImg'] = data.profile_image
                teamList.append(context)
            

            projectManager = eval(Project_obj.project_manager)
            if(len(projectManager) > 0):
                projectManager = projectManager[0].split(',')

            managerList = []
            for j in projectManager:
                context = {}
                data = employeeDetails.objects.get(id=j)
                context['managerName'] = data.employee_name
                context['managerImg'] = data.profile_image
                managerList.append(context)

            print('managerList >>> ',managerList)

            projectTech = eval(Project_obj.project_technology_fk)
            if(len(projectTech) > 0):
                projectTech = projectTech[0].split(',')

            projectTechList = []
            for j in projectTech:
                context = {}
                data = Project_Technology_Master.objects.get(id=j)
                context['tech'] = data.Technology
                projectTechList.append(context)

            print('projectTechList >>> ',projectTechList)

            projectType = eval(Project_obj.project_type_fk)
            if(len(projectType) > 0):
                projectType = projectType[0].split(',')

            projectTypeList = []
            for j in projectType:
                context = {}
                data = project_type_Master.objects.get(id=j)
                context['projectType'] = data.projectType
                projectTypeList.append(context)

            print('projectTypeList >>> ',projectTypeList)

            if(Project_obj.upload_files != None or Project_obj.upload_files != ''):
                Project_obj.upload_files_extension = str(Project_obj.upload_files).split('.')[-1]

            if(Project_obj.upload_files_1 != None or Project_obj.upload_files_1 != ''):
                Project_obj.upload_files_extension_1 = str(Project_obj.upload_files_1).split('.')[-1]

            if(Project_obj.upload_files_2 != None or Project_obj.upload_files_2 != ''):
                Project_obj.upload_files_extension_2 = str(Project_obj.upload_files_2).split('.')[-1]

            if(Project_obj.upload_files_3 != None or Project_obj.upload_files_3 != ''):
                Project_obj.upload_files_extension_3 = str(Project_obj.upload_files_3).split('.')[-1]

            if(Project_obj.upload_files_4 != None or Project_obj.upload_files_4 != ''):
                Project_obj.upload_files_extension_4 = str(Project_obj.upload_files_4).split('.')[-1]

            return render(request,'admin/project/project-details.html',{'Project_obj':Project_obj,'module_obj':module_obj,'moduleCount':len(module_obj),'teamList':teamList,'managerList':managerList,'projectTechList':projectTechList,'projectTypeList':projectTypeList})
        # if(request.session['userType'] == 'teacheR'):
        #     Project_obj = Project_Management.objects.get(id=id)
        #     empObj = employeeDetails.objects.get(userFK=request.user)

        #     teamList = []
        #     if(Project_obj.project_manager != '[]'):
        #         projectTeam = eval(Project_obj.project_manager)
        #         if(len(projectTeam) > 0):
        #             projectTeam = projectTeam[0].split(',')
        #         for j in projectTeam:
        #             context = {}
        #             teamList.append(j)

        #     if(str(empObj.id) not in teamList):
        #         return redirect('unautorizedaccess')

                
        #     module_obj = Module_management.objects.filter(projectFK = Project_obj)
        #     print('modules >> ',module_obj,len(module_obj))
        #     for j in module_obj:
        #         subModList = []
        #         submoduleData = Sub_module_management.objects.filter(moduleFK = j)
        #         for m in submoduleData:
        #             subModList.append(m.subModuleName)
        #         print('sub mod >>> ',subModList)
        #         j.subModules = subModList


        #     # exit()
        #     projectTeam = eval(Project_obj.project_team_member)
        #     if(len(projectTeam) > 0):
        #         projectTeam = projectTeam[0].split(',')

        #     print('projectTeam >>> ',projectTeam)
        #     teamList = []
        #     for j in projectTeam:
        #         context = {}
        #         data = employeeDetails.objects.get(id=j)
        #         context['empName'] = data.employee_name
        #         context['empImg'] = data.profile_image
        #         teamList.append(context)

        #     print('teamList >>> ',teamList)
        #     if(Project_obj.upload_files != None or Project_obj.upload_files != ''):
        #         Project_obj.upload_files_extension = str(Project_obj.upload_files).split('.')[-1]

        #     if(Project_obj.upload_files_1 != None or Project_obj.upload_files_1 != ''):
        #         Project_obj.upload_files_extension_1 = str(Project_obj.upload_files_1).split('.')[-1]

        #     if(Project_obj.upload_files_2 != None or Project_obj.upload_files_2 != ''):
        #         Project_obj.upload_files_extension_2 = str(Project_obj.upload_files_2).split('.')[-1]

        #     if(Project_obj.upload_files_3 != None or Project_obj.upload_files_3 != ''):
        #         Project_obj.upload_files_extension_3 = str(Project_obj.upload_files_3).split('.')[-1]

        #     if(Project_obj.upload_files_4 != None or Project_obj.upload_files_4 != ''):
        #         Project_obj.upload_files_extension_4 = str(Project_obj.upload_files_4).split('.')[-1]

        #     # print(Project_obj.project_team_member)
        #     # for i in Project_obj.project_team_member:
        #     #     print(i.employee_name)
        #     return render(request,'admin/project/project-details.html',{'Project_obj':Project_obj,'module_obj':module_obj,'moduleCount':len(module_obj),'teamList':teamList})
            
        if(request.session['userType'] == 'studdenT'):
            Project_obj = Project_Management.objects.get(id=id)
            empObj = employeeDetails.objects.get(userFK=request.user)


            teamList = []
            if(Project_obj.project_team_member != '[]'):
                projectTeam = eval(Project_obj.project_team_member)
                if(len(projectTeam) > 0):
                    projectTeam = projectTeam[0].split(',')
                for j in projectTeam:
                    context = {}
                    teamList.append(j)

            if(str(empObj.id) not in teamList):
                return redirect('unautorizedaccess')


            module_obj = Module_management.objects.filter(projectFK = Project_obj)
            print('modules >> ',module_obj,len(module_obj))
            for j in module_obj:
                subModList = []
                submoduleData = Sub_module_management.objects.filter(moduleFK = j)
                for m in submoduleData:
                    subModList.append(m.subModuleName)
                print('sub mod >>> ',subModList)
                j.subModules = subModList


            # exit()
            projectTeam = eval(Project_obj.project_team_member)
            if(len(projectTeam) > 0):
                projectTeam = projectTeam[0].split(',')

            print('projectTeam >>> ',projectTeam)
            teamList = []
            teamArray = []
            for j in projectTeam:
                context = {}
                data = employeeDetails.objects.get(id=j)
                context['empName'] = data.employee_name
                context['empImg'] = data.profile_image
                teamList.append(context)
                teamArray.append(data.id)

            if(str(empObj.id) not in teamArray):
                return redirect('unautorizedaccess')

            print('teamList >>> ',teamList)
            if(Project_obj.upload_files != None or Project_obj.upload_files != ''):
                Project_obj.upload_files_extension = str(Project_obj.upload_files).split('.')[-1]

            if(Project_obj.upload_files_1 != None or Project_obj.upload_files_1 != ''):
                Project_obj.upload_files_extension_1 = str(Project_obj.upload_files_1).split('.')[-1]

            if(Project_obj.upload_files_2 != None or Project_obj.upload_files_2 != ''):
                Project_obj.upload_files_extension_2 = str(Project_obj.upload_files_2).split('.')[-1]

            if(Project_obj.upload_files_3 != None or Project_obj.upload_files_3 != ''):
                Project_obj.upload_files_extension_3 = str(Project_obj.upload_files_3).split('.')[-1]

            if(Project_obj.upload_files_4 != None or Project_obj.upload_files_4 != ''):
                Project_obj.upload_files_extension_4 = str(Project_obj.upload_files_4).split('.')[-1]

            # print(Project_obj.project_team_member)
            # for i in Project_obj.project_team_member:
            #     print(i.employee_name)
            return render(request,'admin/project/project-details.html',{'Project_obj':Project_obj,'module_obj':module_obj,'moduleCount':len(module_obj),'teamList':teamList})


@login_required(login_url='/')
def update_project(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            Project_obj = Project_Management.objects.get(id=id)
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')

            count = 0
            if(Project_obj.project_url_for != None):
                count = count + 1
            if(Project_obj.project_url_for_1 != None):
                count = count + 1

            if(Project_obj.project_url_for_2 != None):
                count = count + 1

            if(Project_obj.project_url_for_3 != None):
                count = count + 1

            if(Project_obj.project_url_for_4 != None):
                count = count + 1
            
            return render(request,'admin/project/edit-project-detail.html',{'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj,'Project_obj':Project_obj,'count':count})
        if(request.session['userType'] == 'teacheR'):
            Project_obj = Project_Management.objects.get(id=id)
            employeeObj = employeeDetails.objects.all().order_by('-id')
            project_sector_MasterObj = project_sector_Master.objects.all().order_by('-id')
            project_type_MasterObj = project_type_Master.objects.all().order_by('-id')
            Project_Technology_MasterObj = Project_Technology_Master.objects.all().order_by('-id')

            count = 0
            if(Project_obj.project_url_for != None):
                count = count + 1
            if(Project_obj.project_url_for_1 != None):
                count = count + 1

            if(Project_obj.project_url_for_2 != None):
                count = count + 1

            if(Project_obj.project_url_for_3 != None):
                count = count + 1

            if(Project_obj.project_url_for_4 != None):
                count = count + 1
            
            return render(request,'admin/project/edit-project-detail.html',{'employeeObj':employeeObj,'project_sector_MasterObj':project_sector_MasterObj,'project_type_MasterObj':project_type_MasterObj,'Project_Technology_MasterObj':Project_Technology_MasterObj,'Project_obj':Project_obj,'count':count})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
    
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            projectName = request.POST['ProjectName']
            projectsSector = request.POST['ProjectSector']
            projectType = request.POST.getlist('ProjectTypeArray')
            projectTech = request.POST.getlist('ProjectTechnoloyArray')
            projectStartDate = request.POST.get('startDate').split('-')


            project_overview = request.POST['ProjectOverview']
            projectManagers = request.POST.getlist('ProjectManagersArray')
            projectTeamMember = request.POST.getlist('ProjectTeamArray')

            if(projectManagers == ['']):
                projectManagers = []

            if(projectTeamMember == ['']):
                projectTeamMember = []

            
            ProjectLogo =  request.FILES.get('ProjectLogo')
            print('ProjectLogo >>> ',ProjectLogo)


            UploadData =  request.FILES.get('upload_docs_0')
            UploadData_1 =  request.FILES.get('upload_docs_1')
            UploadData_2 =  request.FILES.get('upload_docs_2')
            UploadData_3 =  request.FILES.get('upload_docs_3')
            UploadData_4 =  request.FILES.get('upload_docs_4')



            urlType =  request.POST.get('upload_url_type_0')
            UrlData =  request.POST.get('upload_url_0')

            urlType_1 =  request.POST.get('upload_url_type_1')
            UrlData_1 =  request.POST.get('upload_url_1')

            urlType_2 =  request.POST.get('upload_url_type_2')
            UrlData_2 =  request.POST.get('upload_url_2')

            urlType_3 =  request.POST.get('upload_url_type_3')
            UrlData_3 =  request.POST.get('upload_url_4')

            urlType_4 =  request.POST.get('upload_url_type_4')
            UrlData_4 =  request.POST.get('upload_url_4')

            message = 'success'
            # try:
            projectSector_fk = project_sector_Master.objects.get(id=int(projectsSector))
            # project_typefk = employeeType_Master.objects.get(id=empType)
            # experience_year_fk = experience_Master.objects.get(id=experience)

            Project_obj = Project_Management.objects.get(id=id)
            Project_obj.project_name = projectName
            Project_obj.project_sector_FK = projectSector_fk
            Project_obj.project_type_fk = projectType
            Project_obj.project_technology_fk = projectTech
            # Project_obj.project_start_date = projectStartDate
            # Project_obj.project_due_date = projectDueDate
            Project_obj.project_overview = project_overview
            Project_obj.project_manager = projectManagers
            Project_obj.project_team_member = projectTeamMember

            if(ProjectLogo != None and ProjectLogo != ''):
                Project_obj.project_logo = ProjectLogo

            if(UploadData != None and UploadData != ''):
                Project_obj.upload_files = UploadData

            if(UploadData_1 != None and UploadData_1 != ''):
                Project_obj.upload_files_1 = UploadData_1

            if(UploadData_2 != None and UploadData_2 != ''):
                Project_obj.upload_files_2 = UploadData_2
            
            if(UploadData_3 != None and UploadData_3 != ''):
                Project_obj.upload_files_3 = UploadData_3
            
            if(UploadData_4 != None and UploadData_4 != ''):
                Project_obj.upload_files_4 = UploadData_4

            if(urlType == ''):
                urlType = None
            if(UrlData == ''):
                UrlData = None
            Project_obj.project_url_for = urlType
            Project_obj.project_url = UrlData

            if(urlType_1 == ''):
                urlType_1 = None
            if(UrlData_1 == ''):
                UrlData_1 = None
            Project_obj.project_url_for_1 = urlType_1
            Project_obj.project_url_1 = UrlData_1

            if(urlType_2 == ''):
                urlType_2 = None
            if(UrlData_2 == ''):
                UrlData_2 = None
            Project_obj.project_url_for_2 = urlType_2
            Project_obj.project_url_2 = UrlData_2

            if(urlType_3 == ''):
                urlType_3 = None
            if(UrlData_3 == ''):
                UrlData_3 = None
            Project_obj.project_url_for_3 = urlType_3
            Project_obj.project_url_3 = UrlData_3

            if(urlType_4 == ''):
                urlType_4 = None
            if(UrlData_4 == ''):
                UrlData_4 = None
            Project_obj.project_url_for_4 = urlType_4
            Project_obj.project_url_4 = UrlData_4

            Project_obj.save()
            # except:
            #     message = 'fail'

            return JsonResponse({'response':message})


        if(request.session['userType'] == 'teacheR'):

            projectStartDate = request.POST.get('endDate').split('-')
            project_overview = request.POST['ProjectOverview']
            projectTeamMember = request.POST.getlist('ProjectTeamArray')

            if(projectTeamMember == ['']):
                projectTeamMember = []

            
            ProjectLogo =  request.FILES.get('ProjectLogo')


            UploadData =  request.FILES.get('upload_docs_0')
            UploadData_1 =  request.FILES.get('upload_docs_1')
            UploadData_2 =  request.FILES.get('upload_docs_2')
            UploadData_3 =  request.FILES.get('upload_docs_3')
            UploadData_4 =  request.FILES.get('upload_docs_4')



            urlType =  request.POST.get('upload_url_type_0')
            UrlData =  request.POST.get('upload_url_0')

            urlType_1 =  request.POST.get('upload_url_type_1')
            UrlData_1 =  request.POST.get('upload_url_1')

            urlType_2 =  request.POST.get('upload_url_type_2')
            UrlData_2 =  request.POST.get('upload_url_2')

            urlType_3 =  request.POST.get('upload_url_type_3')
            UrlData_3 =  request.POST.get('upload_url_4')

            urlType_4 =  request.POST.get('upload_url_type_4')
            UrlData_4 =  request.POST.get('upload_url_4')

            message = 'success'
            # try:
            # project_typefk = employeeType_Master.objects.get(id=empType)
            # experience_year_fk = experience_Master.objects.get(id=experience)

            Project_obj = Project_Management.objects.get(id=id)
            Project_obj.project_team_member = projectTeamMember

            if(ProjectLogo != None and ProjectLogo != ''):
                Project_obj.project_logo = ProjectLogo

            if(UploadData != None and UploadData != ''):
                Project_obj.upload_files = UploadData

            if(UploadData_1 != None and UploadData_1 != ''):
                Project_obj.upload_files_1 = UploadData_1

            if(UploadData_2 != None and UploadData_2 != ''):
                Project_obj.upload_files_2 = UploadData_2
            
            if(UploadData_3 != None and UploadData_3 != ''):
                Project_obj.upload_files_3 = UploadData_3
            
            if(UploadData_4 != None and UploadData_4 != ''):
                Project_obj.upload_files_4 = UploadData_4

            if(urlType == ''):
                urlType = None
            if(UrlData == ''):
                UrlData = None
            Project_obj.project_url_for = urlType
            Project_obj.project_url = UrlData

            if(urlType_1 == ''):
                urlType_1 = None
            if(UrlData_1 == ''):
                UrlData_1 = None
            Project_obj.project_url_for_1 = urlType_1
            Project_obj.project_url_1 = UrlData_1

            if(urlType_2 == ''):
                urlType_2 = None
            if(UrlData_2 == ''):
                UrlData_2 = None
            Project_obj.project_url_for_2 = urlType_2
            Project_obj.project_url_2 = UrlData_2

            if(urlType_3 == ''):
                urlType_3 = None
            if(UrlData_3 == ''):
                UrlData_3 = None
            Project_obj.project_url_for_3 = urlType_3
            Project_obj.project_url_3 = UrlData_3

            if(urlType_4 == ''):
                urlType_4 = None
            if(UrlData_4 == ''):
                UrlData_4 = None
            Project_obj.project_url_for_4 = urlType_4
            Project_obj.project_url_4 = UrlData_4

            Project_obj.save()
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')




@login_required(login_url='/')
def filter_project(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            filterByStatus = request.GET['filterByStatus'] 
            filterByProject = request.GET['filterByProject'] 
            filterByProgress = request.GET['filterByProgress']
            filterByEmployee = request.GET['filterByEmployee']
            filterByProjectSector = request.GET['filterByProjectSector']
            filterByProjectType = request.GET['filterByProjectType']
            filterByLanguage = request.GET['filterByLanguage']

            print('filterByStatus  >>>> ',filterByStatus)
            print('filterByProject  >>>> ',filterByProject)        
            print('filterByProgress  >>>> ',filterByProgress)        
            print('filterByEmployee  >>>> ',filterByEmployee)        
            print('filterByProjectSector  >>>> ',filterByProjectSector)        
            print('filterByProjectType  >>>> ',filterByProjectType)        
            print('filterByLanguage  >>>> ',filterByLanguage)        

        if(request.session['userType'] == 'teacheR'):
            filterByStatus = request.GET['filterByStatus'] 
            filterByProject = request.GET['filterByProject'] 
            filterByProgress = request.GET['filterByProgress']
            filterByEmployee = request.GET['filterByEmployee']
            filterByProjectSector = request.GET['filterByProjectSector']
            filterByProjectType = request.GET['filterByProjectType']
            filterByLanguage = request.GET['filterByLanguage']


            print('filterByStatus  >>>> ',filterByStatus)
            print('filterByProject  >>>> ',filterByProject)        
            print('filterByProgress  >>>> ',filterByProgress)        
            print('filterByEmployee  >>>> ',filterByEmployee)        
            print('filterByProjectSector  >>>> ',filterByProjectSector)        
            print('filterByProjectType  >>>> ',filterByProjectType)        
            print('filterByLanguage  >>>> ',filterByLanguage)        

            
          
            
        if(request.session['userType'] == 'studdenT'):
            filterByStatus = request.GET['filterByStatus'] 
            filterByProject = request.GET['filterByProject'] 
            filterByProgress = request.GET['filterByProgress']
            filterByEmployee = request.GET['filterByEmployee']
            filterByProjectSector = request.GET['filterByProjectSector']
            filterByProjectType = request.GET['filterByProjectType']
            filterByLanguage = request.GET['filterByLanguage']


            print('filterByStatus  >>>> ',filterByStatus)
            print('filterByProject  >>>> ',filterByProject)        
            print('filterByProgress  >>>> ',filterByProgress)        
            print('filterByEmployee  >>>> ',filterByEmployee)        
            print('filterByProjectSector  >>>> ',filterByProjectSector)        
            print('filterByProjectType  >>>> ',filterByProjectType)        
            print('filterByLanguage  >>>> ',filterByLanguage)        

 

#############################################################################################################################
  # All data show
        if request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.all()
           data = get_project_accurate_data(projectname)
           return JsonResponse({'data':data})

    # First Condition Filter by status
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           return JsonResponse({'data':list(data)})

    # singal Condition Started  filterByProject
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(id=filterByProject)
           data = get_project_accurate_data(projectname)
           return JsonResponse({'data':list(data)})
    # singal condition for filter by inprogress  name 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           return JsonResponse({'data':list(data)})

    # singal condition filter for employee  name 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee)
           data = get_project_accurate_data(projectname)
           return JsonResponse({'data':list(data)})

    # singal condition for selecter  name 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector))
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # singal condition for Filter by Type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # singal condition for Filter by Language/Framework  
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #Second  Condition Filter by status & filterByProject
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #Second  Condition Filter by status & filterByProgress
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  

    #Second  Condition Filter by status & filterByEmployee  
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Second  Condition Filter by status & filterByProjectSector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Second  Condition Filter by status & filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Second  Condition Filter by status & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #project name & filter progress
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_progress__range=filterByProgress,project_name=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  

    #project name & Employee
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #project name & selector
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # project name & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(id=filterByProject,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # project name & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    # filter progress & employee
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filter progress & selector
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filter progress & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filter progress & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    # employee & selecter
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector)) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector))
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # employee & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # employee & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    # selector & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
           
    # selector & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filtertype & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filterByProject & SELECTOR & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # PROJECT NAME & EMP & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,id=filterByProject,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #STATU & PROGRESS & TYPE
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #STATU & PROGRESS & LANGUAGE
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})


    #FILTER EMP & SECTOR  & LANGUAGE 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #FILTER PROGRESS & LANGUAGE & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Second  Condition Filter by status & filterByEmployee & SECTOR
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #FILTER STATUS & LANGUAGE & FILTER BY PROECT & SECTOR
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #FILTER STATUS & TYPE & FILTER BY PROECT & SECTOR
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status & filterByEmployee & SECTOR & LANGUAGE 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})


    #Third Condition Filter by status & filterByProject & filterByProgress
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #status & filterByProject & TYPE & LANGUAGE 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & TYPE & LANGUAGE & slector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})           

    #filterByProgress & EMP & PROJECT TYPE & LANGUAGE 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #filterByProgress & EMP & project name & PROJECT TYPE & LANGUAGE 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #status & filterByProgress & EMP & project name & PROJECT TYPE & LANGUAGE 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByProgress & EMPLOYEE
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
           
    #Third Condition Filter by status & filterByProject & filterByProgress & slector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByProgress & filter type 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status & filterByProject & Sector & Type & Progress 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByProgress & language
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #PROJECT NAME & FILTER PROGRESS & EMP & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #PROJECT NAME & FILTER PROGRESS & EMP & SELECTOR
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #PROJECT NAME & FILTER PROGRESS & EMP & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #PROJECT NAME & FILTER PROGRESS & EMP & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    # FILTER PROGRESS & EMP & SELECTOR 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})


    # FILTER PROGRESS & EMP & SELECTOR & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # FILTER PROGRESS & EMP & SELECTOR & FILTER TYPE 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # FILTER PROGRESS & EMP & SELECTOR & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # EMP & SELECTOR & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # EMP & SELECTOR & FILTER TYPE & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
        
    # EMP & SELECTOR & FILTER TYPE & PROJECT NAME
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # EMP & SELECTOR & FILTER TYPE & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    # SELECTOR & FILTER TYPE & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    # SELECTOR & FILTER TYPE & LANGUAGE & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # SELECTOR & FILTER TYPE & LANGUAGE & PROJECT NAME 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
        
    # SELECTOR & FILTER TYPE & LANGUAGE  & PROGRESS
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # STATUS & PROGRESS & SECTOR
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # STATUS & PROGRESS & SECTOR & PROJECT NAME 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    # STATUS & PROGRESS & SECTOR & PROJECT NAME & EMP 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #status & filterByProjectType & filterByLanguage & filterByProgress & filterByProject
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filterByProjectType & filterByLanguage & filterByProgress & emp &
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
  
    # filterByProjectType & filterByLanguage & filterByProgress & filterByProject
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByEmployee 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByProjectSector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Third Condition Filter by status & filterByProject & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #Project name & Filter progress & employee
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_progress__range=filterByProgress,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_progress__range=filterByProgress,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Project name & Filter progress & SELECTOR
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Project name & Filter progress & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Project name & Filter & progress & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_technology_fk__icontains=filterByLanguage,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # Filter progress & EMPLOYEE & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})   
    
    # Filter progress & EMPLOYEE & SELECTOR 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
           
    # Filter progress & EMPLOYEE & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Filter progress & EMPLOYEE & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #EMPLOYEE & SELECTOR & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #EMPLOYEE & SELECTOR & PROJECT NAME
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #EMPLOYEE & SELECTOR & FILTER TYPE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #EMPLOYEE & SELECTOR & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #SELECTOR & FILTER TYPE & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #SELECTOR & FILTER TYPE & PROJECT NAME 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #SELECTOR & FILTER TYPE & PROGRESS
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #SELECTOR & FILTER TYPE & PROGRESS
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #status & progress & project type & sector 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress,project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  

    #status & progress & project type & LANGUAGE & EMP 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress,project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress,project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  
    
    #PROJECT NAME & project type & LANGUAGE & EMP 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,id=filterByProject,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 
    
    #status & PROJECT NAME & sector & LANGUAGE & EMP 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #status & PROJECT NAME & sector & LANGUAGE & EMP & type 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #PROJECT NAME & sector  & LANGUAGE & EMP 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #status & type & progress & language & emp
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_progress__range=filterByProgress,project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  

    #Condition filterByProject & filterByProgress & filterByProjectSector & type 
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})   

    #status & filterByProject & emp & filterByProjectSector & type 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_team_member__icontains=filterByEmployee,project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject) | Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_manager__icontains=filterByEmployee,project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})  

    #status & filterByProject & emp & filterByProjectSector & type & progress 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_team_member__icontains=filterByEmployee,project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_manager__icontains=filterByEmployee,project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})         

    #Fourth Condition Filter by status & filterByProject & filterByProgress & filterByEmployee
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Fourth Condition Filter by status & filterByProject & filterByProgress & filterByProjectSector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
       
    #Fourth Condition Filter by status & filterByProject & filterByProgress & filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #Fourth Condition Filter by status & filterByProject & filterByProgress & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)}) 

    #fivith Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectSector
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})


    #fivith Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #fivith Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Sixe Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectSector 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status & filterByProject & filterByProgress & filterByEmployee &  filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & language
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status & filterByProject & filterByProgress & filterByProjectSector & type & language 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition Filter by status &  filterByProgress & filterByProjectSector & type & language 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByProject & filterByProgress & filterByEmployee & selector & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByProject & filterByProgress & filterByEmployee & selector & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),id=filterByProject,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByProgress & filterByEmployee & selector & filter type
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #Condition filterByProgress & filterByEmployee & selector & filter type & status
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByProgress & filterByEmployee & selector & filter type & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_status=filterByStatus,project_progress__range=filterByProgress,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByEmployee & selector & filter type & language
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByEmployee & selector & filter type & language & status 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,project_status=filterByStatus)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #filterByProject & filterByProgress & filterByEmployee & filterByProjectSector & FILTER TYPE & LANGUAGE
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,id=filterByProject,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,id=filterByProject,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Condition filterByEmployee & selector & filter type & language & project name
        elif request.GET['filterByStatus'] == 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,id=filterByProject) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,id=filterByProject)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #status & filterByProjectType & filterByLanguage 
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] == 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})
    
    #status & filterByProjectType & filterByLanguage & filterByProgress
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] == 'All' and request.GET['filterByProjectSector'] == 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Sixe Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectSector & filterByProjectType
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] == 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType) | Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    #Sixe Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectSector & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] == 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # filterByProgress & filterByEmployee & filterByProjectSector & FILTER TYPE & LANGUAGE & STATUS
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] == 'All'\
            and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All'\
           == 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress) | Project_Management.objects.filter(project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_status=filterByStatus,project_technology_fk__icontains=filterByLanguage,project_progress__range=filterByProgress)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    # Sixe Condition Filter by status & filterByProject & filterByProgress & filterByEmployee & filterByProjectSector & filterByProjectType & filterByLanguage
        elif request.GET['filterByStatus'] != 'All' and request.GET['filterByProject'] != 'All' and request.GET['filterByProgress'] != 'All' and request.GET['filterByEmployee'] != 'All' and request.GET['filterByProjectSector'] != 'All' and request.GET['filterByProjectType'] != 'All' and request.GET['filterByLanguage'] != 'All':
           filterByProgress = filterByProgress.split('-')
           projectname = Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_team_member__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage) | Project_Management.objects.filter(project_status=filterByStatus,id=filterByProject,project_progress__range=filterByProgress,project_manager__icontains=filterByEmployee,project_sector_FK=project_sector_Master.objects.get(id=filterByProjectSector),project_type_fk__icontains=filterByProjectType,project_technology_fk__icontains=filterByLanguage)
           data = get_project_accurate_data(projectname)
           print('data >>> ',data)
           return JsonResponse({'data':list(data)})

    
# --------------------------------------------------------------------------------------------------------------------------------
        
        else:
            filterByProgress = filterByProgress.split('-')
            projectname = Project_Management.objects.filter()
            data = get_project_accurate_data(projectname)
            print('data >>> ',data)
            return JsonResponse({'data':list(data)})




@login_required(login_url='/')
def create_module(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')
            return render(request,'admin/project/add-modules.html',{'projectObj':projectObj})
        if(request.session['userType'] == 'teacheR'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))
            return render(request,'admin/project/add-modules.html',{'projectObj':projectObj})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            projectID = request.POST['projectFk']
            moduleNameArray = request.POST.getlist('moduleName[]')
            moduleDescArray = request.POST.getlist('moduleDescription[]')

            print('project_fk >>> ',projectID)
            print('moduleNameArray >>> ',moduleNameArray)
            print('moduleDescArray >>> ',moduleDescArray)

            message = 'success'
            project_fk = Project_Management.objects.get(id=int(projectID))
            try:
                for i in range(len(moduleNameArray)):
                    obj1 = Module_management(projectFK = project_fk,moduleName=moduleNameArray[i],module_desc = moduleDescArray[i])
                    obj1.save()
            except:
                message = 'fail'

            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            projectID = request.POST['projectFk']
            moduleNameArray = request.POST.getlist('moduleName[]')
            moduleDescArray = request.POST.getlist('moduleDescription[]')

            print('project_fk >>> ',projectID)
            print('moduleNameArray >>> ',moduleNameArray)
            print('moduleDescArray >>> ',moduleDescArray)

            message = 'success'
            project_fk = Project_Management.objects.get(id=int(projectID))
            try:
                for i in range(len(moduleNameArray)):
                    obj1 = Module_management(projectFK = project_fk,moduleName=moduleNameArray[i],module_desc = moduleDescArray[i])
                    obj1.save()
            except:
                message = 'fail'

            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')





@login_required(login_url='/')
def create_sub_module(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')
            return render(request,'admin/project/add-sub-modules.html',{'projectObj':projectObj})

        if(request.session['userType'] == 'teacheR'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))
            return render(request,'admin/project/add-sub-modules.html',{'projectObj':projectObj})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            projectID = request.POST['projectID']
            moduleID = request.POST['moduleFk']
            subModuleNameArray = request.POST.getlist('subModuleName[]')
            subModuleDescArray = request.POST.getlist('subModuleDescription[]')

            print('project_fk >>> ',projectID)
            print('moduleID >>> ',moduleID)
            print('subModuleNameArray >>> ',subModuleNameArray)
            print('subModuleDescArray >>> ',subModuleDescArray)

            message = 'success'
            project_fk = Project_Management.objects.get(id=int(projectID))
            module_fk = Module_management.objects.get(id=int(moduleID))

            try:
                for i in range(len(subModuleNameArray)):
                    obj1 = Sub_module_management(projectFK = project_fk,moduleFK=module_fk,subModuleName=subModuleNameArray[i],subModule_desc = subModuleDescArray[i])
                    obj1.save()
            except:
                message = 'fail'

            return JsonResponse({'response':message})
        if(request.session['userType'] == 'teacheR'):
            projectID = request.POST['projectID']
            moduleID = request.POST['moduleFk']
            subModuleNameArray = request.POST.getlist('subModuleName[]')
            subModuleDescArray = request.POST.getlist('subModuleDescription[]')

            print('project_fk >>> ',projectID)
            print('moduleID >>> ',moduleID)
            print('subModuleNameArray >>> ',subModuleNameArray)
            print('subModuleDescArray >>> ',subModuleDescArray)

            message = 'success'
            project_fk = Project_Management.objects.get(id=int(projectID))
            module_fk = Module_management.objects.get(id=int(moduleID))

            try:
                for i in range(len(subModuleNameArray)):
                    obj1 = Sub_module_management(projectFK = project_fk,moduleFK=module_fk,subModuleName=subModuleNameArray[i],subModule_desc = subModuleDescArray[i])
                    obj1.save()
            except:
                message = 'fail'
            
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')



@login_required(login_url='/')
def module_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')

        elif(request.session['userType'] == 'teacheR'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))

        else:
            return redirect('unautorizedaccess')

        return render(request,'admin/project/project-modules-list.html',{'projectObj':projectObj})


@login_required(login_url='/')
def get_selected_project_module_list(request,id):
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
            return JsonResponse({'response':listObj})
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
            return JsonResponse({'response':listObj})
            
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
            return JsonResponse({'response':listObj})



@login_required(login_url='/')
def sub_module_list(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')

        elif(request.session['userType'] == 'teacheR'):
            employeeFk = employeeDetails.objects.get(userFK=request.user)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))

        else:
            return redirect('unautorizedaccess')
        return render(request,'admin/project/project-sub-modules-list.html',{'projectObj':projectObj})



@login_required(login_url='/')
def get_selected_project_subModule_list(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            moduleObj = Module_management.objects.get(id = int(id))
            project_fk = Project_Management.objects.get(id=int(moduleObj.projectFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)

            listObj = []
            for i in subModule_obj:
                context = {}
                context['mod_id'] = i.moduleFK.id
                context['mod_name'] = i.moduleFK.moduleName.capitalize()
                context['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context['subMod_id'] = i.id
                context['subModuleName'] = i.subModuleName.capitalize()
                context['subModuleDescription'] = i.subModule_desc.capitalize()
                context['projectName'] = project_fk.project_name.capitalize()
                context['projectid'] = project_fk.id


                listObj.append(context)
            return JsonResponse({'response':listObj})
        if(request.session['userType'] == 'teacheR'):
            moduleObj = Module_management.objects.get(id = int(id))
            project_fk = Project_Management.objects.get(id=int(moduleObj.projectFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)

            listObj = []
            for i in subModule_obj:
                context = {}
                context['mod_id'] = i.moduleFK.id
                context['mod_name'] = i.moduleFK.moduleName.capitalize()
                context['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context['subMod_id'] = i.id
                context['subModuleName'] = i.subModuleName.capitalize()
                context['subModuleDescription'] = i.subModule_desc.capitalize()
                context['projectName'] = project_fk.project_name.capitalize()
                context['projectid'] = project_fk.id


                listObj.append(context)
            return JsonResponse({'response':listObj})
            
        if(request.session['userType'] == 'studdenT'):
            moduleObj = Module_management.objects.get(id = int(id))
            project_fk = Project_Management.objects.get(id=int(moduleObj.projectFK.id))
            subModule_obj = Sub_module_management.objects.filter(projectFK=project_fk,moduleFK=moduleObj)

            listObj = []
            for i in subModule_obj:
                context = {}
                context['mod_id'] = i.moduleFK.id
                context['mod_name'] = i.moduleFK.moduleName.capitalize()
                context['mod_desc'] = i.moduleFK.module_desc.capitalize()
                context['subMod_id'] = i.id
                context['subModuleName'] = i.subModuleName.capitalize()
                context['subModuleDescription'] = i.subModule_desc.capitalize()
                context['projectName'] = project_fk.project_name.capitalize()
                context['projectid'] = project_fk.id


                listObj.append(context)
            return JsonResponse({'response':listObj})


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def checkProject(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchData = request.GET['searchData']
            message = 'success'
            if(Project_Management.objects.filter(project_name=searchData)):
                message = 'Project exist'
            
            return JsonResponse({'response':message})
        if(request.session['userType'] == 'teacheR'):
            searchData = request.GET['searchData']
            message = 'success'
            if(Project_Management.objects.filter(project_name=searchData)):
                message = 'Project exist'
            
            return JsonResponse({'response':message})
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def deleteProject(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.get(id=int(id))
            projectObj.delete()
            return redirect('project_list')
        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def check_module_name(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.GET['projectfk']
            moduleName = request.GET['searchData']

            project_obj = Project_Management.objects.get(id=int(projectObj))

            message = 'success'
            if(Module_management.objects.filter(projectFK=project_obj,moduleName = moduleName)):
                message = 'fail'
            return JsonResponse({'response':message})
        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def check_submodule_name(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.GET['projectfk']
            moduleObj = request.GET['modulefk']
            submoduleName = request.GET['searchData']

            project_obj = Project_Management.objects.get(id=int(projectObj))
            module_obj = Module_management.objects.get(id=int(moduleObj))


            message = 'success'
            if(Sub_module_management.objects.filter(projectFK=project_obj,moduleFK = module_obj,subModuleName=submoduleName)):
                message = 'fail'
            return JsonResponse({'response':message})

        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def edit_module(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.POST['projectFK']
            moduleObj = request.POST['moduleFK']
            moduleText = request.POST['moduleText']
            moduleDesc = request.POST['moduleDescription']


            project_obj = Project_Management.objects.get(id=int(projectObj))
            module_obj = Module_management.objects.get(id=int(moduleObj))

            print('projectObj >>> ',projectObj)
            print('moduleObj >>> ',moduleObj)
            print('moduleText >>> ',moduleText)
            print('moduleDesc >>> ',moduleDesc)

            print('project_obj >>> ',project_obj)
            print('module_obj >>> ',module_obj)

            message = 'success'
            try:
                module_obj.moduleName=moduleText.strip()
                module_obj.module_desc=moduleDesc.strip()
                module_obj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})

        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def delete_module(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.GET['projectFK']
            moduleObj = request.GET['moduleFK']


            project_obj = Project_Management.objects.get(id=int(projectObj))
            message = 'success'
            try:
                module_obj = Module_management.objects.get(projectFK=project_obj,id=int(moduleObj))
                module_obj.delete()
            except:
                message = 'fail'
            return JsonResponse({'response':message})

        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def force_update_project_status(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            project_obj = Project_Management.objects.get(id=int(id))
            projectStatus = request.POST['projectStatus']


            message = 'success'
            try:
                project_obj.project_status_force_update = projectStatus
                project_obj.save()

            except:
                message = 'fail'
            return JsonResponse({'response':message})

        if(request.session['userType'] == 'teacheR'):
            return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')
    else:
        return redirect('unautorizedaccess')


# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def edit_submodule(request):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.POST['projectFK']
            moduleObj = request.POST['moduleFK']
            subObj = request.POST['submoduleFK']
            moduleText = request.POST['submoduleText']
            moduleDesc = request.POST['submoduleDescription']

            print('projectObj >>> ',projectObj)
            print('moduleObj >>> ',moduleObj)
            print('subObj >>> ',subObj)

            print('moduleText >>> ',moduleText)
            print('moduleDesc >>> ',moduleDesc)

            project_obj = Project_Management.objects.get(id=int(projectObj))
            module_obj = Module_management.objects.get(id=int(moduleObj))

            subMod_obj = Sub_module_management.objects.get(projectFK = projectObj,moduleFK=moduleObj,id=int(subObj))



            message = 'success'
            try:
                subMod_obj.subModuleName=moduleText.strip()
                subMod_obj.subModule_desc=moduleDesc.strip()
                subMod_obj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})

        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
@login_required(login_url='/')
def delete_submodule(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR' or request.session['userType'] == 'teacheR'):
            projectObj = request.GET['projectFK']
            moduleObj = request.GET['moduleFK']
            submoduleObj = request.GET['submoduleFK']



            project_obj = Project_Management.objects.get(id=int(projectObj))
            module_obj = Module_management.objects.get(id=int(moduleObj))

            message = 'success'
            try:
                subMod_obj = Sub_module_management.objects.get(projectFK = project_obj,moduleFK=module_obj,id=int(submoduleObj))
                subMod_obj.delete()
            except:
                message = 'fail'
            return JsonResponse({'response':message})

        # if(request.session['userType'] == 'teacheR'):
        #     return redirect('unautorizedaccess')
            
        if(request.session['userType'] == 'studdenT'):
            return redirect('unautorizedaccess')

# ##########################################################################################################
# ##########################################################################################################
#                                      FILTER DATA - FUNCTION()
# ##########################################################################################################
def get_project_accurate_data(projectListArray):
    dataArray = []
    print('projectListArray >>> ',projectListArray)
    for i in projectListArray:
        dataDict = {}
        print('i data >>> ',i.project_name)
        dataDict['project_id'] = i.id
        dataDict['project_name'] = i.project_name
        dataDict['project_description'] = i.project_overview

        teamList = []
        data = ' | '
        if(i.project_manager != '[]'):
            projectManagerData = eval(i.project_manager)[0].split(',')
            for j in projectManagerData:
                data = data + str(employeeDetails.objects.get(id=j).employee_name)+' | '
        dataDict['projectManagerName'] = data

        if(i.project_team_member != '[]'):
            projectTeam = eval(i.project_team_member)
            if(len(projectTeam) > 0):
                projectTeam = projectTeam[0].split(',')
            for j in projectTeam:
                context = {}
                data = employeeDetails.objects.get(id=j)
                context['empName'] = data.employee_name
                context['empImg'] = str(data.profile_image)
                teamList.append(context)

        dataDict['teamList'] = teamList
        dataDict['total_module'] = len(Module_management.objects.filter(projectFK = i))
        dataDict['total_task'] = len(Task_Management.objects.filter(projectFK = i))
        dataDict['project_progress'] = i.project_progress
        dataDict['project_status'] = i.project_status
        dataDict['project_logo'] = str(i.project_logo)


        dataArray.append(dataDict)
    return dataArray
# ##########################################################################################################
@login_required(login_url='/')
def change_to_maintenace_mode(request,id):
    if request.method == 'POST':
        message = 'success'
        if(request.session['userType'] == 'masteR'):
            try:
                projectObj = Project_Management.objects.get(id=int(id))
                projectObj.project_to_maintenance = True
                projectObj.save()
            except:
                message = 'fail'

        elif(request.session['userType'] == 'teacheR'):
            try:
                projectObj = Project_Management.objects.get(id=int(id))
                projectObj.project_to_maintenance = True
                projectObj.save()
            except:
                message = 'fail'

        else:
            message = 'fail'

        return JsonResponse({'response':message})

# ##########################################################################################################
@login_required(login_url='/')
def change_to_development_mode(request,id):
    if request.method == 'POST':
        message = 'success'
        if(request.session['userType'] == 'masteR'):
            try:
                projectObj = Project_Management.objects.get(id=int(id))
                projectObj.project_to_maintenance = False
                projectObj.save()
            except:
                message = 'fail'

        elif(request.session['userType'] == 'teacheR'):
            try:
                projectObj = Project_Management.objects.get(id=int(id))
                projectObj.project_to_maintenance = False
                projectObj.save()
            except:
                message = 'fail'

        else:
            message = 'fail'

        return JsonResponse({'response':message})