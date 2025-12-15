// ----------------------------
// API SETTINGS
// ----------------------------
const apiURL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false";

// DOM ELEMENTS
const cryptoBody = document.getElementById("cryptoBody");

// ----------------------------
// FETCH CRYPTO DATA
// ----------------------------
async function fetchCrypto() {
    try {
        // Fetch data from CoinGecko
        const response = await fetch(apiURL);
        const data = await response.json();

        // Clear table before updating
        cryptoBody.innerHTML = "";

        // Populate table rows
        data.forEach(coin => {
            const tr = document.createElement("tr");

            // Price change color
            const changeClass = coin.price_change_percentage_24h >= 0 ? "positive" : "negative";

            tr.innerHTML = `
                <td>${coin.name} (${coin.symbol.toUpperCase()})</td>
                <td>$${coin.current_price.toLocaleString()}</td>
                <td class="${changeClass}">${coin.price_change_percentage_24h.toFixed(2)}%</td>
                <td>$${coin.market_cap.toLocaleString()}</td>
            `;
            cryptoBody.appendChild(tr);
        });

    } catch (error) {
        console.error("Error fetching crypto data:", error);
        cryptoBody.innerHTML = "<tr><td colspan='4'>Failed to load data</td></tr>";
    }
}

// ----------------------------
// INITIAL LOAD
// ----------------------------
fetchCrypto();

// ----------------------------
// AUTO-UPDATE EVERY 10 SECONDS
// ----------------------------
setInterval(fetchCrypto, 10000);