// =======================================================================================================================================
//                                                  Local Storage Value
// =======================================================================================================================================
$(document).ready(function () {
    localStorage.setItem('nextpage', 1);
    localStorage.setItem('previouspage', 0);
    // next = 1, prev = 0
    // on next click =>> prev = nextBtn & next = nextBtn + 1
    // on prev. click =>> next = nextBtn - 1 & prev = nextBtn - 1
});
// =======================================================================================================================================
//                                                  Paginator For Student Management
// =======================================================================================================================================
// --------------------------------------------------------    Next Button   -------------------------------------------------------------
function studentpaginatorNextButton() {
    var nextClick = localStorage.getItem('nextpage');

    // var prevClick = localStorage.getItem('previouspage');
    if (parseInt(nextClick) >= 1) {
        $('#prevButton').show();
        $('#prevButton').css('background-color', '');
        $('#prevButton').css('color', '#007dc6');

        $('#nextButton').css('background-color', '#007dc6');
        $('#nextButton').css('color', 'white');

        var next = parseInt(nextClick) + 1;
        var prev = parseInt(nextClick);

        localStorage.setItem('nextpage', next);
        localStorage.setItem('previouspage', prev);
    } else {
        return false;
    }
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'GET',
        url: "notificationPagination",
        data: {'page': next },
        success: function (response) {
            // console.log(response['searchResultList']['data']);
            console.log(response['response']);
            // -------------------------------------------------------------------------------------------------
            var filteredData = '';
            if (response['notification_paginator']['data'].length > 0) {
                for (var i = 0; i < response['notification_paginator']['data'].length; i++) {

                    // if(response['searchResultList']['data'][i]['request_view_status'] == 'True'){
                    //     var dataStr = ' <div class="notif unread" style="opacity:0.6;">\
                    //                         <p>\
                    //                             <span>'+response['searchResultList']['data'][i]['date']+' | '+response['searchResultList']['data'][i]['time']+'</span>\
                    //                                 '+response['searchResultList']['data'][i]['request_action_description']+'\
                    //                             <a style="pointer-events:none;" authorName="'+response['searchResultList']['data'][i]['request_author']+'" notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" onclick="readAndUnread(this);">\
                    //                             </a>&nbsp;&nbsp;\
                    //                             <i class="fa fa-eye" style="font-size:20px;color:#28afd0;" onclick="updateNotificationStatus(this);" title="view notification" authorName="'+response['searchResultList']['data'][i]['request_author']+'" \notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" NotifyUrl="/'+response['searchResultList']['data'][i]['request_action_url']+'"></i>\
                    //                             &nbsp;&nbsp;<i notifyID="'+response['searchResultList']['data'][i]['id']+'" onclick="deleteNotifications(this)" class="fas fa-trash" style="color:red;font-size:18px;"></i>\
                    //                         </p>\
                    //                     </div>';
                    // }else{
                    //     var dataStr = '<div class="notif unread">\
                    //                     <p>\
                    //                     <span>'+response['searchResultList']['data'][i]['date']+' | '+response['searchResultList']['data'][i]['time']+'</span>\
                    //                     '+response['searchResultList']['data'][i]['request_action_description']+'\
                    //                         <a authorName="'+response['searchResultList']['data'][i]['request_author']+'" notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" onclick="readAndUnread(this);">\
                    //                             Mark as Read\
                    //                         </a>&nbsp;&nbsp;\
                    //                         <i class="fa fa-eye" style="font-size:20px;color:#28afd0;" onclick="updateNotificationStatus(this);" title="view notification" authorName="'+response['searchResultList']['data'][i]['request_author']+'" \notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" NotifyUrl="/'+response['searchResultList']['data'][i]['request_action_url']+'"></i>\
                    //                         &nbsp;&nbsp;<i notifyID="'+response['searchResultList']['data'][i]['id']+'" onclick="deleteNotifications(this)" class="fas fa-trash" style="color:red;font-size:18px;"></i>\
                    //                     </p>\
                    //                 </div>';
                    // }


                    // filteredData = filteredData + dataStr;
                }
                $('#notification_paginator').html('');
                $('#notification_paginator').append(filteredData);
            } else {
                $('#notification_paginator').html('');
            }
        }
    });
    // -----------------------------------------------------------------------------------------------------------------
}
// --------------------------------------------------------    Previous Button   -------------------------------------------------------------
function studentpaginatorPreviousButton() {
    
    var nextClick = localStorage.getItem('nextpage');
    var prevClick = localStorage.getItem('previouspage');

    if (parseInt(prevClick) >= 1) {
        $('#prevButton').css('background-color', '#007dc6');
        $('#prevButton').css('color', 'white');

        $('#nextButton').css('background-color', '');
        $('#nextButton').css('color', '#007dc6');

        var next = parseInt(nextClick) - 1;
        var prev = parseInt(prevClick) - 1;

        localStorage.setItem('nextpage', parseInt(nextClick) - 1);
        localStorage.setItem('previouspage', parseInt(prevClick) - 1);

        if (prev === 0) {
            newPrev = 1;
        } else {
            newPrev = prev;
        }
    } else {
        $('#prevButton').hide();
        return false;
    }

    $.ajax({
        type: 'GET',
        url: "notificationPagination",
        data: {'page': next },
        success: function (response) {
            // console.log(response['searchResultList']['data']);
            console.log(response['response']);
            // -------------------------------------------------------------------------------------------------
            var filteredData = '';
            if (response['notification_paginator']['data'].length > 0) {
                for (var i = 0; i < response['notification_paginator']['data'].length; i++) {

                    // if(response['searchResultList']['data'][i]['request_view_status'] == 'True'){
                    //     var dataStr = ' <div class="notif unread" style="opacity:0.6;">\
                    //                         <p>\
                    //                             <span>'+response['searchResultList']['data'][i]['date']+' | '+response['searchResultList']['data'][i]['time']+'</span>\
                    //                                 '+response['searchResultList']['data'][i]['request_action_description']+'\
                    //                             <a style="pointer-events:none;" authorName="'+response['searchResultList']['data'][i]['request_author']+'" notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" onclick="readAndUnread(this);">\
                    //                             </a>&nbsp;&nbsp;\
                    //                             <i class="fa fa-eye" style="font-size:20px;color:#28afd0;" onclick="updateNotificationStatus(this);" title="view notification" authorName="'+response['searchResultList']['data'][i]['request_author']+'" \notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" NotifyUrl="/'+response['searchResultList']['data'][i]['request_action_url']+'"></i>\
                    //                             &nbsp;&nbsp;<i notifyID="'+response['searchResultList']['data'][i]['id']+'" onclick="deleteNotifications(this)" class="fas fa-trash" style="color:red;font-size:18px;"></i>\
                    //                         </p>\
                    //                     </div>';
                    // }else{
                    //     var dataStr = '<div class="notif unread">\
                    //                     <p>\
                    //                     <span>'+response['searchResultList']['data'][i]['date']+' | '+response['searchResultList']['data'][i]['time']+'</span>\
                    //                     '+response['searchResultList']['data'][i]['request_action_description']+'\
                    //                         <a authorName="'+response['searchResultList']['data'][i]['request_author']+'" notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" onclick="readAndUnread(this);">\
                    //                             Mark as Read\
                    //                         </a>&nbsp;&nbsp;\
                    //                         <i class="fa fa-eye" style="font-size:20px;color:#28afd0;" onclick="updateNotificationStatus(this);" title="view notification" authorName="'+response['searchResultList']['data'][i]['request_author']+'" \notifyID="'+response['searchResultList']['data'][i]['id']+'" requestID="'+response['searchResultList']['data'][i]['requestID']+'" NotifyUrl="/'+response['searchResultList']['data'][i]['request_action_url']+'"></i>\
                    //                         &nbsp;&nbsp;<i notifyID="'+response['searchResultList']['data'][i]['id']+'" onclick="deleteNotifications(this)" class="fas fa-trash" style="color:red;font-size:18px;"></i>\
                    //                     </p>\
                    //                 </div>';
                    // }


                    // filteredData = filteredData + dataStr;
                }
                $('#notificationPaginationAppend').html('');
                $('#notificationPaginationAppend').append(filteredData);
            } else {
                $('#notificationPaginationAppend').html('');
            }
        }
    });
}
// =======================================================================================================================================
