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

function get_server_info() {
    return $.ajax({
        type: "GET",
        url: "/api/admin/server_info/",
        dataType: "json",
        contentType: "application/json;utf-8",
        // data: data,
        timeout: 6000
    });
}

$(document).ready(function () {
    var myChart = echarts.init(document.getElementById('server_info'));
    get_server_info()
        .done(function (response) {
            // 指定图表的配置项和数据
            var cpu_info = response['data'].cpu_info;
            var memory_info = response['data'].memory_info;
            var disk_info = response['data'].disk_info;
            var option = {
                title: {
                    text: '服务器使用率信息'
                },
                tooltip: {},
                legend: {
                    data: ['使用率']
                },
                xAxis: {
                    data: ["cpu", "内存", "硬盘"]
                },
                yAxis: {},
                series: [{
                    name: '使用率',
                    type: 'bar',
                    data: [cpu_info, memory_info, disk_info]
                }]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        })


})

function get_title_list_api() {
    return $.ajax({
        type: "GET",
        url: "/api/admin/title_list/",
        dataType: "json",
        contentType: "application/json;utf-8",
        // data: data,
        timeout: 6000
    });
}

$(document).ready(function () {
    get_title_list_api()
        .done(function (response) {
            var html = "";
            for (var i = 0; i < response['data'].length; i++) {
                html += '<tr>' + '<td>' + response['data'][i].title + '</td>' +
                    '<td>' + response['data'][i].read_num + '</td>' +
                    '<td><button type="button" class="layui-btn layui-btn-sm layui-btn-normal" onclick="">' +
                    '编辑' + '</button>' + '</td>' + '</tr>'
            }
            $("#title_list").html(html)
        })
})