let userInput = document.getElementById("text-input");
let userOutput = document.getElementById("text-output");
const equalButton = document.getElementById("equal");
let userInputText = [];

const operators = Array.from(document.querySelectorAll(".operator")).map(operator => operator.innerText);

document.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", (e) => {
        const btnClicked = e.target.innerText;

        if (btnClicked === "=") {
            return; // Ignore this button. Its functionality is defined separately
        } else if (btnClicked === "AC") {
            userInput.value = "0";
            userOutput.innerText = "";
            userInputText = [];
        } else if (btnClicked === "DEL") {
            userInputText.pop();
            if (userInputText.length === 0) {
                userInput.value = "0";
            } else {
                userInput.value = userInputText.join("");
            }
        } else {
            // Prevent adding operators at the start or multiple operators in a row
            if (operators.includes(btnClicked) && (userInputText.length === 0 || operators.includes(userInputText[userInputText.length - 1]))) {
                return;
            }
            // Make sure input does not start with 0 
            if (userInputText.length === 1 && userInputText[0] === '0') {
                userInputText = [btnClicked];
            } else {
                userInputText.push(btnClicked);
            }
            userInput.value = userInputText.join("");
        }
    });
});

// Set event listener for equal button
equalButton.addEventListener("click", () => {
    let expression = userInput.value; // Get the expression

    // Check if the expression contains any operator
    const expressionContainsOperator = operators.some(operator => expression.includes(operator));

    if (expressionContainsOperator) {
        try {
            let result = eval(expression); // WARNING: Be careful with eval
            userOutput.innerText = result;
        } catch (error) {
            userOutput.innerText = "Error";
        }
    }
});