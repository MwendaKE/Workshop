// ----------------------------
// API SETTINGS
// ----------------------------
const apiURL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false";

// DOM ELEMENTS
const cryptoBody = document.getElementById("cryptoBody");
const searchBox = document.getElementById("searchBox");

let cryptoData = []; // Store fetched data for filtering

// ----------------------------
// FETCH CRYPTO DATA
// ----------------------------
async function fetchCrypto() {
    try {
        const response = await fetch(apiURL);
        const data = await response.json();

        cryptoData = data; // Save to global variable
        displayCrypto(data);
    } catch (error) {
        console.error("Error fetching crypto data:", error);
        cryptoBody.innerHTML = "<tr><td colspan='4'>Failed to load data</td></tr>";
    }
}

// ----------------------------
// DISPLAY CRYPTO
// ----------------------------
function displayCrypto(data) {
    cryptoBody.innerHTML = "";
    data.forEach(coin => {
        const tr = document.createElement("tr");
        const changeClass = coin.price_change_percentage_24h >= 0 ? "positive" : "negative";

        tr.innerHTML = `
            <td>${coin.name} (${coin.symbol.toUpperCase()})</td>
            <td>$${coin.current_price.toLocaleString()}</td>
            <td class="${changeClass}">${coin.price_change_percentage_24h.toFixed(2)}%</td>
            <td>$${coin.market_cap.toLocaleString()}</td>
        `;
        cryptoBody.appendChild(tr);
    });
}

// ----------------------------
// SEARCH FILTER
// ----------------------------
searchBox.addEventListener("input", () => {
    const query = searchBox.value.toLowerCase();
    const filtered = cryptoData.filter(coin =>
        coin.name.toLowerCase().includes(query) || coin.symbol.toLowerCase().includes(query)
    );
    displayCrypto(filtered);
});

// ----------------------------
// INITIAL LOAD & AUTO UPDATE
// ----------------------------
fetchCrypto();
setInterval(fetchCrypto, 10000); // Refresh every 10s