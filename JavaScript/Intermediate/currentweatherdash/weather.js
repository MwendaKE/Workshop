// Replace with your OpenWeatherMap API key
const API_KEY = "";

// Elements
const cityInput = document.getElementById("cityInput");
const getWeatherBtn = document.getElementById("getWeatherBtn");
const weatherInfo = document.getElementById("weatherInfo");
const cityNameEl = document.getElementById("cityName");
const temperatureEl = document.getElementById("temperature");
const descriptionEl = document.getElementById("description");
const weatherIconEl = document.getElementById("weatherIcon");

// Function to fetch weather by city name
async function getWeatherByCity(city) {
    try {
        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`
        );

        if (!response.ok) throw new Error("City not found");

        const data = await response.json();
        showWeather(data);

    } catch (err) {
        alert(err.message);
        weatherInfo.style.display = "none";
    }
}

// Function to fetch weather by coordinates (latitude, longitude)
async function getWeatherByCoords(lat, lon) {
    try {
        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        );

        if (!response.ok) throw new Error("Unable to get weather for your location");

        const data = await response.json();
        showWeather(data);

    } catch (err) {
        alert(err.message);
        weatherInfo.style.display = "none";
    }
}

// Display weather data in UI
function showWeather(data) {
    const name = data.name;
    const temp = data.main.temp;
    const description = data.weather[0].description;
    const icon = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;

    cityNameEl.textContent = name;
    temperatureEl.textContent = `Temperature: ${temp} °C`;
    descriptionEl.textContent = `Weather: ${description}`;
    weatherIconEl.src = icon;
    weatherIconEl.alt = description;

    weatherInfo.style.display = "block";
}

// Detect user location on page load
window.addEventListener("load", () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                getWeatherByCoords(lat, lon);
            },
            (error) => {
                console.warn("Geolocation failed: ", error.message);
                // fallback: show default city
                getWeatherByCity("Nairobi");
            }
        );
    } else {
        alert("Geolocation is not supported by your browser.");
        getWeatherByCity("Nairobi"); // fallback
    }
});

// Search button event
getWeatherBtn.addEventListener("click", () => {
    const city = cityInput.value.trim();
    if (city !== "") {
        getWeatherByCity(city);
    }
});

// Optional: Enter key to search
cityInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") getWeatherBtn.click();
});
