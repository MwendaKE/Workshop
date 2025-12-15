// -----------------------------------------------
// SOFT FADE + ZOOM CAROUSEL (NO DOTS)
// -----------------------------------------------
// CAROUSEL LOGIC:
// 1. All images are stacked on top of each other.
// 2. Only the "active" image is visible (opacity:1).
// 3. We switch images every 2 seconds.
// 4. CSS fades old image out and fades new one in.
// 5. Also slight zoom animation to add smoothness.
// -----------------------------------------------

// Collect all images
let slides = document.querySelectorAll(".carousel img");

// Track which slide is currently visible
let index = 0;

// Change to the next slide
function nextSlide() {
    // Remove active class from current image
    slides[index].classList.remove("active");

    // Move to next index
    index++;
    if (index >= slides.length) {
        index = 0;  // Loop to first image
    }

    // Add active class to new image
    slides[index].classList.add("active");
}

// Auto change image every 2 seconds
setInterval(nextSlide, 2000);