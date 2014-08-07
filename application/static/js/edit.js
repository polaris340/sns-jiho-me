$(document).ready(function(){
    $("div#post-body").editable({theme:'dark'});

    $(document).on('click','#btn-edit-post-submit',function(){
        var body = $("#post-body").html();
        var postId = $("#input-post-id").val();

        show_progress();
        $.post('/edit',{'post_id':postId,'body':body},function(response){
            if (response=='0') {
                show_toast('수정되었습니다','success');
            } else if (response=='1') {
                show_toast('수정 권한이 없습니다','error');
            } else {
                show_toast('오류가 발생하였습니다. 잠시 후에 다시 시도해주세요','error');
            }
        }).always(function(){
            hide_progress();
        }).fail(function(){
            show_toast('오류가 발생하였습니다. 잠시 후에 다시 시도해주세요','error');
        });
    });
});