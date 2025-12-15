// Simple product list
let products = ["Bread", "Milk", "Sugar", "Rice", "Flour", "Oil"];

// Display all at start
let list = document.getElementById("list");
showAll(products);

// Show full list
function showAll(arr) {
    list.innerHTML = "";
    arr.forEach(function(p) {
        let li = document.createElement("li");
        li.innerText = p;
        list.appendChild(li);
    });
}

// Filter products by search text
function filterProducts() {
    let text = document.getElementById("search").value.toLowerCase();

    // Filter items that contain the search term
    let filtered = products.filter(function(p) {
        return p.toLowerCase().includes(text);
    });

    showAll(filtered);
}