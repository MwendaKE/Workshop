import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [location, setLocation] = useState("");
  const [weather, setWeather] = useState(null);
  const [forecast, setForecast] = useState([]);
  const [loading, setLoading] = useState(false);

  const API_KEY = "b5f7005b05b31b232f35daab3064b835"; // <-- replace with your key

  // Fetch weather
  const getWeather = (query) => {
    if (!query) return;

    setLoading(true);
    fetch(
      `https://api.weatherstack.com/current?access_key=${API_KEY}&query=${encodeURIComponent(
        query
      )}`
    )
      .then((res) => res.json())
      .then((data) => {
        if (data.success === false || !data.current) {
          alert("City not found or invalid key");
          setWeather(null);
          setForecast([]);
        } else {
          setWeather(data);

          // Create simple 5-day fake forecast using current temp (Weatherstack free API doesn't give full forecast)
          const fakeForecast = Array.from({ length: 5 }, (_, i) => ({
            day: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][
              new Date().getDay() + i > 6 ? (new Date().getDay() + i) % 7 : new Date().getDay() + i
            ],
            temp: data.current.temperature + i,
            icon: data.current.weather_icons[0],
          }));
          setForecast(fakeForecast);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        alert("Error fetching data");
        setLoading(false);
      });

    setLocation("");
  };

  // Detect user location on load
  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((pos) => {
        const coords = `${pos.coords.latitude},${pos.coords.longitude}`;
        getWeather(coords);
      });
    }
  }, []);

  return (
    <div className="app-container">
      <div className="weather-box">
        <h2>🌤 Cute Weather App</h2>

        <input
          type="text"
          placeholder="Enter city..."
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />

        <button onClick={() => getWeather(location)}>Search</button>

        {loading && <p className="loading">Loading...</p>}

        {weather && (
          <div className="results">
            <h3>
              {weather.location.name}, {weather.location.country}
            </h3>
            <img src={weather.current.weather_icons[0]} alt="icon" />
            <p>Temperature: {weather.current.temperature}°C</p>
            <p>Humidity: {weather.current.humidity}%</p>
            <p>Wind: {weather.current.wind_speed} m/s</p>

            <h4>5-Day Forecast</h4>
            <div className="forecast">
              {forecast.map((day, idx) => (
                <div className="day-card" key={idx}>
                  <p>{day.day}</p>
                  <img src={day.icon} alt="icon" />
                  <p>{day.temp}°C</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

