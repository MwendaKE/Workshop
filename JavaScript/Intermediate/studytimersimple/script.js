// -------------------------------
// Study Timer Logic (Simple JS)
// -------------------------------

// Get HTML elements
var timeDisplay = document.getElementById("time");
var startBtn = document.getElementById("start");
var pauseBtn = document.getElementById("pause");
var resetBtn = document.getElementById("reset");

// Timer variables
var seconds = 0;
var timer = null;   // Will store setInterval

// Convert seconds → HH:MM:SS format
function formatTime(sec) {
    var hrs = Math.floor(sec / 3600);
    var mins = Math.floor((sec % 3600) / 60);
    var secs = sec % 60;

    // Add leading zero if number < 10
    if (hrs < 10) hrs = "0" + hrs;
    if (mins < 10) mins = "0" + mins;
    if (secs < 10) secs = "0" + secs;

    return hrs + ":" + mins + ":" + secs;
}

// Start timer function
function startTimer() {
    // Avoid multiple intervals running
    if (timer !== null) return;

    timer = setInterval(function() {
        seconds = seconds + 1;               // Increase time
        timeDisplay.textContent = formatTime(seconds);  // Update screen
    }, 1000); // Run every second
}

// Pause timer function
function pauseTimer() {
    clearInterval(timer);   // Stop the counting
    timer = null;
}

// Reset timer function
function resetTimer() {
    clearInterval(timer);
    timer = null;
    seconds = 0;
    timeDisplay.textContent = "00:00:00";
}

// Add button clicks
startBtn.onclick = startTimer;
pauseBtn.onclick = pauseTimer;
resetBtn.onclick = resetTimer;