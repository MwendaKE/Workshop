// Load tasks when page opens
window.onload = function() {
    loadTasks();
};

function addTask() {
    let input = document.getElementById("taskInput");
    let task = input.value.trim();

    if (task === "") {
        alert("Enter a task");
        return;
    }

    let tasks = getTasks();
    tasks.push({ text: task, done: false });
    saveTasks(tasks);

    input.value = "";
    loadTasks();
}

function toggleTask(index) {
    let tasks = getTasks();
    tasks[index].done = !tasks[index].done;
    saveTasks(tasks);
    loadTasks();
}

function deleteTask(index) {
    let tasks = getTasks();
    tasks.splice(index, 1);
    saveTasks(tasks);
    loadTasks();
}

// Helpers for LocalStorage
function getTasks() {
    let data = localStorage.getItem("tasks");
    return data ? JSON.parse(data) : [];
}

function saveTasks(tasks) {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Display tasks
function loadTasks() {
    let tasks = getTasks();
    let list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach(function(task, index) {
        let li = document.createElement("li");

        li.innerHTML = `
            <span onclick="toggleTask(${index})" class="${task.done ? 'done' : ''}">
                ${task.text}
            </span>
            <button onclick="deleteTask(${index})">X</button>
        `;

        list.appendChild(li);
    });
}