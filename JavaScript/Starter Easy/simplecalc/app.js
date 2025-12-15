// Function that performs calculation
function calculate(operation) {

    // Read the two numbers from the inputs
    let n1 = parseFloat(document.getElementById("num1").value);
    let n2 = parseFloat(document.getElementById("num2").value);

    let answer = 0;

    // Perform the correct operation based on the button clicked
    if (operation === "+") {
        answer = n1 + n2;
    } else if (operation === "-") {
        answer = n1 - n2;
    } else if (operation === "*") {
        answer = n1 * n2;
    } else if (operation === "/") {
        // Prevent division by zero
        if (n2 === 0) {
            answer = "Cannot divide by zero";
        } else {
            answer = n1 / n2;
        }
    }

    // Show result
    document.getElementById("result").innerText = answer;
}