from flask import Flask, request, send_from_directory, render_template
from database.database import init_db, save_application, get_all_applications
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    save_application(data)
    return {'status': 'success'}

@app.route('/admin')
def admin_page():
    applications = get_all_applications()
    
    html = f"""
    <html>
    <head>
        <title>Admin - Applications</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            .app {{ border: 1px solid #ccc; margin: 10px; padding: 15px; background: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>Job Applications</h1>
        <p>Total: {len(applications)} applications</p>
    """
    
    for app in applications:
        html += f"""
        <div class='app'>
            <h3>{app['full_name']}</h3>
            <p><strong>Phone:</strong> {app['phone']}</p>
            <p><strong>Email:</strong> {app['email']}</p>
            <p><strong>Position:</strong> {app['position']}</p>
            <p><strong>Experience:</strong> {app['experience']}</p>
            <p><strong>Date:</strong> {app['submitted_date'][:10] if app['submitted_date'] else 'N/A'}</p>
        </div>
        """
    
    if not applications:
        html += "<p>No applications submitted yet.</p>"
    
    html += "</body></html>"
    return html

if __name__ == '__main__':
    init_db()
    print("Server running: http://localhost:5000")
    print("Admin page: http://localhost:5000/admin")
    app.run(host='0.0.0.0', port=5000)