layui.use('element', function () {
    var $ = layui.jquery
        , element = layui.element; //Tab的切换功能，切换事件监听等，需要依赖element模块

    element.on('tab(docDemoTabBrief)', function () {
        alert(this.getAttribute('lay-id'))
        var lay_id = this.getAttribute('lay-id');
        var html = ""
        if (lay_id == "index") {
            var html = '<div style="margin-top: 30px">' + '<h2>ceshi</h2>' + '<p style="color: #009688; margin-top: 10px">2020-01-01 | python</p>' +
                '<p style="margin-top: 2%; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden;">' +
                'table 模块是我们的又一走心之作，在 layui 2.0 的版本中全新推出，是 layui最核心的组成之一。它用于对表格进行一些列功能和动态化数据操作，涵盖了日常业务所涉及的几乎全部需求。支持固定表头、固定行、固定列左/列右，支持拖拽改变列宽度，支持排序，支持多级表头，支持单元格的自定义模板，支持对表格重载（比如搜索、条件筛选等），支持复选框，支持分页，支持单元格编辑等等一些列功能。尽管如此，我们仍将对其进行完善，在控制代码量和性能的前提下，不定期增加更多人性化功能。table模块也将是 layui 重点维护的项目之一' +
                '</p><br/><br/>' + '<button type="button" class="layui-btn layui-btn-primary layui-btn-sm" style="float: right">' +
                '阅读全文' + '</button>' + '<br/><br/>' + '<hr>' + '</div>';
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
    });
});
