$(document).ready(function() {
    $("#id_department").select2({ width: '100%', maximumSelectionLength: 10 });
})

$(document).ready(function(){
        $("#datepicker_0").datepicker({
            onSelect: function(selected){
                $("#datepicker_1").datepicker("option","minDate", selected)
            }
        });
        $("#datepicker_1").datepicker({
            onSelect: function(selected){
                $("#datepicker_0").datepicker("option","maxDate", selected)
            }
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

