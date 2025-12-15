// Our list of products (array of objects)
let products = [
    { name: "Laptop", price: 850 },
    { name: "Phone", price: 500 },
    { name: "Headphones", price: 120 },
    { name: "Keyboard", price: 70 },
    { name: "Smartwatch", price: 250 },
    { name: "Speaker", price: 150 }
];

// Get HTML elements
let list = document.getElementById("list");
let search = document.getElementById("search");
let minPrice = document.getElementById("minPrice");
let maxPrice = document.getElementById("maxPrice");
let sort = document.getElementById("sort");

/*
  FUNCTION: showProducts(items)
  PURPOSE: Display products on the screen
*/
function showProducts(items) {
    list.innerHTML = ""; // clear old items

    items.forEach(function(p) {
        let div = document.createElement("div");
        div.className = "product";

        div.innerHTML = `
            <div class="product-title">${p.name}</div>
            <div>Price: $${p.price}</div>
        `;

        list.appendChild(div); // add to the page
    });
}

/*
  FUNCTION: filterProducts()
  PURPOSE:
  - Search by name
  - Filter by min/max price
  - Sort by name or price
*/
function filterProducts() {
    // Start with all products
    let result = products.slice();

    // ----- SEARCH -----
    let text = search.value.toLowerCase();
    if (text) {
        result = result.filter(function(p) {
            return p.name.toLowerCase().includes(text);
        });
    }

    // ----- PRICE FILTER -----
    let min = Number(minPrice.value);
    let max = Number(maxPrice.value);

    if (min) {
        result = result.filter(function(p) {
            return p.price >= min;
        });
    }

    if (max) {
        result = result.filter(function(p) {
            return p.price <= max;
        });
    }

    // ----- SORTING -----
    if (sort.value === "name") {
        result.sort(function(a, b) {
            return a.name.localeCompare(b.name);
        });
    }

    if (sort.value === "price") {
        result.sort(function(a, b) {
            return a.price - b.price;
        });
    }

    // Show final results
    showProducts(result);
}

// Run filter when input changes
search.addEventListener("input", filterProducts);
minPrice.addEventListener("input", filterProducts);
maxPrice.addEventListener("input", filterProducts);
sort.addEventListener("change", filterProducts);

// Show all on start
showProducts(products);