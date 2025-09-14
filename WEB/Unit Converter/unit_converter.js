// Time Conversions

document.getElementById("user-input-time").addEventListener("input", function () {
    const userinput = this.value;
    const convertfrom = document.getElementById("units-from-time").value;
    const convertto = document.getElementById("units-to-time").value;
    
    let result;
    
    if (convertfrom === "hrs" && convertto === "mins") {
        result = userinput * 60;
    } else if (convertfrom === "hrs" && convertto === "secs"){
        result = userinput * 3600;
    } else if (convertfrom === "mins" && convertto === "hrs"){
        result = userinput / 60;
    } else if (convertfrom === "mins" && convertto === "secs"){
        result = userinput * 60;
    }else if (convertfrom === "secs" && convertto === "hrs"){
        result = userinput / 3600;
    } else if (convertfrom === "secs" && convertto === "mins"){
        result = userinput / 60;
    } else {return;}
    
    const resultcontainer = document.getElementById("result-time");
    resultcontainer.textContent = result;
    
});

// Distance Conversions

document.getElementById("user-input-distance").addEventListener("input", function () {
    const userinput = this.value;
    const convertfrom = document.getElementById("units-from-distance").value;
    const convertto = document.getElementById("units-to-distance").value;
    
    let result;
    
    // kms to x
    if (convertfrom === "kms" && convertto === "miles") {
        result = userinput * 0.621;
    } else if (convertfrom === "kms" && convertto === "yard") {
        result = userinput * 1094;
    } else if (convertfrom === "kms" && convertto === "mtrs") {
        result = userinput * 1000;
    } else if (convertfrom === "kms" && convertto === "cms") {
        result = userinput * 100000;
    } else if (convertfrom === "kms" && convertto === "foot") {
        result = userinput * 3281;
    } else if (convertfrom === "kms" && convertto === "inch") {
        result = userinput * 39370;
    // miles to x    
    } else if (convertfrom === "miles" && convertto === "mtrs") {
        result = userinput * 1609;
    } else if (convertfrom === "miles" && convertto === "cms") {
        result = userinput * 160900;
    } else if (convertfrom === "miles" && convertto === "kms") {
        result = userinput / 0.621;
    } else if (convertfrom === "miles" && convertto === "yard") {
        result = userinput * 1760;
    } else if (convertfrom === "miles" && convertto === "foot") {
        result = userinput * 5280;
    } else if (convertfrom === "miles" && convertto === "inch") {
        result = userinput * 63360;
    // inch to x
    } else if (convertfrom === "inch" && convertto === "mtrs") {
        result = userinput / 39.37;
    } else if (convertfrom === "inch" && convertto === "cms") {
        result = userinput * 2.54;
    } else if (convertfrom === "inch" && convertto === "miles") {
        result = userinput / 63360;
    } else if (convertfrom === "inch" && convertto === "yard") {
        result = userinput / 36;
    } else if (convertfrom === "inch" && convertto === "foot") {
        result = userinput / 12;
    } else if (convertfrom === "inch" && convertto === "kms") {
        result = userinput / 39370;
    // foot to x  
    } else if (convertfrom === "foot" && convertto === "mtrs") {
        result = userinput / 3.281;
    } else if (convertfrom === "foot" && convertto === "cms") {
        result = userinput * 30.48;
    } else if (convertfrom === "foot" && convertto === "kms") {
        result = userinput / 3281;
    } else if (convertfrom === "foot" && convertto === "yard") {
        result = userinput / 3;
    } else if (convertfrom === "foot" && convertto === "miles") {
        result = userinput / 5280;
    } else if (convertfrom === "foot" && convertto === "inch") {
        result = userinput * 12;
    // yard to x
    } else if (convertfrom === "yard" && convertto === "mtrs") {
        result = userinput / 1.094;
    } else if (convertfrom === "yard" && convertto === "cms") {
        result = userinput * 91.44;
    } else if (convertfrom === "yard" && convertto === "kms") {
        result = userinput / 1094;
    } else if (convertfrom === "yard" && convertto === "miles") {
        result = userinput / 1760;
    } else if (convertfrom === "yard" && convertto === "foot") {
        result = userinput * 3;
    } else if (convertfrom === "yard" && convertto === "inch") {
        result = userinput * 36;
    // meters to x    
    } else if (convertfrom === "mtrs" && convertto === "cms") {
        result = userinput * 100;
    } else if (convertfrom === "mtrs" && convertto === "kms") {
        result = userinput / 1000;
    } else if (convertfrom === "mtrs" && convertto === "yard") {
        result = userinput * 1.094;
    } else if (convertfrom === "mtrs" && convertto === "miles") {
        result = userinput / 1609;
    } else if (convertfrom === "mtrs" && convertto === "foot") {
        result = userinput * 3.281;
    } else if (convertfrom === "mtrs" && convertto === "inch") {
        result = userinput * 39.37;
    // cm to x    
    } else if (convertfrom === "cms" && convertto === "mtrs") {
        result = userinput * 100;
    } else if (convertfrom === "cms" && convertto === "yard") {
        result = userinput / 91.44;
    } else if (convertfrom === "cms" && convertto === "kms") {
        result = userinput / 100000;
    } else if (convertfrom === "cms" && convertto === "miles") {
        result = userinput / 160900;
    } else if (convertfrom === "cms" && convertto === "foot") {
        result = userinput / 30.48;
    } else if (convertfrom === "cms" && convertto === "inch") {
        result = userinput / 2.54;
    } else {return;}
    
    const resultcontainer = document.getElementById("result-distance");
    resultcontainer.textContent = result;
    
});

