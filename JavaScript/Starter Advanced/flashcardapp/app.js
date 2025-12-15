// Flashcard class to store question and answer
class Flashcard {
    constructor(q, a) {
        this.question = q;
        this.answer = a;
    }
}

// List of flashcards
let cards = [
    new Flashcard("Capital of Kenya?", "Nairobi"),
    new Flashcard("5 + 7?", "12"),
    new Flashcard("Hottest planet?", "Venus")
];

let index = 0; // Current card index

// Show the first card
showCard();

// Display current flashcard
function showCard() {
    let card = cards[index];
    document.getElementById("card").innerText =
        "Q: " + card.question + "\nA: " + card.answer;
}

// Move to next card
function nextCard() {
    index++;

    // Loop back to start if at end
    if (index >= cards.length) index = 0;

    showCard();
}

// Move to previous card
function prevCard() {
    index--;

    // Loop to last card if index becomes negative
    if (index < 0) index = cards.length - 1;

    showCard();
}