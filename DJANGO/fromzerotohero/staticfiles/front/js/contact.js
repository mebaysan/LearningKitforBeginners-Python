$("#form_button").click((e) => {
    e.preventDefault();
    let url = $("#contact_form").attr('action');
    let method = $("#contact_form").attr('method');
    let form_data = new FormData(); // FormData instance oluşturduk
    let name = $("#name").val();
    let email = $("#email").val();
    let message = $("#msg").val();
    form_data.append('name', name);
    form_data.append('email', email);
    form_data.append('message', message);
    if (!name || !email || !message) { // kontrolleri yaptık
        new Toast({
            message: 'All Fields Are Required!',
            type: 'warning'
        });
    } else {
        $.ajax({
            url: url,
            type: method,
            data: form_data,
            contentType: false,
            processData: false,
            success: function (data) {
                if (data.success === true) {
                    new Toast({
                        message: `Thanks for your message dear ${name}!`,
                        type: 'success'
                    });
                    clear_form_fields();
                } else {
                    new Toast({
                        message: `${data.error}`,
                        type: 'danger'
                    });
                }
            }
        });

    }
});

let clear_form_fields = () => {
    $("#name").val("");
    $("#email").val("");
    $("#msg").val("");
};