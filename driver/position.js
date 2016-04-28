//获取元素的纵坐标
function getTop(e)
{
    var offset=e.offsetTop;
    if(e.offsetParent!=null) offset+=getTop(e.offsetParent);
    return offset;
}
//获取元素的横坐标
function getLeft(e)
{
    var offset=e.offsetLeft;
    if(e.offsetParent!=null) offset+=getLeft(e.offsetParent);
    return offset;
}

var ele = document.getElementsByClassName('nc-lang-cnt')[0]

return getTop(ele) + ',' + getLeft(ele);
