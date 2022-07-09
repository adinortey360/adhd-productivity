#import task
import services.tasks as tasks
#import client
import services.clients as clients

#create a new random client for testing
def create_random_client():
    #create a new client
    client = clients.Client()
    #create a new random client
    client.create_client('random_client', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', '02020202','test@test.com');

#run the create_random_client function
create_random_client()