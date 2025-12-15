let seconds = 0;          // Total seconds passed
let timer = null;         // Will store the interval ID

// Start counting every second
function startWatch() {

    // Prevent starting multiple timers
    if (timer !== null) return;

    timer = setInterval(function() {
        seconds++;

        // Convert seconds to minutes + seconds
        let mins = Math.floor(seconds / 60);
        let secs = seconds % 60;

        // Format seconds to 2 digits
        if (secs < 10) secs = "0" + secs;

        // Display time
        document.getElementById("display").innerText = mins + ":" + secs;

    }, 1000);
}

// Stop counting
function stopWatch() {
    clearInterval(timer);
    timer = null;
}

// Reset back to 0
function resetWatch() {
    stopWatch();          // Stop first
    seconds = 0;          // Reset count
    document.getElementById("display").innerText = "0:00";
}