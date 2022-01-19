// localStorage.setItem('projectFK',projectFk);
if(localStorage.hasOwnProperty("projectFK")){
    localStorage.removeItem("projectFK");
}
// ########################################################################################################################################
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// ########################################################################################################################################
// ########################################################################################################################################
function createTask(){
    // var projectFk = $('#projectsData').val();
    if(localStorage.hasOwnProperty("projectFK")){
        var projectFK = localStorage.getItem('projectFK');
        // localStorage.removeItem("projectFK");
    }else{
        alert('Select valid Project!');
        return false;
    }

    var moduleFk = $('#modulesData').val();
    var subModuleFk = $('#submodulesData').val();

    var taskTitle = $('#task-title').val();

    var dueDate = $('#datepicker').val();
    var dueTime = $('#dueTime').val();
    var priority = $('#task-priority2').val();
    var employeeFK = $('#employeeFK').val();

    var taskDescription = $('#taskDescription').val();

    // if(projectFK.length == 0){
    //     alert('Select valid Project!');
    //     return false;
    // }
    if(moduleFk == null){
        alert('Select valid Module!');
        return false;
    }
    // if(subModuleFk.length == 0){
    //     alert('Select valid Submodule!');
    //     return false;
    // }
    if(taskTitle.length == 0){
        alert('Enter valid Task Title!');
        return false;
    }if(dueDate.length == 0){
        alert('Select valid Due date!');
        return false;
    }if(dueTime.length == 0){
        alert('Select valid Due time!');
        return false;
    }if(priority.length == 0){
        alert('Select priority!');
        return false;
    }
    if(typeof employeeFK != 'undefined'){
        if(employeeFK.length == 0){
            alert('Select valid Employee!');
            return false;
        }
    }else{
        var employeeFK = '';
    }


    console.log('projectFk >>> ',projectFK);
    console.log('moduleFk >>> ',moduleFk);
    console.log('subModuleFk >>> ',subModuleFk);
    console.log('taskTitle >>> ',taskTitle);
    console.log('dueDate >>> ',dueDate);
    console.log('dueTime >>> ',dueTime);
    console.log('priority >>> ',priority);
    // console.log('employeeFK >>> ',employeeFK);
    console.log('taskDescription >>> ',taskDescription);

    $('#createBtn').css('display','none');
    $('#spinnerBtn').css('display','');
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/task-management/add-task",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'projectFk':projectFK,'moduleFk':moduleFk,'subModuleFk':subModuleFk,'taskTitle':taskTitle,'dueDate':dueDate,'dueTime':dueTime,'priority':priority,'employeeFK':employeeFK,'taskDescription':taskDescription,},
        success: function (response) {
            console.log(response['response']);
            
            if(response['response'] == 'success'){
                $('#createBtn').css('display','');
                $('#spinnerBtn').css('display','none');
                alert('New Task Added successfully');
                window.location.reload()
            }else{
                $('#createBtn').css('display','');
                $('#spinnerBtn').css('display','none');
                alert('An Error occured while storing Task Info. Please try again!');
                return false;
            }
        }
    });
    // --------------------------------------------------------


}
// ########################################################################################################################################
// ########################################################################################################################################
