$(document).ready(function(){
    $('#btn-post').click(function(){
        $.ajax({
            url: 'ajax/num',
            method: 'post',
            data: {
                phone: $('#phone').val(),
                name: $('#name').val(),
                secname: $('#secname').val(),
            },
            success: function(){
                alert("Теперь на ваш номер телефона будет поступать информация об акциях.");
            },
            failure: function(){
                alert(response.val());
            }
        });
    });

});