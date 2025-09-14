from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(150), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.task}>'
        
        
with app.app_context():
    db.create_all()
    
    
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/tasks', methods=['GET'])  
def get_tasks():
    tasks = Task.query.all()
    tasks_data = [{'tid': task.tid, 'task': task.task, 'completed': task.completed} for task in tasks]
    return jsonify(tasks_data)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.json['task']
    if task:
        new_task = Task(task=task)
        db.session.add(new_task)
        db.session.commit()
        
        return jsonify({'tid': new_task.tid, 'task': new_task.task}), 201
    
    return jsonify({'error': 'Invalid input'}), 400
    
    
@app.route('/tasks/<int:taskid>/complete', methods=['PUT'])
def compete_task(taskid):
    task = Task.query.get(taskid)
    if task:
        if task.completed == True:
            task.completed = False
            
        else:
            task.completed = True
            
        db.session.commit()
        
        return jsonify({'message': f"Task '{task.tid}' completed successfully"})
    
    return jsonify({'error': 'Task not found'})


@app.route('/update/<int:taskid>', methods=['PUT'])
def update_task(taskid):
    task = Task.query.get(taskid)
    data = request.get_json()
    
    if "new_task_name" in data:
        task.task = data["new_task_name"]
        
    try:
        db.session.commit()
        return jsonify({'message': f"Task '{task.tid}' updated successfully"})
       
    except Exception as error:
        db.commit.rollback()
        return jsonify({'error': str(error)})


@app.route('/delete/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
    task = Task.query.get(taskid)
    if task:
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({'message': 'Task deleted'}), 200
    
    return jsonify({'error': 'Task not found'}), 404
    
    
if __name__ == "__main__":
    app.run(debug=True)