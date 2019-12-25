$("#site_submit").click((e) => {
    e.preventDefault(); // elementin kendi default özelliğini block eder!.
    let phone = $("#site_title").val();
    let title = $("#site_phone").val();
    let about = $("#site_about").val();
    if (phone == '' || title == '' || about == '') {
        new Toast({
            message: 'Phone & Title & About Fields Are Required!',
            type: 'danger'
        });
    } else {
        $('#site_settings_form').submit(); // formu submit eder
    }
});