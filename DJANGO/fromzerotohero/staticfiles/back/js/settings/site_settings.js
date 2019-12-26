$("#site_settings_form").on("submit", (e) => {
    e.preventDefault(); // elementin kendi default özelliğini block eder!.
    let url = $("#ajax_url_link").val();
    let phone = $("#site_phone").val();
    let title = $("#site_title").val();
    let about = $("#site_about").val();
    let site_facebook = $("#site_facebook").val();
    let site_twitter = $("#site_twitter").val();
    let site_youtube = $("#site_youtube").val();
    let site_link = $("#site_link").val();
    let site_pic = $("#site_pic").val();
    if (phone == '' || title == '' || about == '') {
        new Toast({
            message: 'Phone & Title & About Fields Are Required!',
            type: 'danger'
        });
    } else {
        let bilgiler = {
            'phone': phone,
            'title': title,
            'about': about,
            'site_facebook': site_facebook,
            'site_twitter': site_twitter,
            'site_youtube': site_youtube,
            'site_link': site_link,
            'site_pic': site_pic
        };
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'json',
            data: bilgiler,
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