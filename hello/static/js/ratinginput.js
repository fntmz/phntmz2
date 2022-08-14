$(".ratings").bind("click", function () {
    var divs = $(".ratings");
    var curIdx = divs.index($(this)) + 1;

    $("#rating-input").val(curIdx);
    $("#rating-submit").click();
});

$(document).ready(function () {
    if ($("#current-rating")) {
        for (var i = 0; i < parseInt($("#current-rating").text()); i++) {
            $(".ratings").eq(i).css("color", "var(--a-highlight");
        }
    }
});
