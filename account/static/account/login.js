$(document).ready(function () {
    $('#login').load("/account/login/" + ' #login');
    $(document).on('submit', '#loginform', function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/account/login/",
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                username: $(this).serializeArray()[1].value,
                password: $(this).serializeArray()[2].value,
            },
            success: function (data) {
                if (data == 'OK') {
                    javascript: location.reload(true);
                }
                else {
                    $('#error').html(data);
                }
            },
        });
    }); 
});