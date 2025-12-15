// Select the toggle button
let toggle = document.getElementById("toggle");

// When the button is clicked, switch themes
toggle.addEventListener("click", function () {

    // If background is already dark, switch to light mode
    if (document.body.style.background === "black") {

        // Set background to white
        document.body.style.background = "white";

        // Set text color to black
        document.body.style.color = "black";
    } 
    // Otherwise, switch to dark mode
    else {
        document.body.style.background = "black";
        document.body.style.color = "white";
    }
});