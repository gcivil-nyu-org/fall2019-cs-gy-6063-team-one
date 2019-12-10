$(document).ready(function(){
    $("#withdraw_button").show();
    $("#withdraw").hide();

    $("#withdraw_button").click(function(){
        $("#withdraw_button").hide();
        $("#withdraw").show();
    });

    $("#no").click(function(){
        $("#withdraw").hide();
        $("#withdraw_button").show();
    });

    // If the application status has the W class, indicating an application status of
    // WITHDRAWN, add grey coloring to the job details and personal details
    if ($(".W")){
        $("#job_details").addClass("W_text");
        $("#personal_details").addClass("W_text");
    }

});