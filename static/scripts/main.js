// AJAX for posting
function get_random_city() {
    console.log("Preparing to get city") // sanity check
    $.ajax({
        url : "/api/v1/get_random_city", // the endpoint
        type : "GET", // http method

        // handle a successful response
        success : function(result) {
            $("#loading-div").remove(); // remove the loading sign
            $("#results").html("<h1 id='name'>" + result + "</h1>")
            console.log(result); // log the returned json to the console
            console.log("Success in getting city"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $("#loading-div").remove(); // remove the loading sign
            var error_box = $("<div data-alert>")
            error_box.attr("class", "alert-box alert radius").text("Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a>").appendTo("#results") // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$(document).ready(function() {
  get_random_city();
});
