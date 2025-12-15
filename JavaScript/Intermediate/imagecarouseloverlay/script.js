// ------------------------------------------------------
// ADVANCED FADE CAROUSEL WITH OVERLAY + ARROWS
// ------------------------------------------------------
// LOGIC:
// • All images and overlays are paired (image then overlay)
// • Only "active" image is visible
// • Overlay following the active image becomes visible
// • Arrows allow manual movement
// • We can add auto-play if needed
// ------------------------------------------------------

// Get all images
let slides = document.querySelectorAll(".carousel img");

// Get all overlays (each corresponds to a slide)
let overlays = document.querySelectorAll(".overlay");

// Current slide index
let index = 0;

/* ----------------------------
   Function to move to any slide
----------------------------- */
function showSlide(i) {
    // Remove current active classes
    slides[index].classList.remove("active");
    overlays[index].style.opacity = "0";

    // Update index (circular looping)
    index = i;
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    // Activate new slide
    slides[index].classList.add("active");
    overlays[index].style.opacity = "1";
}

/* ----------------------------
   Next + Previous Buttons
----------------------------- */
document.getElementById("next").onclick = function () {
    showSlide(index + 1);
};

document.getElementById("prev").onclick = function () {
    showSlide(index - 1);
};

/* ----------------------------
   Optional Auto-Play (uncomment)
----------------------------- */
setInterval(() => {
     showSlide(index + 1);
}, 3000);
