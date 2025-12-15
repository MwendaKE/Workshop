// Create an array (a list) that holds all the quotes
let quotes = [
    "Believe in yourself.",
    "Stay positive.",
    "Keep moving forward.",
    "Success is no accident.",
    "Discipline beats motivation."
];

// Function that picks a new random quote
function newQuote() {
    // Generate a random number from 0 to (quotes.length - 1)
    // Math.random() gives a number between 0 and 1
    // Multiplying by quotes.length gives a number in the range of the array size
    // Math.floor() removes decimals so we get a whole number index
    let i = Math.floor(Math.random() * quotes.length);

    // Find the HTML element with id="quote" and display the selected quote
    document.getElementById("quote").innerText = quotes[i];
}