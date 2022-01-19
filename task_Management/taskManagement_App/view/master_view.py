from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from ..models.master_models import designation_Master
from django.contrib.auth.decorators import login_required
from ..models.project_model import Project_Management
from ..models.employee_model import employeeDetails
from ..models.master_models import *
# ##########################################################################################################
#                                       DESIGNATION MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def designation_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            designationObj = designation_Master.objects.all()
            return render(request,'admin/master/designation-master.html',{'designationObj':designationObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = designation_Master(designation_name=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_designation_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = designation_Master.objects.get(id=int(id))
            context={'id':data.id,'designation_name':data.designation_name}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_designation_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = designation_Master.objects.filter(designation_name=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_designation_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            data = designation_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.designation_name = designationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_designation_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = designation_Master.objects.get(id=int(id))
            empObj = employeeDetails.objects.filter(designationFK=data)
            if(len(empObj)):
                return JsonResponse({'response':'Exist'})
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       QUALIFICATION MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def qualification_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            qualificationObj = qualification_Master.objects.all()
            return render(request,'admin/master/qualification-master.html',{'qualificationObj':qualificationObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = qualification_Master(qualification_type=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_qualification_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = qualification_Master.objects.get(id=int(id))
            context={'id':data.id,'qualification_name':data.qualification_type}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_qualification_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = qualification_Master.objects.filter(qualification_type=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_qualification_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['qualificationText']
            data = qualification_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.qualification_type = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_qualification_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = qualification_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       PROJECT SECTOR MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def project_sector_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            project_sector_MasterObj = project_sector_Master.objects.all()
            print('project_sector_Master >>> ',project_sector_MasterObj)
            return render(request,'admin/master/project-sector-master.html',{'project_sector_MasterObj':project_sector_MasterObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = project_sector_Master(sector=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_project_sector_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = project_sector_Master.objects.get(id=int(id))
            context={'id':data.id,'sector_name':data.sector}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_project_sector_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = project_sector_Master.objects.filter(sector=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_project_sector_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['sectorText']
            data = project_sector_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.sector = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_project_sector_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = project_sector_Master.objects.get(id=int(id))
            projectSectorObj = Project_Management.objects.filter(project_sector_FK=data)
            if(len(projectSectorObj)):
                return JsonResponse({'response':'Exist'})
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       PROJECT TYPE MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def project_type_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            project_type_MasterObj = project_type_Master.objects.all()
            return render(request,'admin/master/project-type-master.html',{'project_type_MasterObj':project_type_MasterObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['projectTypeText']
            message = 'success'
            try:
                designationObj = project_type_Master(projectType=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_project_type_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = project_type_Master.objects.get(id=int(id))
            context={'id':data.id,'sector_name':data.projectType}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_project_type_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = project_type_Master.objects.filter(projectType=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_project_type_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['sectorText']
            data = project_type_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.projectType = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_project_type_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = project_type_Master.objects.get(id=int(id))
            project_type_fkObj = Project_Management.objects.filter(project_type_fk__icontains=id)
            if(len(project_type_fkObj)):
                return JsonResponse({'response':'Exist'})
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       PROJECT TYPE MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def project_tech_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            project_tech_MasterObj = Project_Technology_Master.objects.all()
            return render(request,'admin/master/project-technology-master.html',{'project_tech_MasterObj':project_tech_MasterObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['Technology']
            message = 'success'
            try:
                designationObj = Project_Technology_Master(Technology=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_project_tech_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = Project_Technology_Master.objects.get(id=int(id))
            context={'id':data.id,'sector_name':data.Technology}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_project_tech_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = Project_Technology_Master.objects.filter(Technology=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_project_tech_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['sectorText']
            data = Project_Technology_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.Technology = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_project_tech_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = Project_Technology_Master.objects.get(id=int(id))
            project_type_fkObj = Project_Management.objects.filter(project_technology_fk__icontains=id)
            if(len(project_type_fkObj)):
                return JsonResponse({'response':'Exist'})
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       EVENT HIGHLIGHT MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def event_highlight_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            event_highlight_MasterObj = event_highlight_Master.objects.all()
            return render(request,'admin/master/event-highlights-master.html',{'event_highlight_MasterObj':event_highlight_MasterObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['highlightText']
            message = 'success'
            try:
                designationObj = event_highlight_Master(highlight_name=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_event_highlight_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = event_highlight_Master.objects.get(id=int(id))
            context={'id':data.id,'sector_name':data.highlight_name}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_event_highlight_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = event_highlight_Master.objects.filter(highlight_name=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_event_highlight_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['highlightText']
            data = event_highlight_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.highlight_name = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_event_highlight_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = event_highlight_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       CULTURAL EVENT MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def cultural_event_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            cultural_event_MasterObj = culturalEvent_Master.objects.all()
            print('cultural_event_MasterObj >>> ',cultural_event_MasterObj)
            return render(request,'admin/master/cultural-events-master.html',{'cultural_event_MasterObj':cultural_event_MasterObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['highlightText']
            message = 'success'
            try:
                designationObj = culturalEvent_Master(event_name=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_cultural_event_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = culturalEvent_Master.objects.get(id=int(id))
            context={'id':data.id,'sector_name':data.event_name}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_cultural_event_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = culturalEvent_Master.objects.filter(event_name=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_cultural_event_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            qualificationText = request.POST['highlightText']
            data = culturalEvent_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.event_name = qualificationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_cultural_event_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = culturalEvent_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       DOCUMENT TYPE MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def documentType_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            designationObj = document_Master.objects.all()
            return render(request,'admin/master/document-type-master.html',{'designationObj':designationObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = document_Master(document_type=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_documentType_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = document_Master.objects.get(id=int(id))
            context={'id':data.id,'designation_name':data.document_type}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_documentType_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = document_Master.objects.filter(document_type=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_documentType_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            data = document_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.document_type = designationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_documentType_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = document_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       PASSING YEAR MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def passingYear_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            designationObj = passingYear_Master.objects.all()
            return render(request,'admin/master/passing-year-master.html',{'designationObj':designationObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = passingYear_Master(passingYear=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_passingYear_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = passingYear_Master.objects.get(id=int(id))
            context={'id':data.id,'designation_name':data.passingYear}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_passingYear_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = passingYear_Master.objects.filter(passingYear=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_passingYear_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            data = passingYear_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.passingYear = designationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_passingYear_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = passingYear_Master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# ##########################################################################################################
#                                       LOCATION MASTER VIEW
# ##########################################################################################################
@login_required(login_url='/')
def location_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            locationObj = Location_master.objects.all()
            return render(request,'admin/master/location-master.html',{'designationObj':locationObj})
        else:
            return redirect('unautorizedaccess')
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            message = 'success'
            try:
                designationObj = Location_master(location=designationText)
                designationObj.save()
            except:
                message = 'fail'
            return JsonResponse({'response':message})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def get_specific_location_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = Location_master.objects.get(id=int(id))
            context={'id':data.id,'designation_name':data.location}
            return JsonResponse({'response':context})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def check_location_master(request):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            searchString = request.GET.getlist('search_string')
            data = Location_master.objects.filter(location=searchString)
            messages = 'not-exist'
            if(len(data)>0):
                messages="exist"
            return JsonResponse({'response':messages})
        else:
            return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def edit_location_master(request,id):
    if request.method == 'POST':
        if(request.session['userType'] == 'masteR'):
            designationText = request.POST['designationText']
            data = Location_master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.location = designationText
                data.save()
            except:
                messages="fail"
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
# .......................................................................................................
# .......................................................................................................
@login_required(login_url='/')
def delete_location_master(request,id):
    if request.method == 'GET':
        if(request.session['userType'] == 'masteR'):
            data = Location_master.objects.get(id=int(id))
            messages = 'success'
            try:
                data.delete()
            except:
                messages = 'fail'
            return JsonResponse({'response':messages})
    else:
        return redirect('unautorizedaccess')
