// Working currency API with full CORS support
let apiURL = "https://open.er-api.com/v6/latest/USD";

// Page elements
let amount = document.getElementById("amount");
let from = document.getElementById("from");
let to = document.getElementById("to");
let result = document.getElementById("result");

let rates = {}; // store fetched rates

// Load currency data
async function loadCurrencies() {
    try {
        let res = await fetch(apiURL);
        let data = await res.json();

        // If API fails
        if (data.result !== "success") {
            result.innerText = "Failed to load currency data.";
            return;
        }

        rates = data.rates; // store all rates

        // Fill dropdowns
        for (let code in rates) {
            let option1 = document.createElement("option");
            let option2 = document.createElement("option");

            option1.value = code;
            option2.value = code;

            option1.text = code;
            option2.text = code;

            from.appendChild(option1);
            to.appendChild(option2);
        }

        // Set defaults
        from.value = "USD";
        to.value = "EUR";
        convert();

    } catch (err) {
        result.innerText = "Error fetching exchange rates.";
    }
}

// Convert function
function convert() {
    let amt = Number(amount.value);

    if (!amt) {
        result.innerText = "Enter a valid amount.";
        return;
    }

    let fromRate = rates[from.value];
    let toRate = rates[to.value];

    let converted = (amt / fromRate) * toRate;

    result.innerText =
        amt + " " + from.value + " = " +
        converted.toFixed(3) + " " + to.value;
}

// Listen for input
amount.addEventListener("input", convert);
from.addEventListener("change", convert);
to.addEventListener("change", convert);

// Run
loadCurrencies();