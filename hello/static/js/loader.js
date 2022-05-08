window.addEventListener("scroll", noScroll);

function noScroll() {
    window.scrollTo(0, 0);
}

$(window).on("load", function () {
    window.removeEventListener("scroll", noScroll);
})