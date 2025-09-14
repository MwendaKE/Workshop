document.addEventListener("DOMContentLoaded", (event) => {
    fetchAndDisplayTasks();
});

function fetchAndDisplayTasks() {
    fetch('/tasks')
        .then(response =>  {
            if (!response.ok) {
                throw new Error("Failed to fetch tasks: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const tBody = document.getElementById("tasks-container");
    
            // Clear all existing rows to prevent duplicate rows
            tBody.innerHTML = ""; 
    
            data.forEach((task, index) => {
                // Create <tr></tr> table element
                const tRow = document.createElement("tr");
        
                // Create <td></td> elements and add data
                const tIndex = document.createElement("td");
                tIndex.textContent = index + 1;
                
                //----------
                const tText = document.createElement("td");
                
                const editIcon = document.createElement("span");
                editIcon.classList.add("fa","fa-edit");
                editIcon.style.color = "#ccc";
                editIcon.addEventListener('click', () => updateTask(task));
                
                tText.textContent = task.task;
                tText.appendChild(editIcon);
                
                if (task.completed) {
                    tText.classList.add("completed");
                }
                
                // Action Buttons
                const tAction = document.createElement("td");
                const tActionsContainer = document.createElement("div");
                tActionsContainer.classList.add("actions");
                
                //---------
                const comBtn = document.createElement("i");
                comBtn.classList.add("fa","fa-check");
                comBtn.addEventListener('click', () => completeTask(task.tid));
                
                tActionsContainer.appendChild(comBtn);
                
                //--------
                const delBtn = document.createElement("i");
                delBtn.classList.add("fa","fa-trash","deletebtn");
                delBtn.addEventListener('click', () => deleteTask(task.tid));
                
                tActionsContainer.appendChild(delBtn);
                
                //---------
                tAction.appendChild(tActionsContainer);
        
                // Put data to the <tr></tr> element
                tRow.appendChild(tIndex);
                tRow.appendChild(tText);
                tRow.appendChild(tAction);
        
                // Put the <tr></tr> element to <tbody></body> element
                tBody.appendChild(tRow);
            });
        })
        .catch (error => {
            alert(error);
        });    
}

function addNewTask() {
    const taskInput = document.getElementById("todo-text");
    const taskText = taskInput.value.trim();
    
    if (taskText === "") return;
    
    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
          },
        body: JSON.stringify({
            'task': taskText
        })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to add new task: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            taskInput.value = "";
            fetchAndDisplayTasks();
        })
        .catch(error => {
            alert(error);
        });
}

function completeTask(taskid) {
    fetch(`/tasks/${taskid}/complete`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        } 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to complete task: " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        fetchAndDisplayTasks();
    })
    .catch(error => {
        alert(error);
    });
}

function updateTask(task) {
    document.getElementById('task-edit-modal').style.display = 'flex';
    document.getElementById('modal-input').value = task.task;
    
    document.getElementById("submit-modal").onclick = function() {
        const taskNewText = document.getElementById('modal-input').value.trim();
        
        if (taskNewText) {
            document.getElementById('task-edit-modal').style.display = 'none';
            
            fetch(`/update/${task.tid}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                 },
                 body: JSON.stringify({'new_task_name': taskNewText})
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to update task: " + response.statusText);
                }
                return response.json();
             })
            .then(data => {
                fetchAndDisplayTasks();
            })
            .catch(error => {
                alert(error);
            });
        }
    }
}

function deleteTask(taskid) {
    fetch(`/delete/${taskid}`, {method: 'DELETE'})
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to delete task: " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        fetchAndDisplayTasks();
    })
    .catch(error => {
        alert(error);
    });
}

function closeTaskModal() {
    document.getElementById('task-edit-modal').style.display = 'none';
}


