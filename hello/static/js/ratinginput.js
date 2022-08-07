$(".ratings").click(function () {
    $("#rating-input").val($(this).index() - 1);
    $("#rating-submit").click();
});

$(document).ready(function () {
    if ($("#current-rating")) {
        for (var i = 0; i < parseInt($("#current-rating").text()); i++) {
            $(".ratings").eq(i).css("color", "var(--a-highlight");
        }
    }
});
