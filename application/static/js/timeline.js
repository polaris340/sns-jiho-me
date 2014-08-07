//autoload
var last=false;
var running=false;

$(document).ready(function(){
    //get_posts(0);

    $(document).on('scroll',function(){
        if (last) return false;

        var lastPost = $('#post-list>div.panel:last-child');
        var lastPostId = lastPost.data('postId');


        if ($('body').scrollTop()+$(window).height() > lastPost.offset().top) {

            get_posts(lastPostId);

        }
    });
});

function get_posts(start_id) {
    if (!running) {
        running = true;

        show_progress();
        $.post('/get_posts',{'start_id':start_id},function(response){
            if (response.trim()=='') {
                last=true;
                return false;
            }
            $("#post-list").append(response);
        }).always(function(){
            hide_progress();
            running = false;
        });
    }
}