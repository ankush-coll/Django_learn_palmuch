let warningTime = 1 * 60 * 1000; 
let logoutTime = 2 * 60 * 1000;

let warningTimer;
let logoutTimer;

function resetTimers() {

    clearTimeout(warningTimer);
    clearTimeout(logoutTimer);

    warningTimer = setTimeout(function() {
        alert("You will be logged out in 1 minute due to inactivity.");
    }, warningTime);

    logoutTimer = setTimeout(function() {
        window.location.href = "/accounts/login/";
    }, logoutTime);
}

window.onload = resetTimers;

document.onmousemove = resetTimers;
document.onclick = resetTimers;
document.onscroll = resetTimers;