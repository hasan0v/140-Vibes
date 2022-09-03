document.addEventListener('play', function(e){
    var audios = document.getElementsByTagName('audio');
    for(var i = 0, len = audios.length; i < len;i++){
        if(audios[i] != e.target){
            audios[i].pause();
        }
    }
}, true);

$(document).ready(function(){
        document.addEventListener('mousemove', e => {
            $(".cursor").attr("style", "top: "+(e.pageY - 10)+"px; left: "+(e.pageX - 10)+"px;");
            $(".cursor").css('display', 'block');
        })
});