// Money Conversions

document.getElementById("user-input-money").addEventListener("input", function () {
    const userinput = this.value;
    const convertfrom = document.getElementById("units-from-money").value;
    const convertto = document.getElementById("units-to-money").value;
    
    let result;
    
    // ksh to x
    if (convertfrom === "ksh" && convertto === "usd") {
        result = userinput / 129.0;
    } else if (convertfrom === "ksh" && convertto === "ush"){
        result = userinput * 29;
    } else if (convertfrom === "ksh" && convertto === "tsh"){
        result = userinput * 21;
    // usd to x    
    } else if (convertfrom === "usd" && convertto === "ksh"){
        result = userinput * 129;
    } else if (convertfrom === "usd" && convertto === "tsh"){
        result = userinput * 2710;
    } else if (convertfrom === "usd" && convertto === "ush"){
        result = userinput * 3722;
    // tsh to x    
    } else if (convertfrom === "tsh" && convertto === "usd"){
        result = userinput / 2710;
    } else if (convertfrom === "tsh" && convertto === "ksh"){
        result = userinput * 21;
    } else if (convertfrom === "tsh" && convertto === "ush"){
        result = userinput * 1.37;
    // ush to x    
    } else if (convertfrom === "ush" && convertto === "usd"){
        result = userinput / 3722;
    } else if (convertfrom === "ush" && convertto === "ksh"){
        result = userinput / 29;
    } else if (convertfrom === "ush" && convertto === "tsh"){
        result = userinput / 1.37;
    } else {return;}
    
    const resultcontainer = document.getElementById("result-money");
    resultcontainer.textContent = result;
    
});

// Mass Conversions

document.getElementById("user-input-mass").addEventListener("input", function () {
    const userinput = this.value;
    const convertfrom = document.getElementById("units-from-mass").value;
    const convertto = document.getElementById("units-to-mass").value;
    
    let result;
    
    if (convertfrom === "kgs" && convertto === "grms") {
        result = userinput * 1000;
    } else if (convertfrom === "kgs" && convertto === "pnds"){
        result = userinput * 2.205;
    } else if (convertfrom === "grms" && convertto === "kgs"){
        result = userinput / 1000;
    } else if (convertfrom === "grms" && convertto === "pnds"){
        result = userinput / 453.6;
    } else if (convertfrom === "pnds" && convertto === "kgs"){
        result = userinput / 2.205;
    } else if (convertfrom === "pnds" && convertto === "grms"){
        result = userinput * 453.6;
    } else {return;}
    
    const resultcontainer = document.getElementById("result-mass");
    resultcontainer.textContent = result;
    
});

// Tab Switch

function openUnitContainer(event, containerId) {
    //select and hide all the unit-containers
    const tabContainers = document.querySelectorAll(".units-container");
    tabContainers.forEach(container => {container.classList.remove("active-container")});
    
    //select and remove active classe from the tabs
    const tabs = document.querySelectorAll(".tab");
    tabs.forEach(tab => {tab.classList.remove("active-tab")});
    
    //apply tab style
    const selectedContainer = document.getElementById(containerId);
    selectedContainer.classList.add("active-container");
    event.currentTarget.classList.add("active-tab");
}