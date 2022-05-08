var toggle = false;
function toggleNavbar() {
    let count = $("#navbar-content > *").length;
    if (toggle == false) {
        toggle = true;
        $("section:nth-child(1)").css("width", "100%");
        $("section:nth-child(2)").css("width", "576px");
        $("#navbar-back-text").css("opacity", "1")

        setTimeout(function () {
            $("#navbar-content").css("visibility", "visible");
        }, 300);
        for (let i = 0; i < count + 1; i++) {
            setTimeout(function () {
                $("#navbar-content > *:nth-child(" + i + ")").css(
                    "opacity",
                    "1"
                );
                $("#navbar-content > *:nth-child(" + i + ")").css(
                    "top",
                    "0"
                );
            }, 200 * i + 100);
        }
    } else {
        toggle = false;
        for (let i = 0; i < count + 1; i++) {
            setTimeout(function () {
                $(
                    "#navbar-content > *:nth-last-child(" +
                    (i + 1) +
                    ")"
                ).css("opacity", "0");
                $(
                    "#navbar-content > *:nth-last-child(" +
                    (i + 1) +
                    ")"
                ).css("top", "10px");
            }, 200 * i);
        }
        setTimeout(function () {
            $("#navbar-back-text").css("opacity", "0")
            $("#navbar-content").css("visibility", "hidden");
            $("section:nth-child(1)").css("width", "100%");
            $("section:nth-child(2)").css("width", "90px");
        }, 200 * count);
    }
}