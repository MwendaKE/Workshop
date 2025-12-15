// Simple city → latitude/longitude map
let cities = {
    "nairobi": { lat: -1.286389, lon: 36.817223 },
    "mombasa": { lat: -4.0435, lon: 39.6682 },
    "kampala": { lat: 0.3476, lon: 32.5825 }
};

// Get weather data
function checkWeather() {
    let name = document.getElementById("city").value.toLowerCase();

    // Check if city exists in our list
    if (!cities[name]) {
        document.getElementById("output").innerText = "City not found.";
        return;
    }

    let lat = cities[name].lat;
    let lon = cities[name].lon;

    // Use OpenMeteo API (no key needed)
    let url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    // Fetch data from API
    fetch(url)
    .then(response => response.json())
    .then(data => {

        // Extract temperature from result
        let temp = data.current_weather.temperature;

        document.getElementById("output").innerText =
            "Current Temperature: " + temp + "°C";
    })
    .catch(() => {
        document.getElementById("output").innerText = "Error fetching weather.";
    });
}