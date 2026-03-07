let warningTime = 1 * 60 * 1000; 
let logoutTime = 2 * 60 * 1000;

let warningTimer;
let logoutTimer;

function showWarningToast() {

    Toastify({
        text: "⚠️ You will be logged out in 1 minute due to inactivity",
        duration: 60000,
        gravity: "top",
        position: "right",
        backgroundColor: "#ff9800",
        close: true
    }).showToast();

}

function resetTimers() {

    clearTimeout(warningTimer);
    clearTimeout(logoutTimer);

    warningTimer = setTimeout(function () {
        showWarningToast();
    }, warningTime);

    logoutTimer = setTimeout(function () {
        window.location.href = "/accounts/login/";
    }, logoutTime);
}

window.onload = resetTimers;

document.onmousemove = resetTimers;
document.onkeypress = resetTimers;
document.onclick = resetTimers;
document.onscroll = resetTimers;