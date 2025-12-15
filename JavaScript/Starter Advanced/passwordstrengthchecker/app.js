// Check password strength using simple rules
function checkStrength() {
    let pass = document.getElementById("pass").value;
    let res = document.getElementById("result");

    // Basic strength rules using regex
    let strong = /(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}/;
    let medium = /(?=.*[A-Za-z])(?=.*\d).{6,}/;

    // Strong password
    if (strong.test(pass)) {
        res.innerText = "Strength: Strong";
        res.style.color = "green";
    }
    // Medium password
    else if (medium.test(pass)) {
        res.innerText = "Strength: Medium";
        res.style.color = "orange";
    }
    // Weak password
    else {
        res.innerText = "Strength: Weak";
        res.style.color = "red";
    }
}