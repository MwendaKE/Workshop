// FormExample.jsx
// A simple form that takes name and email, and shows the result after submitting

import { useState } from "react";

function FormExample() {
  // Store each form field
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  // Store submitted data
  const [submittedData, setSubmittedData] = useState(null);

  // Handle form submission
  function handleSubmit(e) {
    e.preventDefault(); // stop page refresh

    // Save the name + email
    setSubmittedData({
      name: name,
      email: email
    });

    // Clear form fields
    setName("");
    setEmail("");
  }

  return (
    <div>
      {/* Form starts here */}
      <form onSubmit={handleSubmit}>
        {/* Name field */}
        <div>
          <label>Your Name: </label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)} // updates name
            placeholder="Enter your name"
          />
        </div>

        {/* Email field */}
        <div>
          <label>Your Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)} // updates email
            placeholder="Enter your email"
          />
        </div>

        {/* Submit button */}
        <button type="submit">Submit</button>
      </form>

      {/* Show submitted data */}
      {submittedData && (
        <div style={{ marginTop: "20px" }}>
          <h2>Submitted Data:</h2>
          <p><strong>Name:</strong> {submittedData.name}</p>
          <p><strong>Email:</strong> {submittedData.email}</p>
        </div>
      )}
    </div>
  );
}

export default FormExample;


// 1. Controlled Inputs

// Every input uses:
// value={name}
// onChange={(e) => setName(e.target.value)}

// This means React controls the input.

// 2. Form Submission

// onSubmit runs handleSubmit()
// We stop page refresh and save the data.

// 3. Showing Data

// We store it in submittedData and display it.

