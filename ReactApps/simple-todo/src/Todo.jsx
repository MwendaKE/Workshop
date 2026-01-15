// Todo.jsx
// A very simple todo list where you type a task and add it to a list

import { useState } from "react";

function Todo() {
  // taskText stores the text typed in the input box
  // setTaskText changes the value
  const [taskText, setTaskText] = useState("");

  // tasks is an array that will store all added tasks
  const [tasks, setTasks] = useState([]);

  // Function to add a new task
  function addTask() {
    // Do not add empty tasks
    if (taskText.trim() === "") {
      return;
    }

    // Add the new task to the list
    setTasks([...tasks, taskText]);

    // Clear input box
    setTaskText("");
  }

  return (
    <div>

      {/* Input: type task here */}
      <input
        type="text"
        placeholder="Enter a task"
        value={taskText}              // show current text
        onChange={(e) => setTaskText(e.target.value)} // update text
      />

      {/* Button to add task */}
      <button onClick={addTask}>Add Task</button>

      <h2>Tasks:</h2>

      {/* List of tasks */}
      <ul>
        {tasks.map((t, index) => (
          <li key={index}>{t}</li>    // show each task
        ))}
      </ul>
    </div>
  );
}

export default Todo;


// 1. Input Box
// Whatever you type goes into taskText using onChange.

// 2. Add Button
// When clicked, it runs addTask().
// The task is pushed into the list tasks.

// 3. Task List
// We loop (map) through all tasks and show them one by one.
