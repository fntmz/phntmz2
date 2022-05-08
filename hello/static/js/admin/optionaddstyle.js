var count = $("body option").length;

$(window).on("load", function () {
    for (let i = 0; i < count + 1; i++) {
        $("body option:nth-child(" + i + ")").css({
            "color": "black",
        });
    }
});
