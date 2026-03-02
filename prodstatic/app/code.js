document.addEventListener("DOMContentLoaded", function () {
    let slides = document.querySelectorAll(".slide");
    let index = 0;

    setInterval(() => {
        slides[index].classList.remove("active");
        index = (index + 1) % slides.length;
        slides[index].classList.add("active");
    }, 3000);
});

function openMenu() {
        document.getElementById("mySidebar").style.width = "250px";
    }

    function closeMenu() {
        document.getElementById("mySidebar").style.width = "0";
    }