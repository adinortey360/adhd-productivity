#import database service
from services.database import Database

#create controller for client
class Client:
    #initialize the class
    def __init__(self):
        #return none
        return None
    
    #create new client in database with parameters client_name, client_address, client_phone, client_email, return the id of the new client
    def create_client(self, client_name, client_address, client_phone, client_email):
        #create a database object
        db = Database()
        #insert new client in database
        db.insert('client', "'"+client_name+"', '"+client_address+"', '"+client_phone+"', '"+client_email+"'")
        #return the id of the new client
        return db.search('client', client_name)[0][0]

    #get all clients from database, return a list of clients
    def get_clients(self):
        #create a database object
        db = Database()
        #return all clients from database
        return db.view('client')

    #get client by id from database, return a list of client
    def get_client_by_id(self, client_id):
        #create a database object
        db = Database()
        #return client by id from database
        return db.search('client', client_id)

    #get client by name from database, return a list of client
    def get_client_by_name(self, client_name):
        #create a database object
        db = Database()
        #return client by name from database
        return db.search('client', client_name)

    #delete client by id from database, return a list of client
    def delete_client_by_id(self, client_id):
        #create a database object
        db = Database()
        #delete client by id from database
        db.delete('client', client_id)
        #return client by id from database
        return db.search('client', client_id)

    #update client by id from database, return client
    def update_client_by_id(self, client_id, client_name, client_address, client_phone, client_email):
        #create a database object
        db = Database()
        #update client by id from database
        db.update('client', client_id, client_name, client_address, client_phone, client_email)
        #return client by id from database
        return db.search('client', client_id)

    