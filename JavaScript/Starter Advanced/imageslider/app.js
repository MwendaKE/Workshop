let images = [
    "https://picsum.photos/300?1",
    "https://picsum.photos/300?2",
    "https://picsum.photos/300?3"
];

let index = 0;

// Show first image
document.getElementById("img").src = images[index];

// Change image
function next() {
    index++;
    if (index >= images.length) index = 0;
    document.getElementById("img").src = images[index];
}