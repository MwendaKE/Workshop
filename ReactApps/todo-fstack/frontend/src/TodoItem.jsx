// TodoItem.jsx
// Component for a single Todo item
import axios from "axios";

function TodoItem({ todo, reload }) {

  const API_URL = "http://127.0.0.1:5000";

  // Toggle completed
  function toggleCompleted() {
    axios.put(API_URL + "/todos/" + todo.id, {
      completed: !todo.completed
    }).then(() => reload());
  }

  // Delete todo
  function deleteTodo() {
    axios.delete(API_URL + "/todos/" + todo.id)
      .then(() => reload());
  }

  return (
    <div
      style={{
        padding: "10px",
        marginBottom: "10px",
        background: "#f1f1f1",
        borderRadius: "5px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}
    >
      <span
        style={{
          textDecoration: todo.completed ? "line-through" : "none",
          cursor: "pointer"
        }}
        onClick={toggleCompleted}
      >
        {todo.title}
      </span>

      <button
        onClick={deleteTodo}
        style={{
          background: "red",
          color: "white",
          border: "none",
          padding: "5px 10px",
          borderRadius: "5px"
        }}
      >
        Delete
      </button>
    </div>
  );
}

export default TodoItem;

