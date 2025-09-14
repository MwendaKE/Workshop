document.getElementById("lookup").onclick = () => {
    const input = document.getElementById("lookup-city");
    const location = input.value.trim();
    
    const apikey = "b5f7005b05b31b232f35daab3064b835";
    
    fetch(`https://api.weatherstack.com/current?access_key=${apikey}&query=${encodeURIComponent(location)}`)
        .then(response => response.json())
        .then(data => {
          displayWeatherData(data);
        })
        .catch(error => {
          console.log(error);
        });

      input.value = '';
};

function displayWeatherData(data) {
    const location = data.location;
    const instantWeather = data.current;
    
    document.getElementById("body").style.backgroundImage = `url(${instantWeather.weather_icons[0]})`;
    document.getElementById("body").style.backgroundRepeat = 'no-repeat';
    document.getElementById("body").style.backgroundSize = 'cover';
    document.getElementById("body").style.backdropFilter = "blur(100px)";
    
    document.getElementById("loc").innerText = `Showing weather data for: ${location.name}, ${location.country}`;
    document.getElementById("img").src = instantWeather.weather_icons[0];
    document.getElementById("desc").innerText = `Description: ${instantWeather.weather_descriptions[0]}`;
    document.getElementById("temp").innerText = `Temperature: ${instantWeather.temperature} ⁰C`;
    document.getElementById("feelike").innerText = `Feels Like: ${instantWeather.feelslike} ⁰C`;
    document.getElementById("winspeed").innerText = `Wind Speed: ${instantWeather.wind_speed} km/h`;
    document.getElementById("humid").innerText =  `Humidity: ${instantWeather.humidity} %`;
    document.getElementById("uv").innerText =  `UV Index: ${instantWeather.uv_index}`;
    document.getElementById("obstime").innerText =  `Observation Time: ${instantWeather.observation_time}`;
}
