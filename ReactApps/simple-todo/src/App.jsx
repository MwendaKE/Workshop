// App.jsx
// This file loads our Todo component and displays the app title

import Todo from "./Todo"; // import our to-do component

function App() {
  return (
    <div>
      <h1>Simple Todo App</h1>

      {/* Show the Todo component */}
      <Todo />
    </div>
  );
}

export default App;

