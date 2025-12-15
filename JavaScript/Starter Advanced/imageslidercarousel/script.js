// Get the slides container
let slides = document.getElementById("slides");

// Count how many images are inside the slider
let totalImages = slides.children.length;

// Track which image index we are showing (start with 0)
let index = 0;

// This function moves the slider to the next image
function nextSlide() {

    // Increase index to show the next image
    index++;

    // If the index becomes bigger than last image, restart from 0
    if (index >= totalImages) {
        index = 0;
    }

    /* 
       Move the slides container to the left.
       -400px per image (because each image width is 400px)
       Example:
       index = 1 → move to -400px
       index = 2 → move to -800px
    */
    slides.style.transform = `translateX(-${index * 400}px)`;
}

// Automatically change image every 1 second (1000 ms)
setInterval(nextSlide, 1000);