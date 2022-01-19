from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models.project_model import Project_Management
from ..models.employee_model import employeeDetails
from django.contrib.auth.models import User
from ..models.file_model import file_management

# ##########################################################################################
# FILES lIST
# ##########################################################################################
@login_required(login_url='/')
def files_list(request):
    if request.method == 'GET':
        if request.session['userType'] == 'masteR':
            projectObj = Project_Management.objects.all().order_by('-id')
            fileObj = file_management.objects.all().order_by('-id')
            empObj = employeeDetails.objects.all().order_by('-id')
            return render(request,'admin/files/files-list.html',{'projectObj':projectObj,'fileObj':fileObj,'empObj':empObj})

        elif request.session['userType'] == 'teacheR':
            user_FK = User.objects.get(email=request.user)
            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))
            empObj = employeeDetails.objects.all().order_by('-id')
            fileList = []
            for i in projectObj:
                fileObj = file_management.objects.filter(projectFK=i)
                for j in fileObj:
                    context = {}
                    context['id'] = j.id
                    context['projectFK'] = j.projectFK
                    context['file_title'] = j.file_title
                    context['file_type'] = j.file_type
                    context['userFK'] = j.userFK
                    context['file'] = str(j.file)
                    fileList.append(context)
            return render(request,'admin/files/files-list.html',{'projectObj':projectObj,'fileObj':fileList,'empObj':empObj})
        
        elif request.session['userType'] == 'studdenT':
            user_FK = User.objects.get(email=request.user)
            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            projectObj = Project_Management.objects.filter(project_team_member__icontains = str(employeeFk.id))
            fileList = []
            for i in projectObj:
                fileObj = file_management.objects.filter(projectFK=i)
                for j in fileObj:
                    context = {}
                    context['id'] = j.id
                    context['projectFK'] = j.projectFK
                    context['file_title'] = j.file_title
                    context['file_type'] = j.file_type
                    context['userFK'] = j.userFK
                    context['file'] = str(j.file)
                    fileList.append(context)
            return render(request,'admin/files/files-list.html',{'projectObj':projectObj,'fileObj':fileList})
        
        else:
            return redirect('unautorizedaccess')
        
    else:
        return redirect('unautorizedaccess')


# ##########################################################################################
# FILES ADD
# ##########################################################################################
@login_required(login_url='/')
def add_files(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            projectObj = Project_Management.objects.all().order_by('-id')
            return render(request,'admin/files/add-new-files.html',{'projectObj':projectObj})

        if request.session['userType'] == 'teacheR':
            user_FK = User.objects.get(email=request.user)
            employeeFk = employeeDetails.objects.get(userFK=user_FK)
            projectObj = Project_Management.objects.filter(project_manager__icontains = str(employeeFk.id))
            return render(request,'admin/files/add-new-files.html',{'projectObj':projectObj})

        else:
            return redirect('unautorizedaccess')


    else:
        message = 'success'

        try:
            fileTitle = request.POST['file_title']
            project = request.POST['project']
            doc_type = request.POST['doc_type']
            uploaded_file = request.FILES['uploaded_file']

            fileObj = file_management(userFK=request.user,projectFK=Project_Management.objects.get(id=int(project)),file_title=fileTitle,file_type=doc_type,file=uploaded_file)
            fileObj.save()

        except:
            try:
                fileTitle = request.POST['file_title']
                # project = request.POST['project']
                doc_type = request.POST['doc_type']
                uploaded_file = request.FILES['uploaded_file']

                fileObj = file_management(userFK=request.user,file_title=fileTitle,file_type=doc_type,file=uploaded_file)
                fileObj.save()

            except:
                message = 'fail'

        return JsonResponse({'response':message})



# ##########################################################################################
# FILES DELETION
# ##########################################################################################
@login_required(login_url='/')
def delete_files(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            fileObj = file_management.objects.get(id=int(id))
            fileObj.delete()
            return redirect('files_list')

        if request.session['userType'] == 'teacheR':
            fileObj = file_management.objects.get(id=int(id))
            fileObj.delete()
            return redirect('files_list')

        else:
            return redirect('unautorizedaccess')
    else:
            return redirect('unautorizedaccess')

# ##########################################################################################
# ##########################################################################################
