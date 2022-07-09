#tensorfow
import tensorflow as tf
#import task
import services.tasks as tasks

#create class for recommendations 
class Recommendations:
    #initialize the class
    def __init__(self):
        #return none
        return None

#create recommendations for task
    def recommendations():
        #get all tasks from database
        tasks = tasks.get_tasks()
        #jsonify tasks
        tasks = json.dumps(tasks)
        #return tasks
        return tasks
