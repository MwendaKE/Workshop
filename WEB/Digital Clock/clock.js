document.addEventListener("DOMContentLoaded", (event) => {
    showCurrentTime();
});

function showCurrentTime() {
    const hourElem = document.getElementById("hour");
    const minElem = document.getElementById("min");
    const secElem = document.getElementById("sec");
    
    let time = new Date();
    
    let hours = time.getHours();
    let minutes = time.getMinutes();
    let seconds = time.getSeconds();
    
    hourElem.innerText = hours.toString().padStart(2,0);
    minElem.innerText = minutes.toString().padStart(2,0);
    secElem.innerText = seconds.toString().padStart(2,0);
    
    setTimeout(showCurrentTime, 1000);
}



