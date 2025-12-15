// Fetch weather data from API
function getWeather() {
    let city = document.getElementById("city").value;

    // Simple public API (no key needed)
    let url = "https://wttr.in/" + city + "?format=%C+%t";

    fetch(url)
        .then(response => response.text())       // Convert to plain text
        .then(data => {
            document.getElementById("result").innerText = data;
        })
        .catch(err => {
            document.getElementById("result").innerText = "Error loading weather";
        });
}