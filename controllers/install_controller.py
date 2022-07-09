#import database service
from services.database import Database

#create controller for install
class Install:
    #Initialize the class
    def __init__(self):
        #return none
        return None

    #create client table in database with parameters client_name, client_address, client_phone, client_email, return the id of the new client
