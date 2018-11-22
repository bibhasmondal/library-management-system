$(document).ready(function () {
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    ws = new WebSocket(ws_scheme + '://' + window.location.host + "/library/");
    var i;
    var row;
    ws.onopen = function (e) {
        i=0;
        row = ['row1', 'row2'];
        console.log(e);
        window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value){
            ws.send(value);
        });
    };

    ws.onmessage = function (e) {
        if (e.data != 'Head client not found'){
            var ebooksdata = JSON.parse(e.data);
            ebookshtml = '<a href=' + ebooksdata.booklink + '>' +
                '<div class="container-fluid '+row[i%2]+'">' +
                '<div class="col-sm-3">' + ebooksdata.author + '</div>' +
                '<div class="col-sm-7">' + ebooksdata.title + '</div>' +
                '<div class="col-sm-2"><i>' + ebooksdata.type + ';' + ebooksdata.size + '</i></div>' +
                '</div>' +
                '</a>';
            i+=1;
            if (i>1){
                $('#ebookscount').html(i+' ebooks found.');
            }
            else{
                $('#ebookscount').html(i + ' ebook found.');
            }        
            document.getElementById("ebooksdata").style.display = "block";
            document.getElementById("loader").style.display = "none";
            $('#ebooksdata').append(ebookshtml);
        }
        else{
            document.getElementById("ebooksdata").style.display = "block";
            document.getElementById("loader").style.display = "none";
            $('#ebookscount').html('Head client not found.');
        }    
    };
    ws.onclose = function (e) {
        if (i < 1) {
            setTimeout(function () {
                document.getElementById("loader").style.display = "none";
                $('#ebookscount').html('No ebook found.');
            }, 3000);
        }      
        console.log(e)
    };
    ws.onerror = function (e) {
        if (i < 1) {
            setTimeout(function () {
                document.getElementById("loader").style.display = "none";
                $('#ebookscount').html('No ebook found.');
            }, 3000);
        }
        console.log(e)
    };
    $('#ebooksdata').click(function (e) {
        e.preventDefault();
        window.open($(e.target).parents('a').attr('href'));
    });
});
