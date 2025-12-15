// We store all expenses here
let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

// Display saved expenses at start
showExpenses();

/* -----------------------------------------------------
   Add a new expense
----------------------------------------------------- */
function addExpense() {
    let title = document.getElementById("title").value;
    let amount = document.getElementById("amount").value;
    let category = document.getElementById("category").value;

    // Simple validation
    if (title === "" || amount === "") {
        alert("Please enter all fields.");
        return;
    }

    // Create expense object
    let expense = {
        title: title,
        amount: Number(amount),
        category: category
    };

    // Add to array
    expenses.push(expense);

    // Save to localStorage
    localStorage.setItem("expenses", JSON.stringify(expenses));

    // Refresh UI
    showExpenses();
}

/* -----------------------------------------------------
   Display all expenses in page
----------------------------------------------------- */
function showExpenses() {
    let list = document.getElementById("list");
    list.innerHTML = ""; // clear

    expenses.forEach(function(e) {
        let div = document.createElement("div");
        div.className = "expense";

        div.innerHTML = `<b>${e.title}</b> - $${e.amount} (${e.category})`;

        list.appendChild(div);
    });
}