tasks = []

def add_task(title, description, priority):
    tasks.append ({ 'title': title,
        'description': description,
        'priority': priority,
        'status': 'pending'
    })

def get_tasks():
    return tasks