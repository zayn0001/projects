$(function () {
    $(".navbar-toggler").blur(function (event){
        var screenWidth = window.innerWidth;
        if (screenWidth < 992) {
            $("#navbarSupportedContent").collapse("hide");
        }
    })
})