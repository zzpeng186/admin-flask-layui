// function get_article(msg, callback){
//     alert(msg)
//     var data_list = []
//     $.ajax({
//         type: "GET",
//         url: "/api/article_list/",
//         dataType: "json",
//         async: true,
//         success: function (obj){
//             // alert(data)
//             data_list = obj.data;
//             callback(data_list)
//         }
//     });
//     // alert(data_list)
//     // return data_list
// }

// function get_article(callback) {
// 	// console.log(msg)
// 	var data_list = []
// 	$.ajax({
// 		type: "GET",
// 		url: "/api/article_list/",
// 		dataType: "json",
// 		async: true,
// 		success: function(obj) {
// 			data_list = obj.data;
// 			alert(obj)
// 			callback(data_list)
// 		}
// 	});
// 	// alert(data_list)
// 	// return data_list
// }

// function get_article() {
// 	// console.log(msg)
// 	// var data_list = []
// 	return $.ajax({
// 		type: "GET",
// 		url: "/api/article_list/",
// 		dataType: "json",
// 		async: true,
// 	});
// 	// alert(data_list)
// 	// return data_list
// }

function get_article() {
    return $.ajax({
        type: "GET",
        url: "/api/article_list/",
        dataType: "json",
        contentType: "application/json;utf-8",
        // data: data,
        timeout: 6000
    });
}

// get_article()
//     .done(function (response) {
//         console.log(response);
//         var msg = response['msg']
//         if (msg == 'success'){
//             // alert(response['data'])
//             return response['data']
//         }else {
//             alert('error')
//         }
//         // return data_dict
//     })
//     .fail(function () {
//         //TODO
//     });

layui.use('element', function () {
    var $ = layui.jquery
        , element = layui.element; //Tab的切换功能，切换事件监听等，需要依赖element模块

    element.on('tab(docDemoTabBrief)', function () {
        alert(this.getAttribute('lay-id'));
        // var data_list = get_article(callback)
        // var data_list = get_article()

        // var data_list = get_article('一些参数', (res) => {
		// 	return res;
		// });
        // var da = callback()
        // data_list = get_article()
        // console.log(data_list)
        // alert(data_list['count'])
        var lay_id = this.getAttribute('lay-id');
        var html = ""
        get_article()
            .done(function (response) {
                console.log(response);
                var data_list = response['data']
                if (lay_id == "index") {
                    alert(response['data'].length)
                    for (var i = 0; i < data_list.length; i++) {
                        html += '<div style="margin-top: 30px">' + '<h2>' + data_list[i].title + '</h2>' + '<p style="color: #009688; margin-top: 10px">2020-01-01 | python</p>' +
                            '<p style="margin-top: 2%; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden;">' +
                            'table 模块是我们的又一走心之作，在 layui 2.0 的版本中全新推出，是 layui最核心的组成之一。它用于对表格进行一些列功能和动态化数据操作，涵盖了日常业务所涉及的几乎全部需求。支持固定表头、固定行、固定列左/列右，支持拖拽改变列宽度，支持排序，支持多级表头，支持单元格的自定义模板，支持对表格重载（比如搜索、条件筛选等），支持复选框，支持分页，支持单元格编辑等等一些列功能。尽管如此，我们仍将对其进行完善，在控制代码量和性能的前提下，不定期增加更多人性化功能。table模块也将是 layui 重点维护的项目之一' +
                            '</p><br/><br/>' + '<button type="button" class="layui-btn layui-btn-primary layui-btn-sm" style="float: right">' +
                            '阅读全文' + '</button>' + '<br/><br/>' + '<hr>' + '</div>';
                    }
                    $("#tab_content_detail").html(html)

                }
                if (lay_id == "2") {
                    html = '<li class="layui-timeline-item">' +
                        '<i class="layui-icon layui-timeline-axis"></i>' +
                        '<div class="layui-timeline-content layui-text">' +
                        '<h3 class="layui-timeline-title">8月18日</h3>' +
                        '<ul>' +
                        '<li>《登高》</li>' +
                        '<li>《茅屋为秋风所破歌》</li>' +
                        '</ul>' +
                        '</div>' + '</li>';
                    $("#tab_content_detail").html(html)
                }
                // return data_dict
            })
            .fail(function () {
                //TODO
            });

    });
});

$(document).ready(function (){
    get_article()
        .done(function (response) {
            var data_list = response['data'];
            var html = '';
            for (var i = 0; i < data_list.length; i++) {
                html += '<div style="margin-top: 30px">' + '<h2>' + data_list[i].title + '</h2>' + '<p style="color: #009688; margin-top: 10px">2020-01-01 | python</p>' +
                    '<p style="margin-top: 2%; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden;">' +
                    'table 模块是我们的又一走心之作，在 layui 2.0 的版本中全新推出，是 layui最核心的组成之一。它用于对表格进行一些列功能和动态化数据操作，涵盖了日常业务所涉及的几乎全部需求。支持固定表头、固定行、固定列左/列右，支持拖拽改变列宽度，支持排序，支持多级表头，支持单元格的自定义模板，支持对表格重载（比如搜索、条件筛选等），支持复选框，支持分页，支持单元格编辑等等一些列功能。尽管如此，我们仍将对其进行完善，在控制代码量和性能的前提下，不定期增加更多人性化功能。table模块也将是 layui 重点维护的项目之一' +
                    '</p><br/><br/>' + '<button type="button" class="layui-btn layui-btn-primary layui-btn-sm" style="float: right" onclick="detail_click(' + data_list[i].id + ')">' +
                    '阅读全文' + '</button>' + '<br/><br/>' + '<hr>' + '</div>';
            }
            var form_html = ''
            form_html = '<form class="layui-form" action="">' + html + '</form>'
            $("#tab_content_detail").html(form_html)
        })
})

