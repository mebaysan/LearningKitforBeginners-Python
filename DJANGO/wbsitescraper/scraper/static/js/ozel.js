$("#delete_btn").click(() => {
    $("#site_address").val('');
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$("#research_btn").click(() => {
    let scrape_url = $("#site_address").val();
    let bilgiler = {'scrape_url': scrape_url};
    $.ajax({
        url: '/',
        type: 'post',
        dataType: 'json',
        data: bilgiler,
        complete: function () {
        },
        success: function (data) {
            if (data.success === true) { // eğer dönen data içerisindeki success değişkeni tip olarak true ise
                $("#site_address").val("");
                $("#result").show();
                $("#result_tablo > tbody").empty(); // bir istek daha geldiğinde önce tabloyu temizliyoruz
                $("#site_adresi_result").text("(" + data.site + ")");
                $("#site_adresi_result").attr('href', data.site);
                for (let i = 0; i < data['links'].length; i++) {
                    $('#result_tablo > tbody:last-child').append("<tr><td>" + data.links[i]['link'] + "</td><td>" + data.links[i]['name'] + "</td><td><a href='" + data.site + data.links[i]['link'] + "'>" + data.links[i]['name'] + "</a></td></tr>"); // tablomuza eleman ekliyoruz
                }
            } else {
                Swal.fire(
                    'Oops?',
                    'Please repeat the search or try again with the http protocol',
                    'error'
                );
            }

        }
    });
});
