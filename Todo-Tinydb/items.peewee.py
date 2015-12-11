from models import *

def get_items(status = -1):
    if (status >= 0):
        query = Todo.select().where(Todo.status == status).order_by(Todo.task.asc())
    else:
        query = Todo.select().order_by(Todo.task.asc())
    result = []
    for todo in query:
        result.append(
            {
                'id':todo.id,
                'task':todo.task,
                'status':todo.status
            })
    return result
    
def new_item(task,status):
    todo = Todo.create(task = task, status = status)
    
def get_item(id):
    todo = Todo.get(id=id)
    return {'id':id, 'task':todo.task, 'status':todo.status}

def save_item(item):
    todo = Todo.get(id=item['id'])
    todo.task = item['task']
    todo.status = item['status']
    todo.save()

def discard_item(id):
    todo = Todo.get(id=id)
    todo.delete_instance()

if __name__ == "__main__":
    new_item("really new stuff",0)
    items = get_items(-1)
    for item in items:
        print (item)
    print ('-----')
    item = get_item(10)
    item['task'] = "new version:" + item['task']
    save_item(item)
    print(item)    
     
