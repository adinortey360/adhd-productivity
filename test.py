#import task
import services.tasks as tasks
#import client
import services.clients as clients
#import random
import random

#create a new random client for testing
def create_random_client():
    #generate random phone number
    phone = str(random.randint(1, 100))
    #generate random email address @gmail.com
    email = phone+"@gmail.com"
    #generate random address
    address = "Address "+str(random.randint(1, 100))
    #generate random client name
    name = "Client "+str(random.randint(1, 100))
    


    #create a new client
    client = clients.Client()
    #create a new random client
    id = client.create_client(name, address, phone, email)
    #return id
    return id


#get all clients from database
def get_clients():
    #create a new client
    client = clients.Client()
    #get all clients from database
    return client.get_clients()


#run the create_random_client function
print(create_random_client())
#run the get_clients function
print(get_clients())