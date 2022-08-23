function toggleSection(title1, title2, section1, section2) {
    if ($("#toggle-btn").text() == title1) {
        $("#toggle-btn").text(title2);
        $(section1).fadeIn("slow");
        $(section2).fadeOut("slow");
    } else {
        $("#toggle-btn").text(title1);
        $(section1).fadeOut("slow");
        $(section2).fadeIn("slow");
    }
}
