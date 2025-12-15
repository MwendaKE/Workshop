let countdown = null;   // Stores setInterval ID

function startCountdown() {
    let secs = parseInt(document.getElementById("seconds").value);

    // If the user enters nothing, stop
    if (isNaN(secs) || secs <= 0) return;

    // Clear any previous countdown
    clearInterval(countdown);

    // Display immediately
    document.getElementById("display").innerText = secs;

    // Start counting down
    countdown = setInterval(function() {

        secs--;  // Reduce seconds by 1

        document.getElementById("display").innerText = secs;

        // When countdown finishes
        if (secs <= 0) {
            clearInterval(countdown);
            document.getElementById("display").innerText = "Done!";
        }

    }, 1000);   // Runs every 1 second
}