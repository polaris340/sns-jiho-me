// $(document).ready(function(){
//     $(document).on('submit','form',function onLoginSubmit(){
//         var data = $(this).serializeArray();
//         login(data);
//         return false;
//     });
// });



function login(data) {
    show_progress();
    $.post('/login_submit',data,function(response){
        if (response=='0') {
            location.href = '/';
        } else {
            show_toast('로그인에 실패하였습니다.', 'error');
        }
    }).fail(function(){
        show_toast('오류가 발생했습니다. 잠시 후에 다시 시도해주세요', 'error');
    }).always(function(){
        hide_progress();
    });
}