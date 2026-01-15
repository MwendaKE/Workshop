// App.jsx
import Greeting from "./Greeting";  // Import our component

function App() {
  return (
    <div>
      <h1>Greeting Component Project</h1>

      {/* Using Greeting component with different names */}
      <Greeting name="Njagi" />
      <Greeting name="Alice" />
      <Greeting name="Brian" />
    </div>
  );
}

export default App;

