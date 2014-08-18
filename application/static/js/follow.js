var xhr;
var running = false;

$(document).ready(function(){
    $('#input-find-user').keyup(function(e){
        if (xhr) xhr.abort();
        if ($(this).val()=='') {
            $("#find-result").empty();
        } else {
            find_user($(this).val());
        }


    });

    $(document).on('click', "#find-result li", function(){
        if (running) {
            show_toast('잠시만 기다려주세요');
        } else {
            add_following($(this));
        }
    });
});

function add_following(target) {
    running = true;
    show_progress();
    $.post('/add_following',{'following_id':target.data('userId')}, function(response){
        if (response == '0') {
            show_toast('등록되었습니다','success');
            target.remove().appendTo('#following-list')
        } else if (response == '1') {
            show_toast('이미 등록된 회원입니다','warning');
        } else {
            show_toast('오류가 발생했습니다','error');
        }
    }).fail(function(){
        show_toast('오류가 발생했습니다','error');
    }).always(function(){
        running = false;
        hide_progress();
    });
}

function find_user(keyword){
    show_progress();
    xhr = $.post('/find_user',{'keyword':keyword} ,function(response){
        $("#find-result").html(response);
    }).always(function(){
        $('#input-find-user').removeAttr('disabled').focus();
        hide_progress();
    });
}