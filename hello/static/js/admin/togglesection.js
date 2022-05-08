var toggle = false

function toggleSection() {
    if (toggle == false) {
        toggle = true
        $("#toggle-btn").text("login")
        $("#register-section").fadeIn("slow");
        $("#login-section").fadeOut("slow");
    } else {
        toggle = false
        $("#toggle-btn").text("register")
        $("#register-section").fadeOut("slow");
        $("#login-section").fadeIn("slow");
    }
}