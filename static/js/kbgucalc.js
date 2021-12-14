$(document).ready(function(){
    $('#button1').click(function(){
        var weight = $('#weight').val();
        var height = $('#height').val();
        var age = $('#age').val();
        var active = $('#active').val();
        var gender = $('input[name=gender]:checked').val();
        if (gender != 5){gender = -161};
        var res_food = (10 * weight + 6.25 * height - 5 * age + gender) * active;
        var norm_weight = height - 100 - (height - 150) * 0.5;

        $('#k_pod').empty().append(Math.round(res_food) + " Ккал");
        $('#b_pod').empty().append(Math.round(res_food * 0.3 * 0.25) + " г");
        $('#j_pod').empty().append(Math.round(res_food * 0.3 * 0.113) + " г");
        $('#u_pod').empty().append(Math.round(res_food * 0.4 * 0.25) + " г");

        $('#k_nab').empty().append(Math.round(res_food * 1.15) + " Ккал");
        $('#b_nab').empty().append(Math.round(res_food * 0.3 * 0.25 * 1.15) + " г");
        $('#j_nab').empty().append(Math.round(res_food * 0.3 * 0.113 * 1.15) + " г");
        $('#u_nab').empty().append(Math.round(res_food * 0.4 * 0.25 * 1.15) + " г");

        $('#k_poh').empty().append(Math.round(res_food * 0.8) + " Ккал");
        $('#b_poh').empty().append(Math.round(res_food * 0.3 * 0.25 * 0.8) + " г");
        $('#j_poh').empty().append(Math.round(res_food * 0.2 * 0.113 * 0.8) + " г");
        $('#u_poh').empty().append(Math.round(res_food * 0.5 * 0.25 * 0.8) + " г");
    });





});