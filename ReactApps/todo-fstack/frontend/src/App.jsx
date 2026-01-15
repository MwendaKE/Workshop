import { useState, useEffect } from "react";

// -------------------------------
// MAIN APP COMPONENT
// -------------------------------
function App() {
  const [todos, setTodos] = useState([]);     // List of todos
  const [newTodo, setNewTodo] = useState(""); // New todo input
  const [editingId, setEditingId] = useState(null); // Track the item being edited
  const [editingText, setEditingText] = useState(""); // Temp edited text

  // -------------------------------
  // FETCH TODOS FROM BACKEND
  // -------------------------------
  const fetchTodos = () => {
    fetch("http://127.0.0.1:5000/todos")
      .then((res) => res.json())
      .then((data) => setTodos(data));
  };

  // Call fetchTodos once when page loads
  useEffect(() => {
    fetchTodos();
  }, []);

  // -------------------------------
  // ADD TODO
  // -------------------------------
  const addTodo = () => {
    if (newTodo.trim() === "") return;

    fetch("http://127.0.0.1:5000/todos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: newTodo }),
    }).then(() => {
      setNewTodo("");
      fetchTodos();
    });
  };

  // -------------------------------
  // TOGGLE COMPLETED
  // -------------------------------
  const toggleCompleted = (id, currentValue) => {
    fetch(`http://127.0.0.1:5000/todos/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !currentValue }),
    }).then(() => fetchTodos());
  };

  // -------------------------------
  // START EDITING
  // -------------------------------
  const startEditing = (id, currentTitle) => {
    setEditingId(id);
    setEditingText(currentTitle);
  };

  // -------------------------------
  // SAVE EDITED TODO
  // -------------------------------
  const saveEdit = (id) => {
    if (editingText.trim() === "") return;

    fetch(`http://127.0.0.1:5000/todos/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        // reuse the backend PUT (it supports both completed + title)
        completed: false,  
        title: editingText  
      }),
    }).then(() => {
      setEditingId(null);   // stop editing mode
      setEditingText("");   // clear input
      fetchTodos();         // refresh list
    });
  };

  // -------------------------------
  // DELETE TODO
  // -------------------------------
  const deleteTodo = (id) => {
    fetch(`http://127.0.0.1:5000/todos/${id}`, {
      method: "DELETE",
    }).then(() => fetchTodos());
  };

  return (
    <div style={styles.container}>
      <h2>Todo App (React + Flask)</h2>

      {/* Input for new todo */}
      <div style={styles.row}>
        <input
          style={styles.input}
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Enter a new task"
        />

        <button style={styles.button} onClick={addTodo}>
          Add
        </button>
      </div>

      <ul style={styles.list}>
        {todos.map((todo) => (
          <li key={todo.id} style={styles.listItem}>
            {/* Complete checkbox */}
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleCompleted(todo.id, todo.completed)}
            />

            {/* Editing mode */}
            {editingId === todo.id ? (
              <>
                <input
                  style={styles.editInput}
                  value={editingText}
                  onChange={(e) => setEditingText(e.target.value)}
                />

                <button style={styles.smallButton} onClick={() => saveEdit(todo.id)}>
                  Save
                </button>
              </>
            ) : (
              <>
                {/* Normal text */}
                <span style={todo.completed ? styles.completedText : {}}>
                  {todo.title}
                </span>

                <button
                  style={styles.smallButton}
                  onClick={() => startEditing(todo.id, todo.title)}
                >
                  Edit
                </button>
              </>
            )}

            {/* Delete button */}
            <button
              style={{ ...styles.smallButton, backgroundColor: "red" }}
              onClick={() => deleteTodo(todo.id)}
            >
              X
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

// -------------------------------
// SIMPLE INLINE STYLES
// -------------------------------
const styles = {
  container: {
    maxWidth: "500px",
    margin: "30px auto",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "8px",
    fontFamily: "Arial",
  },
  row: {
    display: "flex",
    gap: "10px",
  },
  input: {
    flex: 1,
    padding: "10px",
  },
  button: {
    padding: "10px",
  },
  list: {
    marginTop: "20px",
    listStyle: "none",
    padding: 0,
  },
  listItem: {
    display: "flex",
    gap: "10px",
    alignItems: "center",
    marginBottom: "10px",
  },
  smallButton: {
    padding: "5px 10px",
  },
  editInput: {
    padding: "5px",
  },
  completedText: {
    textDecoration: "line-through",
    color: "gray",
  },
};

export default App;

