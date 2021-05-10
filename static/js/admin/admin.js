function get_admin_index() {
    return $.ajax({
        type: "GET",
        url: "/api/admin/index/",
        dataType: "json",
        contentType: "application/json;utf-8",
        // data: data,
        timeout: 6000
    });
}

$(document).ready(function () {

    get_admin_index()
        .done(function (response) {
            // alert(response['data'].login_ip)
            var server_info = "";
            var login_ip_detail = response['data'].login_ip;
            var black_ip_list = response['data'].black_ip;
            alert(login_ip_detail)
            var black_ip_html = "";
            document.getElementById('login_ip_addr').innerText = login_ip_detail;
            // $.("#login_ip_addr").text(login_ip_detail);
            for (var i =  0; i < black_ip_list.length; i++) {
                // alert(black_ip_list[i][0])
                black_ip_html += '<tr>' + '<td>' + black_ip_list[i][0] + '</td>' +
                    '<td>' + black_ip_list[i][1] + '</td>' +
                    '<td>' + black_ip_list[i][2] + '</td>'
            }
            $("#black_ip").html(black_ip_html)
        })
})