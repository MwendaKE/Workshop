// Load saved notes from localStorage or start empty
let notes = JSON.parse(localStorage.getItem("notes")) || [];

// Save a note
function saveNote() {
    let text = document.getElementById("note").value;

    // Ignore empty text
    if (!text.trim()) return;

    // Add to notes array
    notes.push(text);

    // Save updated notes into localStorage
    localStorage.setItem("notes", JSON.stringify(notes));

    // Clear textarea
    document.getElementById("note").value = "";

    // Refresh the UI
    displayNotes();
}

// Show notes in list
function displayNotes() {
    let list = document.getElementById("list");
    list.innerHTML = "";

    notes.forEach(function(n) {
        // Create <li> element for each note
        let li = document.createElement("li");
        li.innerText = n;
        list.appendChild(li);
    });
}

// Display notes at start
displayNotes();