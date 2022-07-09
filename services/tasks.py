#get database and create a class for it
from services.database import Database

#create a class for task controller
class Task:
    #initialize the class and create sqlite table for task if it doesn't exist
    def __init__(self):
        return None
        
    
    #create new task in database with parameters task_name, client_id, status, due_date and task_description, return the id of the new task    
    def create_task(self, task_name, client_id, status, due_date, task_description):
        #create a database object
        db = Database()
        #insert new task in database
        db.insert('task', "'"+task_name+"', '"+client_id+"', '"+status+"', '"+due_date+"', '"+task_description+"'")
        #return the id of the new task
        return db.search('task', task_name)[0][0]

    #get all tasks from database, return a list of tasks
    def get_tasks(self):
        #create a database object
        db = Database()
        #return all tasks from database
        return db.view('task')

    #get task by id from database, return a list of task
    def get_task_by_id(self, task_id):
        #create a database object
        db = Database()
        #return task by id from database
        return db.search('task', task_id)

    #get task by name from database, return a list of task
    def get_task_by_name(self, task_name):
        #create a database object
        db = Database()
        #return task by name from database
        return db.search('task', task_name)

    #delete task by id from database, return a list of task
    def delete_task_by_id(self, task_id):
        #create a database object
        db = Database()
        #delete task by id from database
        db.delete('task', task_id)
        #return task by id from database
        return db.search('task', task_id)

    #update task by id from database, return task
    def update_task_by_id(self, task_id, task_name, client_id, status, due_date, task_description):
        #create a database object
        db = Database()
        #update task by id from database
        db.update('task', task_id, task_name, client_id, status, due_date, task_description)
        #return task by id from database
        return db.search('task', task_id)
        