function send_detail(data) {
    return $.ajax({
        type: "post",
        dataType: "json",
        data: data,
        url: '/api/admin/article_add11/',
        timeout: 6000
        // beforeSend: function (xhr, settings) {
        //     xhr.setRequestHeader("X-CSRFToken", settings);
        // },
        // success: function (obj) {
        //     alert(obj.msg)
        //     return obj.msg
        // }
    })
}

layui.use(['form', 'layedit', 'laydate'], function () {
    var form = layui.form
        , layer = layui.layer
        , layedit = layui.layedit
        , laydate = layui.laydate;

    //日期
    laydate.render({
        elem: '#date'
        , value: new Date()
    });
    // laydate.render({
    //     elem: '#date1'
    // });

    layedit.set({
        uploadImage: {
            url: '/api/admin/add_image/',
        }
    });
    //创建一个编辑器
    var editIndex = layedit.build('LAY_demo_editor');

    //自定义验证规则
    form.verify({
        title: function (value) {
            if (value.length < 5) {
                return '标题至少得5个字符啊';
            }
        }
        , content: function (value) {
            return layedit.sync(editIndex);
        }
    });

    //监听指定开关
    form.on('switch(switchTest)', function (data) {
        layer.msg('开关checked：' + (this.checked ? 'true' : 'false'), {
            offset: '6px'
        });
        layer.tips('温馨提示：请注意开关状态的文字可以随意定义，而不仅仅是ON|OFF', data.othis)
    });

    //监听提交
    form.on('submit(demo1)', function (data) {
        // console.log(data.field);
        //});
        data = JSON.stringify(data.field);
        alert(data)
        send_detail(data)
            .done(function (response) {
                alert(response.msg)
                location.reload();
                // layer.open({
                //     type: 1,
                //     content: "保存成功" //这里content是一个DOM，注意：最好该元素要存放在body最外层，否则可能被其它的相对元素所影响
                // });
            })
        // var is_success = send_detail(data);
        // if (is_success == "success") {
        //     location.reload();
        //     alert('2222')
        // }
        // return false;
    });

});

