$(".estado").off().on('click', function (e) {
    e.preventDefault();
    let id = $(this).val()
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "/estado/",
        data: id,
        dataType: "JSON",
        error: function(xhr, status){

        },
        success: function (response) {
            
        }
    });
});