let quotes = {
    motivation: ["Keep going", "Believe", "Never stop"],
    life: ["Life is short", "Live fully", "Be kind"],
    success: ["Work hard", "Stay focused", "Be disciplined"]
};

// Show random quote
function newQuote() {
    let cat = document.getElementById("cat").value;

    let list = quotes[cat];                          // Pick category
    let i = Math.floor(Math.random() * list.length); // Random index

    document.getElementById("quote").innerText = list[i];
}

newQuote();