const maxHeight = $(window).height() * 0.5;
$(window).on("scroll", function () {
    if (document.documentElement.scrollTop > maxHeight) {
        $("#navigation").css("transform", "translateY(0)");
    } else {
        $("#navigation").css("transform", "translateY(-62px)");
    }
});

