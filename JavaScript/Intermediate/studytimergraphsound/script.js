// -------------------------------
// STUDY TIMER
// -------------------------------

// Get elements
var timeDisplay = document.getElementById("time");
var startBtn = document.getElementById("start");
var pauseBtn = document.getElementById("pause");
var resetBtn = document.getElementById("reset");
var dingSound = document.getElementById("dingSound");

// Timer variables
var seconds = 0;
var timer = null;

// Format time to HH:MM:SS
function formatTime(s) {
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    var sec = s % 60;

    if (h < 10) h = "0" + h;
    if (m < 10) m = "0" + m;
    if (sec < 10) sec = "0" + sec;

    return h + ":" + m + ":" + sec;
}

// Start timer
function startTimer() {
    if (timer !== null) return;

    timer = setInterval(function() {
        seconds++;

        // Update display
        timeDisplay.textContent = formatTime(seconds);

        // Play sound at 25 minutes (1500 sec)
        if (seconds === 1500) {
            dingSound.play();
            saveStudyMinutes(Math.floor(seconds / 60));
            drawChart();
        }

    }, 1000);
}

// Pause timer
function pauseTimer() {
    clearInterval(timer);
    timer = null;
}

// Reset timer
function resetTimer() {
    clearInterval(timer);
    timer = null;
    seconds = 0;
    timeDisplay.textContent = "00:00:00";
}

// Buttons
startBtn.onclick = startTimer;
pauseBtn.onclick = pauseTimer;
resetBtn.onclick = resetTimer;

// -------------------------------
// SAVE DAILY STUDY DATA
// -------------------------------

// We store minutes in localStorage
function saveStudyMinutes(min) {
    var today = new Date().toISOString().slice(0, 10); // yyyy-mm-dd

    var stored = localStorage.getItem("studyData");
    var data = stored ? JSON.parse(stored) : {};

    if (!data[today]) {
        data[today] = 0;
    }

    data[today] += min;

    localStorage.setItem("studyData", JSON.stringify(data));
}

// -------------------------------
// DRAW SIMPLE BAR CHART
// -------------------------------

function drawChart() {
    var canvas = document.getElementById("studyChart");
    var ctx = canvas.getContext("2d");

    // Reset chart
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    var stored = localStorage.getItem("studyData");
    var data = stored ? JSON.parse(stored) : {};

    var keys = Object.keys(data);
    var values = Object.values(data);

    // Draw bars
    var barWidth = (canvas.width - 40) / keys.length;
    var max = Math.max(...values, 10); // so graph never looks empty

    keys.forEach(function(day, i) {
        var barHeight = (values[i] / max) * 150;

        ctx.fillStyle = "#28a745";
        ctx.fillRect(20 + i * barWidth, 180 - barHeight, barWidth - 15, barHeight);

        ctx.fillStyle = "#000";
        ctx.font = "10px Arial";
        ctx.fillText(values[i] + "m", 20 + i * barWidth, 175 - barHeight);

        ctx.fillText(day.slice(5), 20 + i * barWidth, 195);
    });
}

// Draw chart on page load
drawChart();