function get_article_detail(article_id) {
    return $.ajax({
        type: "GET",
        url: "/api/detail" + "?id=" + article_id,
        dataType: "json",
        contentType: "application/json;utf-8",
        // data: data,
        timeout: 6000
    });
}

function detail_click(data_id){
    get_article_detail(data_id)
        .done(function (response) {
            // alert('1')
            var data_detail = response['data'];
            var html = "";
            html = '<div style="margin-top: 30px">' + '<h1 style="text-align:center">' + data_detail.title + '</h1>' +
                '<p style="color: #009688; margin-top: 10px">2020-01-01 | ' + data_detail.category + '</p>' +
                '<br/>' + '<hr>' +
                '<p>' + data_detail.content + '</p>' +
                '<br/><br/>' + '<hr>' + '</div>';
            $("#tab_content_detail").html(html)
        })
    // alert(data_id)
}

$(document).ready(function () {
    $("#detail").click(function () {
        alert('dianjile')
    })
})
// layui.use('element', function () {
//     var $ = layui.jquery
//         , element = layui.element; //Tab的切换功能，切换事件监听等，需要依赖element模块
//
//     element.on('tab(docDemoTabBrief)', function () {
//         alert(this.getAttribute('lay-id'));
//         // var data_list = get_article(callback)
//         var data_list = get_article()
//
//         // var data_list = get_article('一些参数', (res) => {
// 		// 	return res;
// 		// });
//         // var da = callback()
//         // data_list = get_article()
//         console.log(data_list)
//         alert(data_list['count'])
//         var lay_id = this.getAttribute('lay-id');
//         var html = ""
//         if (lay_id == "index") {
//             // alert(data_list.data.length)
//             for (var i=0; i<data_list.length; i++){
//                 html += '<div style="margin-top: 30px">' + '<h2>' + data_list.data[i] + '</h2>' + '<p style="color: #009688; margin-top: 10px">2020-01-01 | python</p>' +
//                 '<p style="margin-top: 2%; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden;">' +
//                 'table 模块是我们的又一走心之作，在 layui 2.0 的版本中全新推出，是 layui最核心的组成之一。它用于对表格进行一些列功能和动态化数据操作，涵盖了日常业务所涉及的几乎全部需求。支持固定表头、固定行、固定列左/列右，支持拖拽改变列宽度，支持排序，支持多级表头，支持单元格的自定义模板，支持对表格重载（比如搜索、条件筛选等），支持复选框，支持分页，支持单元格编辑等等一些列功能。尽管如此，我们仍将对其进行完善，在控制代码量和性能的前提下，不定期增加更多人性化功能。table模块也将是 layui 重点维护的项目之一' +
//                 '</p><br/><br/>' + '<button type="button" class="layui-btn layui-btn-primary layui-btn-sm" style="float: right">' +
//                 '阅读全文' + '</button>' + '<br/><br/>' + '<hr>' + '</div>';
//             }
//             // var html = '<div style="margin-top: 30px">' + '<h2>ceshi</h2>' + '<p style="color: #009688; margin-top: 10px">2020-01-01 | python</p>' +
//             //     '<p style="margin-top: 2%; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden;">' +
//             //     'table 模块是我们的又一走心之作，在 layui 2.0 的版本中全新推出，是 layui最核心的组成之一。它用于对表格进行一些列功能和动态化数据操作，涵盖了日常业务所涉及的几乎全部需求。支持固定表头、固定行、固定列左/列右，支持拖拽改变列宽度，支持排序，支持多级表头，支持单元格的自定义模板，支持对表格重载（比如搜索、条件筛选等），支持复选框，支持分页，支持单元格编辑等等一些列功能。尽管如此，我们仍将对其进行完善，在控制代码量和性能的前提下，不定期增加更多人性化功能。table模块也将是 layui 重点维护的项目之一' +
//             //     '</p><br/><br/>' + '<button type="button" class="layui-btn layui-btn-primary layui-btn-sm" style="float: right">' +
//             //     '阅读全文' + '</button>' + '<br/><br/>' + '<hr>' + '</div>';
//             $("#tab_content_detail").html(html)
//
//         }
//         if (lay_id == "2") {
//             html = '<li class="layui-timeline-item">' +
//                 '<i class="layui-icon layui-timeline-axis"></i>' +
//                 '<div class="layui-timeline-content layui-text">' +
//                 '<h3 class="layui-timeline-title">8月18日</h3>' +
//                 '<ul>' +
//                 '<li>《登高》</li>' +
//                 '<li>《茅屋为秋风所破歌》</li>' +
//                 '</ul>' +
//                 '</div>' + '</li>';
//             $("#tab_content_detail").html(html)
//         }
//     });
// });


