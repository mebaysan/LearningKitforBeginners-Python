// $("#show_message_btn").click((e) => {
//     e.preventDefault();
//     let id = $("#show_message_btn").data('id');
//     let url = $("#show_message_btn").attr('href');
//     let form_data = new FormData();
//     form_data.append('message_pk', id);
//     form_data.append('process', 'is_it_read')
//     console.log("Merhaba id = " + id);
//     $.ajax({
//         url: url,
//         type: "post",
//         data: form_data,
//         contentType: false,
//         processData: false,
//         success: function (data) {
//             if (data.success === true) {
//                 new Toast({
//                     message: 'Başarıyla Mesaj Okundu!',
//                     type: 'success'
//                 });
//
//             } else {
//                 new Toast({
//                     message: "Something Wrong!",
//                     type: 'danger'
//                 });
//             }
//         }
//     });
// });
//
// let get_page_data = () => {
//     let url = $("#show_message_btn").attr('href');
//     let form_data = new FormData();
//     form_data.append('process', 'get_page_data');
//     $.ajax({
//         url: url,
//         type: "post",
//         data: form_data,
//         contentType: false,
//         processData: false,
//         success: function (data) {
//             if (data.success) {
//                 console.log(data);
//             } else {
//                 new Toast({
//                     message: "Something Wrong!",
//                     type: 'danger'
//                 });
//             }
//         }
//     });
// };