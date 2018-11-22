$(document).ready(function () {
    $('#logout').click(function () {
        $.ajax({
            url: "/account/logout/",
            success: function (data) {
                javascript: location.reload(true);
            },
        });
    });
    $('#myNavbar,#myBody,.navbar-header').click(function () {
        $('#navLogin').collapse('hide');
    });
});