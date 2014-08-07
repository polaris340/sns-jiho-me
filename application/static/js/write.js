$(document).ready(function(){
    $("#editor").editable({inlineMode:false,
        theme:'dark',
        minHeight:500});

    $(document).on('submit','form',function(){
        show_progress();
    });
});