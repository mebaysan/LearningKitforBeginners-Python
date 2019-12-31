$("#btn_submit").on('click', (e) => {
    e.preventDefault();
    let old_pass = $("#old_pass").val();
    let new_pass = $("#new_pass").val();
    if (!old_pass || !new_pass) {
        new Toast({
            message: 'All fields are required!',
            type: 'danger'
        });
    } else {
        $("#change_pass_form").submit();
    }
});