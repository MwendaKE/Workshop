// Get the input field and the strength display area
let password = document.getElementById("password");
let strength = document.getElementById("strength");

// Run code whenever the user types
password.addEventListener("input", function () {

    // Store the typed password in a variable
    let pass = password.value;

    // Very simple strength logic:
    // Short = weak, medium length = medium, long = strong
    if (pass.length < 4) {
        strength.innerText = "Weak";
    } else if (pass.length < 8) {
        strength.innerText = "Medium";
    } else {
        strength.innerText = "Strong";
    }
});