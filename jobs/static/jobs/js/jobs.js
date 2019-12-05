$(document).ready(function() {
    $("#id_department").select2({ width: '100%', maximumSelectionLength: 10 });
})

$(document).ready(function(){


        $("#datepicker_0").datepicker({
            onSelect: function(selected){
                $("#datepicker_1").datepicker("option","minDate", selected)
            },
            changeMonth: true,
        });
        $("#datepicker_1").datepicker({
            onSelect: function(selected){
                $("#datepicker_0").datepicker("option","maxDate", selected)
            },
            changeMonth: true,
        });
        $('.datepicker').on('click', function(e) {
            e.preventDefault();
            $(this).attr("autocomplete", "off");
        });
});

$(document).ready(function() {

    $('a#advanced_options_link').click(function(){
        $('div#advanced_search_options').slideToggle();
        if (this.innerHTML === 'View advanced options') this.innerHTML = 'Hide advanced options';
        else {
            this.innerHTML = 'View advanced options';
        }
        return false;
    });

});

