const passwordInput = document.getElementById("password");

passwordInput.addEventListener("input", function () {
    console.log("Password typing detected:", passwordInput.value);
});