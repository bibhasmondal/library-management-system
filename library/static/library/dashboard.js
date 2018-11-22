$(document).ready(() => {
    $('.req_inner .body').hide();

    $('.req_inner').on('click', event => {
        $(this).find('.body').show();
        $(event.currentTarget).find('.body').slideToggle();
        $(event.currentTarget).find('i').toggleClass('fa-arrow-right');
        $(event.currentTarget).find('i').toggleClass('fa-arrow-down');
    })
})