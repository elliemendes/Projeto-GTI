tasks = []

def add_task(title, description, priority):
    tasks = { 'title': title,
        'description': description,
        'priority': priority,
        'status': 'pending'}
    tasks.append(tasks)
    

def get_tasks():
    return tasks