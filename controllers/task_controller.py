#get database and create a class for it
from services.database import Database

#create a class for task controller
class TaskController:
    #initialize the class
    def __init__(self):
        #return none
        return None
    
    #create new task in database with parameters task_name, client, due_date and task_description, return the id of the new task    
    def create_task(self, task_name, client, due_date, task_description):
        #create a new database
        db = Database()
        #insert new task into database
        db.insert('task', "'"+task_name+"', '"+client+"', '"+due_date+"', '"+task_description+"'")
        #get the id of the new task
        return db.search('task', task_name)[0][0]

    #get all tasks from database, return a list of tasks
    def get_all_tasks(self):
        #create a new database
        db = Database()
        #get all tasks from database
        return db.view('task')

    #get task by id from database, return a list of tasks
    def get_task_by_id(self, id):
        #create a new database
        db = Database()
        #get task by id from database
        return db.search('task', id)

    