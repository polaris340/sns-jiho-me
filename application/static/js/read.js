$(document).ready(function(){
    $("img").each(function(){
        var maxWidth = $('.panel-body').width();
        if ($(this).width() > maxWidth) {
            $(this).attr('width',maxWidth);
        }
    });

    // $(document).on('click','.btn-delete-post',function(){
    //     var url = $(this).attr('href');
    //     show_confirm('정말 삭제하시겠습니까?','warning',function(){
    //         location.href=url;
    //     });
    //     return false;
    // });
});