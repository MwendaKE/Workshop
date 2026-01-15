// Greeting.jsx
// This component shows a greeting message using props

function Greeting(props) {
  // props.name is the name passed from App.jsx

  return (
    <h2>Hello, {props.name}!</h2>
  );
}

export default Greeting;

