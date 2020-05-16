function mover()
{
    var event;
    event = document.getElementById('my_img');
    event.innerHTML='<center><img src="my_img.jpg" width="600px" height="800px"></center>';
    
}
function mout(){
    var event;
    event = document.getElementById('my_img');
    event.innerHTML='';
}
function showimg()
{

    var event;
    event = document.getElementById('character_img');
    if (event.style.display == 'none'){
        event.style = "display:"
        var bt;
        bt = document.getElementsByClassName('about_me');
        bt[3].innerHTML = '돌아가기';
    }else{
        event.style = "display:none"
        var bt;
        bt = document.getElementsByClassName('about_me');
        bt[3].innerHTML = '확인하기';
    }
    
}