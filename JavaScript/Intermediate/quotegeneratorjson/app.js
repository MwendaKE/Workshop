let quotesData = {};          // Store quotes loaded from JSON
let currentTab = "motivation";
let loadedCount = 0;
const BATCH_SIZE = 5;

// Fetch JSON
fetch("quotes.json")
    .then(res => res.json())
    .then(data => {
        quotesData = data;
        showQuotes();
    })
    .catch(err => console.error("Error loading quotes:", err));

function switchTab(tabName) {
    currentTab = tabName;
    loadedCount = 0;
    document.getElementById("quotes-container").innerHTML = "";

    let tabElements = document.getElementsByClassName("tab");
    for (let i = 0; i < tabElements.length; i++) {
        tabElements[i].classList.remove("active");
    }

    event.target.classList.add("active");
    showQuotes();
}

// Show next batch of quotes
function showQuotes() {
    let container = document.getElementById("quotes-container");
    let list = quotesData[currentTab];

    for (let i = loadedCount; i < loadedCount + BATCH_SIZE && i < list.length; i++) {
        let item = list[i];
        let div = document.createElement("div");
        div.classList.add("quote");
        div.innerHTML = `<span class="quote-text">${item.quote}</span> ~ <span class="quote-author">${item.author}</span>`;
        container.appendChild(div);
    }

    loadedCount += BATCH_SIZE;
}

// Infinite scroll
window.addEventListener("scroll", function() {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 10) {
        if (loadedCount < quotesData[currentTab].length) {
            showQuotes();
        }
    }
});

// Open modal
function openModal() {
    document.getElementById("quote-modal").style.display = "block";
}

// Close modal when clicking outside
window.onclick = function(event) {
    let modal = document.getElementById("quote-modal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Add new quote
function addQuote() {
    let quoteText = document.getElementById("new-quote").value.trim();
    let authorText = document.getElementById("new-author").value.trim();
    let category = document.getElementById("new-category").value;

    if (quoteText && authorText) {
        // Add quote to data
        quotesData[category].push({quote: quoteText, author: authorText});

        // If current tab matches, show new quote immediately
        if (category === currentTab) {
            let container = document.getElementById("quotes-container");
            let div = document.createElement("div");
            div.classList.add("quote");
            div.innerHTML = `<span class="quote-text">${quoteText}</span> ~ <span class="quote-author">${authorText}</span>`;
            container.appendChild(div);
        }

        // Reset modal fields
        document.getElementById("new-quote").value = "";
        document.getElementById("new-author").value = "";
        document.getElementById("quote-modal").style.display = "none";
    } else {
        alert("Please enter both quote and author.");
    }
}