# app.py
# Flask backend for Todo CRUD API using SQLAlchemy

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Todo

app = Flask(__name__)
CORS(app)

# ----------------------------------------
# DATABASE CONFIG
# ----------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ----------------------------------------
# CREATE TABLES (Flask 3 compatible)
# ----------------------------------------
# Flask 3 removed before_first_request, so we use this method
with app.app_context():
    db.create_all()


# ----------------------------------------
# GET ALL TODOS
# ----------------------------------------
@app.get("/todos")
def get_todos():
    todos = Todo.query.all()
    return jsonify([t.to_dict() for t in todos])


# ----------------------------------------
# ADD TODO
# ----------------------------------------
@app.post("/todos")
def add_todo():
    data = request.json
    title = data.get("title", "").strip()

    if title == "":
        return jsonify({"error": "Title is required"}), 400

    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"message": "Todo added"}), 201


# ----------------------------------------
# UPDATE TODO (edit title or toggle completed)
# ----------------------------------------
@app.put("/todos/<int:todo_id>")
def update_todo(todo_id):
    data = request.json

    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    # Update title if provided
    if "title" in data:
        new_title = data["title"].strip()
        if new_title == "":
            return jsonify({"error": "Title cannot be empty"}), 400
        todo.title = new_title

    # Update completed status if provided
    if "completed" in data:
        todo.completed = data["completed"]

    db.session.commit()

    return jsonify({"message": "Todo updated"})


# ----------------------------------------
# DELETE TODO
# ----------------------------------------
@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Todo deleted"})


# ----------------------------------------
# RUN APP
# ----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

