from flask import Flask, render_template, request, redirect, url_for
from models import add_task, get_tasks

app = Flask(__name__)

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    add_task(title, description, priority)
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)