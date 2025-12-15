// Get references to HTML elements
let text = document.getElementById("text");
let charCount = document.getElementById("charCount");
let wordCount = document.getElementById("wordCount");

// This event runs every time the user types inside the textarea
text.addEventListener("input", function () {

    // Get everything the user has typed
    let content = text.value;

    // Character count = total length of the text
    charCount.innerText = content.length;

    // Split text into words using spaces
    let words = content.trim().split(/\s+/);

    // If text is empty, word count = 0  
    // Otherwise, count the split words
    wordCount.innerText = content.trim() === "" ? 0 : words.length;
});