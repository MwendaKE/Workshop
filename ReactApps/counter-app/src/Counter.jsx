// Counter.jsx
// This component displays a number and buttons to increase or decrease it

import { useState } from "react";

// useState helps the component remember values (like the counter number)

function Counter() {
  // Create a state variable "number" with initial value 0
  // setNumber is a function that changes "number"
  const [number, setNumber] = useState(0);

  // Function to increase the counter
  function increase() {
    setNumber(number + 1);
  }

  // Function to decrease the counter
  function decrease() {
    setNumber(number - 1);
  }

  return (
    <div>
      <h2>Counter: {number}</h2>

      {/* Button to increase */}
      <button onClick={increase}>Increase</button>

      {/* Button to decrease */}
      <button onClick={decrease}>Decrease</button>
    </div>
  );
}

export default Counter;

// useState(0) sets the starting number to 0.
// number holds the current value.
// setNumber() updates it.
// Clicking buttons calls the functions and changes the number.
