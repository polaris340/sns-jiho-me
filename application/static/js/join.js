$(document).ready(function(){


    $(document).on('submit','form',function onSubmit(){
        
        var data = $(this).serializeArray();
        join(data);


        return false;
    });


    //form validation
    $(document).on('change', 'input[name=email]', function emailPatternCheck(){
        var email = $(this).val();
        if (email.length > 0) {

            if (!email.match(/^[\w\d_.]+@[\w\d_.]+\.(\w+|\w+\.\w+)$/)) {
                show_toast('메일 형식이 일치하지 않습니다','error');
                $(this).select();
            } else {
            // 이메일 중복 체크
            email_duplicate_check(email);
        }
    }
});

    $(document).on('change', 'input[name=password]', function passwordPatternCheck(){
        var password = $(this).val();
        if (password.length > 0) {

            if (password.length < 6 || password.length > 20) {
                show_toast('비밀번호는 6자 이상, 20자 이하로 설정해주세요', 'error');
                $(this).focus();
            } else if (!password.match(/[a-zA-Z]+/) || !password.match(/[0-9]+/)) {
                show_toast('비밀번호에는 영문자, 숫자를 모두 포함시켜주세요', 'error');
                $(this).select();
            }
        }
    });

    $(document).on('change', 'input[name=password-confirm]', function confirmPasswordMatchCheck(){
        var password = $("input[name=password]").val();
        var confirmPassword = $(this).val();

        if (confirmPassword.length > 0 && password!=confirmPassword) {
            show_toast('비밀번호가 일치하지 않습니다','error');
        }

    });

    $(document).on('change', 'input[name=username]', function usernamePatternCheck(){
        var username = $(this).val();

        if (username.length > 0) {
            if (username.length > 10) {
                show_toast('사용자 이름은 10자 이하로 설정해주세요','error');
                $(this).select();
            }
            if (!username.match(/^[a-zA-Z가-힣0-9_.]+$/)) {
                show_toast('사용자 이름에는 영문자, 한글, 숫자, _, .만 사용 가능합니다.', 'error');
                $(this).select();
            }
        }
    });

    $(document).on('change', 'input[name=mobile]', function phonePatternCheck(){
        var phone = $(this).val();

        if (phone.length > 0) {
            if (!phone.match(/^\+?[0-9-]{10,14}$/)) {
                show_toast('숫자, -, + 만 입력해주세요','error');
                $(this).select();
            }
        }
    });

});


function email_duplicate_check(email) {
    show_progress();
    $.post('/email_duplicate_check',{email:email},function(response){
        if (response == '0') {

        } else {
            show_toast('이미 사용중인 이메일 주소입니다.','error');
            $('input[name=email]').select();
        }
    }).fail(function(){
        show_toast('오류가 발생했습니다. 잠시 후에 다시 시도해주세요','error');
    }).always(function(){
        hide_progress();
    });
}


function join(data) {
    show_progress();
    $.post('/join_submit',data, function(response){
        if (response=='0') {
            location.href='/login';
        } else {
            switch (response) {
                case '1':
                    show_toast('이미 사용중인 이메일입니다.','error');
                    $('input[name=email]').select();
                    break;
                case '2':
                    show_toast('메일 형식이 잘못되었습니다.','error');
                    $('input[name=email]').select();
                    break;
                case '3':
                    show_toast('잘못된 비밀번호입니다.','error');
                    $('input[name=password]').select();
                    break;
                case '4':
                    show_toast('사용자 이름이 잘못되었습니다.','error');
                    $('input[name=username]').select();
                    break;
                case '5':
                    show_toast('전화번호 형식이 잘못되었습니다.','error');
                    $('input[name=mobile]').select();
                    break;
            }
        }
    }).fail(function(){
        show_toast('오류가 발생했습니다. 잠시 후에 다시 시도해주세요','error');
    }).always(function(){
        hide_progress();
    });
}