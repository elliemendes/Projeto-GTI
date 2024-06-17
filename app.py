from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = [
    {'title': 'Task 1', 'description': 'Description 1', 'priority': 'High'},
    {'title': 'Task 2', 'description': 'Description 2', 'priority': 'Low'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority')
    tasks.append({'title': title, 'description': description, 'priority': priority})
    return jsonify({'message': 'Task added successfully!'}), 201

if __name__ == '_main_':
    app.run(debug=True)