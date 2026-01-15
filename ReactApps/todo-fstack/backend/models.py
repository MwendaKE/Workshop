# nano models.py

# models.py
# This file creates the SQLite database and Todo model using SQLAlchemy.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        # Convert model to Python dictionary (JSON-friendly)
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

