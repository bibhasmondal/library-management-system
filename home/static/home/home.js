$(document).ready(function () {
    if (screen.availHeight == screen.height) {
        if (screen.availHeight > screen.availWidth) {

            $('#img1,#img2,#img3').height(screen.availWidth - $('nav').height() - $('footer').height() + "px");
        }
        else {
            $('#img1,#img2,#img3').height(screen.availHeight - $('nav').height() - $('footer').height() + "px");
        }
    }
    else
    {
        $('#img1,#img2,#img3').height(screen.availHeight - $('nav').height() - $('footer').height() - 2 * (screen.height - screen.availHeight - 7) + "px");
        /*$('#img1,#img2,#img3').height("100%")*/

    }
});