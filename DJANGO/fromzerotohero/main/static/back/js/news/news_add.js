$("button").click((e) => {
    e.preventDefault(); // elementin kendi default özelliğini block eder!.
    let category_val = $("#news_category").val();
    if (category_val == '0') {
        new Toast({
            message: 'Please choose a category!',
            type: 'danger'
        });
    } else {
        $('#newsAdd').submit(); // formu submit eder
    }
});