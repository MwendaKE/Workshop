// Object containing quotes for each category
let quotes = {
    motivation: [
        "Believe in yourself.",
        "You are stronger than you think.",
        "Push harder than yesterday.",
        "Dream it. Wish it. Do it.",
        "Do something today that your future self will thank you for.",
        "Don't stop when you're tired. Stop when you're done.",
        "Little things make big days.",
        "Success doesn't just find you. You have to go get it.",
        "It's going to be hard, but hard does not mean impossible.",
        "Keep going. Everything you need will come to you at the perfect time."
    ],
    life: [
        "Life is what happens when you're busy making other plans.",
        "In the middle of every difficulty lies opportunity.",
        "Life is short. Smile while you still have teeth.",
        "Do what you can with what you have, where you are.",
        "The purpose of life is a life of purpose.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "The best way to predict your future is to create it.",
        "Life is really simple, but we insist on making it complicated.",
        "Turn your wounds into wisdom.",
        "Life is either a daring adventure or nothing at all."
    ],
    success: [
        "Success is not final; failure is not fatal: It is the courage to continue that counts.",
        "Don’t be afraid to give up the good to go for the great.",
        "I find that the harder I work, the more luck I seem to have.",
        "Success usually comes to those who are too busy to be looking for it.",
        "Opportunities don't happen. You create them.",
        "Don't wait for opportunity. Create it.",
        "The secret of success is to do the common thing uncommonly well.",
        "Action is the foundational key to all success.",
        "Success is the sum of small efforts repeated day in and day out.",
        "Great things never come from comfort zones."
    ]
};

// Current active tab
let currentTab = "motivation";

// Function to switch tabs
function switchTab(tabName) {
    currentTab = tabName; // Update current tab

    // Highlight active tab
    let tabElements = document.getElementsByClassName("tab");
    for (let i = 0; i < tabElements.length; i++) {
        tabElements[i].classList.remove("active");
    }

    // Add active class to the clicked tab
    event.target.classList.add("active");

    // Show a new random quote
    showQuote();
}

// Function to display a random quote from current tab
function showQuote() {
    let list = quotes[currentTab];
    let i = Math.floor(Math.random() * list.length);
    document.getElementById("quote").innerText = list[i];
}

// Initial quote on page load
showQuote();