// ##############################################################################################################
// ##############################################################################################################
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
// ##############################################################################################################
// ##############################################################################################################
function add_cultural_event(){
    var eventID = $('#culturalEventID').val().trim();
    var eventTitle = $('#culturalEventTitle').val().trim();
    var eventDate = $('#culturalEventDate').val();
    var eventManagerID = $('#culturalEventManager').val();
    var eventBudget = $('#culturalEventBudget').val();
    var eventHighlight = $('#culturalEventHighlight').val();
    // var specialPerformance = $('#event_highlights').val();
    // var creative = $('#event_highlights').val();


    console.log('eventID >>> ',eventID);
    console.log('eventTitle >>> ',eventTitle);
    console.log('eventDate >>> ',eventDate);
    console.log('eventManagerID >>> ',eventManagerID);
    console.log('eventBudget >>> ',eventBudget);
    console.log('eventHighlight >>> ',eventHighlight);
    // console.log('specialPerformance >>> ',specialPerformance);
    // console.log('creative >>> ',creative);

    var employee_ID=[];
    var employee_perform=[];

    $('.employeeID').each(function() { employee_ID.push($(this).val()); });
    console.log(employee_ID);
    $('.employee_performance').each(function() { employee_perform.push($(this).val()); });
    console.log(employee_perform);

    
    var performanceDetail = '';
    var lstIndex = employee_ID.length -1;
    for(var i=0;i<employee_ID.length;i++){
        var stringData = employee_ID[i]+'$'+employee_perform[i];
        if(i != lstIndex){
            stringData = stringData + "|";
        }
        performanceDetail = performanceDetail + stringData;
    }
    console.log('performanceDetail >>> ',performanceDetail);



    if(eventID.trim() == ''){
        alert('select a Cultural event!');
        return false;
    }
    if(eventTitle.trim() == ''){
        alert('Enter event title!');
        return false;
    }
    if(eventDate.trim() == ''){
        alert('select a date to create event!');
        return false;
    }
    if(eventManagerID.trim() == ''){
        alert('select event manager!');
        return false;
    }
    if(eventBudget.trim() == ''){
        alert('select event date!');
        return false;
    }
    if(eventHighlight.length == 0){
        alert('select atleast 1 highlight!');
        return false;
    }

    var formdata = new FormData();
    formdata.append("eventID", eventID);
    formdata.append("eventTitle", eventTitle);
    formdata.append("eventDate", eventDate);
    formdata.append("eventManagerID", eventManagerID);
    formdata.append("eventBudget", eventBudget);
    formdata.append("eventHighlight[]", eventHighlight);
    formdata.append("performanceDetail", performanceDetail);

    let myFileimg = document.getElementById('emp_photo').files[0];
    if (typeof myFileimg != 'undefined') {
        formdata.append('event_creative', myFileimg, myFileimg['name']);
    }else{
        alert('select event creative!')
    }


    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/event-management/add-cultural-event/"+eventID.toString(),
        headers: { 'X-CSRFToken': csrftoken },
        data: formdata,
        cache : false,
        processData : false,
        contentType : false,
        encType : 'multipart/form-data',
        success: function (response) {
            console.log(response['response']);
            if(response['response'] == 'created'){
                alert('New Event created Successfully');
                window.location.reload()
            }else if(response['response'] == 'updated'){
                alert('Event updated Successfully');
                window.location.reload()
            }else{
                alert('An error occured!');
                return false;
            }
        }
    });
    // --------------------------------------------------------
}
// ##############################################################################################################
// ##############################################################################################################
function check_existing_cultural_event(){
    var eventID = $('#culturalEventID').val();
    // ---------------  AJAX CALL  ----------------------------
    $.ajax({
        type: 'GET',
        url: "/event-management/check_existing_cultural_event/"+eventID.toString(),
        success: function (response) {
            console.log(response['response']);
            if(response['response'].length > 0 && response['response'][0]['message'] == 'exist'){
                $('#culturalEventText').css('display','');
                $('#culturalEventDate').val(response['response'][0]['date']);
                $('#culturalEventHighlight').val(response['response'][0]['highlight']);
                // $("#culturalEventHighlight").select2({
                // });

            }else if(response['response'].length > 0 && response['response'][0]['message'] == 'new'){
                $('#culturalEventText').css('display','none');
                $('#culturalEventDate').val(response['response'][0]['date']);
                // $('#culturalEventHighlight').val(response['response'][0]['highlight']);
                // $("#culturalEventHighlight").select2({
                // });
            }else if(response['response'].length == 0){
                $('#culturalEventText').css('display','none');
                $('#culturalEventDate').val('');
                // $('#culturalEventHighlight').val(response['response'][0]['highlight']);
                // $("#culturalEventHighlight").select2({
                // });
            }else{
                $('#culturalEventText').css('display','none');
                $('#culturalEventDate').val('');
                // $("#culturalEventHighlight").select2({
                // });
                // $('#culturalEventHighlight').val(response['response'][0]['highlight']);
            }
            $("#culturalEventHighlight").select2({
            });
        }
    });
    // --------------------------------------------------------
}