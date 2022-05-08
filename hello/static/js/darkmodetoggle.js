window.onload = function () {
    if (localStorage.getItem("darkmode")) {
        document.body.setAttribute("data-theme", localStorage.getItem('darkmode'));
    } else {
        document.body.setAttribute("data-theme", "dark_theme");
    }
}

function setThemePreference() {
    $("#darkmode-btn").addClass("animation-spin")
    setTimeout(function () {
        $("#darkmode-btn").removeClass("animation-spin")
    }, 500)

    if (localStorage.getItem("darkmode") == "light_theme") {
        localStorage.setItem("darkmode", "dark_theme");
        document.body.setAttribute("data-theme", "dark_theme");
        toggleDarkmode = true;
    } else {
        localStorage.setItem("darkmode", "light_theme");
        document.body.setAttribute("data-theme", "light_theme");
        toggleDarkmode = false;
    }
}