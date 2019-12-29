$('#example-datatable tbody').on('click', '#show_message_btn', function (e) {
    //https://datatables.net/examples/advanced_init/events_live.html datatable event selector
    e.preventDefault();
    let id = $(this).attr('data-id');
    let url = $(this).attr('href');
    let form_data = new FormData();
    form_data.append('message_pk', id);
    form_data.append('process', 'is_it_read');
    $.ajax({
        url: url,
        type: "post",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                Swal.fire({
                    title: data.name,
                    icon: 'info',
                    html: '<h6>Message</h6>'
                        + '<p>' + data.message + '</p>'
                });
                new Toast({
                    message: "Message has ben readed was successfully!",
                    type: 'success'
                });
                get_page_data();
                setTimeout(
                    function () {
                        location.reload();
                    }, 8000);
            } else {
                new Toast({
                    message: "Something Wrong!",
                    type: 'danger'
                });
            }
        }
    });
});


$('#example-datatable tbody').on('click', '#delete_message_btn', function (e) {
    e.preventDefault();
    let id = $(this).attr('data-id');
    let url = $(this).attr('href');
    let form_data = new FormData();
    form_data.append('message_pk', id);
    form_data.append('process', 'delete_message');
    $.ajax({
        url: url,
        type: "post",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                new Toast({
                    message: 'Mesaj Has been Deleted Was Successfully!',
                    type: 'success'
                });
                get_page_data();
                setTimeout(
                    function () {
                        location.reload();
                    }, 8000);
            } else {
                new Toast({
                    message: "Something Wrong!",
                    type: 'danger'
                });

            }
        }
    });
});


let get_page_data = () => {
    let url = $("#show_message_btn").attr('href');
    let form_data = new FormData();
    form_data.append('process', 'get_page_data');
    $.ajax({
        url: url,
        type: "post",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                console.log(data.messages);
            } else {
                new Toast({
                    message: "Something Wrong!",
                    type: 'danger'
                });
            }
        }
    });
};