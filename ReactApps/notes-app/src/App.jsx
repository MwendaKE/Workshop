import { useState, useEffect } from "react";
import "./App.css";

function App() {
  // -------------------------
  // STATE VARIABLES
  // -------------------------
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [category, setCategory] = useState("");
  const [search, setSearch] = useState("");
  const [editingId, setEditingId] = useState(null); // for edit mode

  // -------------------------
  // LOAD FROM localStorage ONCE
  // -------------------------
  useEffect(() => {
    const saved = localStorage.getItem("notes");
    if (saved) {
      setNotes(JSON.parse(saved));
    }
  }, []);

  // -------------------------
  // SAVE TO localStorage WHEN NOTES CHANGE
  // -------------------------
  useEffect(() => {
    localStorage.setItem("notes", JSON.stringify(notes));
  }, [notes]);

  // -------------------------
  // ADD OR UPDATE NOTE
  // -------------------------
  const handleSave = () => {
    if (title.trim() === "" || body.trim() === "") {
      alert("Title and body are required");
      return;
    }

    // UPDATE MODE
    if (editingId !== null) {
      const updatedNotes = notes.map((n) =>
        n.id === editingId
          ? { ...n, title, body, category }
          : n
      );

      setNotes(updatedNotes);
      setEditingId(null);
    } else {
      // ADD MODE
      const newNote = {
        id: Date.now(),
        title,
        body,
        category,
      };

      setNotes([newNote, ...notes]);
    }

    // Clear inputs
    setTitle("");
    setBody("");
    setCategory("");
  };

  // -------------------------
  // DELETE NOTE
  // -------------------------
  const deleteNote = (id) => {
    setNotes(notes.filter((n) => n.id !== id));
  };

  // -------------------------
  // EDIT NOTE (LOAD DATA INTO INPUTS)
  // -------------------------
  const editNote = (note) => {
    setTitle(note.title);
    setBody(note.body);
    setCategory(note.category);
    setEditingId(note.id);
  };

  // -------------------------
  // FILTERED SEARCH RESULTS
  // -------------------------
  const filteredNotes = notes.filter(
    (n) =>
      n.title.toLowerCase().includes(search.toLowerCase()) ||
      n.body.toLowerCase().includes(search.toLowerCase()) ||
      n.category.toLowerCase().includes(search.toLowerCase())
  );

  // -------------------------
  // UI
  // -------------------------
  return (
    <div className="app-container">
      <div className="main-box">

        {/* TITLE */}
        <h1>Notes App</h1>

        {/* SEARCH BAR */}
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search notes..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        {/* INPUTS */}
        <input
          type="text"
          placeholder="Note title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <textarea
          rows="4"
          placeholder="Note details..."
          value={body}
          onChange={(e) => setBody(e.target.value)}
        ></textarea>

        <input
          type="text"
          placeholder="Category (tag)"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />

        {/* SAVE BUTTON */}
        <button onClick={handleSave}>
          {editingId ? "Update Note" : "Add Note"}
        </button>

        {/* NOTES LIST */}
        <div className="notes-list">
          {filteredNotes.length === 0 ? (
            <p className="empty-message">No notes found</p>
          ) : (
            filteredNotes.map((note) => (
              <div className="note-item" key={note.id}>
                <div className="note-header">
                  <span className="note-title">{note.title}</span>

                  <div>
                    <button
                      className="small edit"
                      onClick={() => editNote(note)}
                    >
                      Edit
                    </button>

                    <button
                      className="small delete"
                      onClick={() => deleteNote(note.id)}
                    >
                      Delete
                    </button>
                  </div>
                </div>

                {/* CATEGORY TAG */}
                {note.category && (
                  <span className="tag">{note.category}</span>
                )}

                <p>{note.body}</p>
              </div>
            ))
          )}
        </div>

      </div>
    </div>
  );
}

export default App;

