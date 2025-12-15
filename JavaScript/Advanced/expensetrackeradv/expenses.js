// Elements
const expenseForm = document.getElementById("expenseForm");
const descInput = document.getElementById("desc");
const amountInput = document.getElementById("amount");
const categoryInput = document.getElementById("category");
const dateInput = document.getElementById("date");
const expensesBody = document.getElementById("expensesBody");

let expenses = JSON.parse(localStorage.getItem("expenses") || "[]");
let editIndex = null;

// ----------------------------
// RENDER EXPENSES TABLE
// ----------------------------
function renderExpenses() {
    expensesBody.innerHTML = "";

    expenses.forEach((expense, index) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${expense.desc}</td>
            <td>${expense.amount}</td>
            <td>${expense.category}</td>
            <td>${expense.date}</td>
            <td>
                <button class="edit" onclick="editExpense(${index})">Edit</button>
                <button class="delete" onclick="deleteExpense(${index})">Delete</button>
            </td>
        `;

        expensesBody.appendChild(row);
    });

    updateChart();
}

// ----------------------------
// ADD OR UPDATE EXPENSE
// ----------------------------
expenseForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const expense = {
        desc: descInput.value,
        amount: parseFloat(amountInput.value),
        category: categoryInput.value,
        date: dateInput.value
    };

    if(editIndex !== null){
        expenses[editIndex] = expense;
        editIndex = null;
    } else {
        expenses.push(expense);
    }

    localStorage.setItem("expenses", JSON.stringify(expenses));
    expenseForm.reset();
    renderExpenses();
});

// ----------------------------
// EDIT EXPENSE
// ----------------------------
function editExpense(index){
    const expense = expenses[index];
    descInput.value = expense.desc;
    amountInput.value = expense.amount;
    categoryInput.value = expense.category;
    dateInput.value = expense.date;
    editIndex = index;
}

// ----------------------------
// DELETE EXPENSE
// ----------------------------
function deleteExpense(index){
    if(confirm("Are you sure you want to delete this expense?")){
        expenses.splice(index,1);
        localStorage.setItem("expenses", JSON.stringify(expenses));
        renderExpenses();
    }
}

// ----------------------------
// CHART
// ----------------------------
const ctx = document.getElementById("expenseChart").getContext("2d");
let chart;

function updateChart(){
    const categories = {};
    expenses.forEach(exp => {
        if(categories[exp.category]){
            categories[exp.category] += exp.amount;
        } else {
            categories[exp.category] = exp.amount;
        }
    });

    const labels = Object.keys(categories);
    const data = Object.values(categories);

    if(chart) chart.destroy();

    chart = new Chart(ctx,{
        type:'bar',
        data:{
            labels:labels,
            datasets:[{
                label:'Expenses by Category',
                data:data,
                backgroundColor:['#0288d1','#fbc02d','#d32f2f','#388e3c','#7b1fa2']
            }]
        },
        options:{
            responsive:true,
            plugins:{
                legend:{ display:false }
            }
        }
    });
}

// ----------------------------
// INITIAL LOAD
// ----------------------------
renderExpenses();