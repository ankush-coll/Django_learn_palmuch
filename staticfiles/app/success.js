function LoginSuccess(user){
    Toastify({
        text:`Login success!! Welcome dear ${user} 😄`,
        duration:3500,
        gravity:"top",
        position:"center",
        backgroundColor:"#0eaa1e",
        close:true
    }).showToast();
}

function OTPSuccess(){
    Toastify({
        text:"OTP validation success!! 😄",
        duration:3500,
        gravity:"top",
        position:"center",
        backgroundColor:"#0eaa1e",
        close:true
    }).showToast();
}

// duration: 25000,
//         gravity: "top",
//         position: "right",
//         backgroundColor: "#a81111",
//         close: true
//     }).showToast();
