function showTime() {
    // Create a new Date object to get the current date and time
    let now = new Date();

    // Convert the time into a human-readable format (HH:MM:SS)
    let time = now.toLocaleTimeString();

    // Find the HTML element with id="time" and display the time inside it
    document.getElementById("time").innerText = time;
}

// Call the showTime function every 1000 milliseconds (1 second)
// This keeps updating the clock in real-time
setInterval(showTime, 1000);

// Call the function once immediately when the page loads
// This shows the time instantly without waiting 1 second
showTime();