// Load saved expenses from localStorage OR start with an empty array
let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

// Function to add a new expense
function addExpense() {
    let item = document.getElementById("item").value;
    let amount = parseFloat(document.getElementById("amount").value);

    // If fields are empty, stop the function
    if (!item || isNaN(amount)) return;

    // Create a new expense object
    let expense = { item: item, amount: amount };

    // Add to the array
    expenses.push(expense);

    // Save updated list to localStorage
    localStorage.setItem("expenses", JSON.stringify(expenses));

    // Refresh the UI
    displayExpenses();
}

// Function to display all expenses
function displayExpenses() {
    let list = document.getElementById("list");
    let totalDisplay = document.getElementById("total");

    list.innerHTML = ""; // Clear list first

    let total = 0;

    // Loop through every expense in the array
    expenses.forEach(function(exp) {

        // Create list item and show item + amount
        let li = document.createElement("li");
        li.textContent = exp.item + " - $" + exp.amount;

        list.appendChild(li);

        // Add to total
        total += exp.amount;
    });

    // Show total expenses
    totalDisplay.innerText = total;
}

// First display when page opens
displayExpenses();