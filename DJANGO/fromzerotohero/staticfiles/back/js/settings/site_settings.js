$("#site_settings_form").submit((e) => {
    e.preventDefault(); // elementin kendi default özelliğini block eder!.
    let url = $("#ajax_url").val();
    let form_data = new FormData(); // FormData instance oluşturduk
    let phone = $("#site_phone").val();
    let title = $("#site_title").val();
    let about = $("#site_about").val();
    let site_facebook = $("#site_facebook").val();
    let site_twitter = $("#site_twitter").val();
    let site_youtube = $("#site_youtube").val();
    let site_link = $("#site_link").val();
    let site_pic = $("#site_pic")[0].files[0]; // resmi yakaladık
    form_data.append('site_phone', phone); // bu şekilde yollayınca view kısmında request.POST.get('site_phone') olarak yakalayacağız
    form_data.append('site_title', title);
    form_data.append('site_about', about);
    form_data.append('site_facebook', site_facebook);
    form_data.append('site_twitter', site_twitter);
    form_data.append('site_youtube', site_youtube);
    form_data.append('site_link', site_link);
    form_data.append('site_pic', site_pic);
    if (!phone || !title || !about) { // kontrolleri yaptık
        new Toast({
            message: 'Phone & Title & About Fields Are Required!',
            type: 'danger'
        });
    } else {
        $.ajax({
            url: url,
            type: "post",
            data: form_data,
            contentType: false,
            processData: false,
            success: function (data) {
                if (data.success) {
                    new Toast({
                        message: 'Site ayarları başarıyla güncellendi!',
                        type: 'success'
                    });
                } else {
                    new Toast({
                        message: 'Birtakım hatalar meydana geldi!',
                        type: 'danger'
                    });
                }
            }
        });

    }
});