var input_is_inventoried;
var form_group;

$(function () {

    input_is_inventoried = $('input[name="is_inventoried"]');
    //form_group = document.getElementsByClassName('form-group');

    //console.log(input_is_inventoried);

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('input[name="pvp"]')
        .TouchSpin({
            min: 0.01,
            max: 1000000,
            step: 0.01,
            decimals: 2,
            boostat: 5,
            verticalbuttons: true,
            maxboostedstep: 10,
            prefix: '$'
        })
        .on('keypress', function (e) {
            return validate_decimals($(this), e);
        });

    $('input[name="stock"]')
        .TouchSpin({
            min: 0,
            max: 1000000,
            step: 1,
            verticalbuttons: true,
        })
        .on('keypress', function (e) {
            return validate_form_text('numbers', e, null);
        });

    input_is_inventoried.on('change', function(){
        //Video 22
       // var container = $(this).parent().parent();  // ubicamos en container principal=div
        //               buscamos en el contenedor el elemento stock
        //var container = $(this).parent().parent().find('input[name="stock"]');
        //     ahora buscamos el padre de este elemento porque tenemos que borrar tanto
        //     la etiqueta como el input
        var container = $(this).parent().parent().find('input[name="stock"]').parent().parent();
        //console.log(container);
        $(container).show();
        if (!this.checked) {
            $(container).hide();  // oculto el elemento 4 - stock
        }
        /*
        $(form_group[4]).show();
        if (!this.checked) {
            $(form_group[4]).hide();  // oculto el elemento 4 - stock
        }*/
    });

    if ($('input[name="action"]').val()==='edit'){
        input_is_inventoried.trigger('change');
    }

    //input_is_inventoried.removeClass();
});