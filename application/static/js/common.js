var color = {
    default:'#28324E',
    warning:'#f37934',
    error:'#b8312f',
    success:'#2969b0'
};

var defaultStyle = {
    color:'white',
    display:'inline-block',
    borderRadius:'.5em',    
    lineHeight:'1.8em',
    fontWeight:'bold',
    fontSize:'1.2em',
    padding:'0px 10px'

};

function show_toast(message, level, style){

    level = level || 'default';

    // set custom styles
    if(style){
        for(s in defaultStyle){
            if(!style[s]){
                style[s] = defaultStyle[s];
            }
        }
    }else{
        style = defaultStyle;
    }

    style.backgroundColor = color[level];
    


    if($('div#toast').length>0){
        setTimeout('show_toast("'+message+'","'+level+'", '+JSON.stringify(style)+')',300);
    }else{
        var toast = '<div id="toast" style="text-align:center;position:fixed;bottom:20%;width:100%;padding:0px;maring:0px;display:none;z-index:9999;"><span>'+message+'</span></div>';
        
        $('body').append(toast);
        $('div#toast')
            .find('span')
            .css(style)
            .parent()
            .fadeIn(300)
            .delay(1000)
            .fadeOut(300,function(){

                $('div#toast').remove();
            }); 
    }
    

}


function show_progress(progressClass, progressId){
    progressId = progressId||"progress";
    progressClass = progressClass||'success';
    if ($('#progress').length==0) {
        $('body').append('<div class="progress" id="'+progressId+'" style="position:fixed;top:0px;z-index:9999;width:100%;"><div class="progress-bar progress-bar-'+progressClass+' progress-bar-striped active" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width:100%;"></div></div>');    
        
    }
    
}


function hide_progress(progressId){
    progressId = progressId||'progress';
    $("#"+progressId).remove();
}

function show_confirm(message, level, callback, autohide,  tagId){

    autohide = autohide||true;
    level = level||'default';
    tagId = tagId||'confirm';
    if($('#'+tagId).length > 0) {
        return false;
    }

    $("body").append('<div id="'+tagId+'" style="line-height:2em;padding:10px;position:fixed;z-index:9999;right:20px;top:20px;border-radius:5px;background:'+color[level]+';color:white;font-weight:bold;display:none;box-shadow:0px 0px 2px 2px rgb(100,100,100);">'+message+'<br><div class="pull-right"><button type="button" class="btn btn-default btn-sm btn-cancel">Cancel</button>&nbsp;<button type="button" class="btn btn-primary btn-sm btn-ok">Ok</button></div></div>');

    
    $("#"+tagId).find(".btn-cancel").click(function(){
        if(callback) callback(false);
        $("#"+tagId).fadeOut(300,function(){
            $("#"+tagId).remove();
        });
    });

    $("#"+tagId).find('.btn-ok').click(function(){
        if(callback) callback(true);
        $("#"+tagId).fadeOut(300,function(){
            $("#"+tagId).remove();
        });
    });
    

    $("#"+tagId)
        .fadeIn(300);

    if(autohide){
        setTimeout('$("#'+tagId+'").fadeOut(300,function(){$("#'+tagId+'").remove(); });',3000);
    }

}