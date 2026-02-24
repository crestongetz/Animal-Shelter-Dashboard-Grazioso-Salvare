# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # TODO: DELETE hardcoded values in production
        # USER = 'aacuser' 
        # PASS = 'password'
        
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        #self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=aac' % (USER, PASS))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data) -> bool:
        if data is None:
            print('Nothing to save, because data parameter is empty')
            return False
        try:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
            
        except Exception as e: #if data is not empty but not a dict
            print(f'An error occured: {e}')
            return False


    # Create method to implement the R in CRUD.
    def read(self, data) -> list:
        if data is None:
            print('Nothing to save, because data parameter is empty')
            return list()
        try:
            #reads data from database and adds it to a list
            results = self.database.animals.find(data)
            list_of_results = [doc for doc in results] #change to subset of data for large datasets
                
            return list_of_results
            
        except Exception as e: #if data is not empty but not a dict
            print(f'An error occured: {e}')
            return list()
    
    
    # method to implement U in CRUD. returns number of updated objects
    def update(self, query, updateData, updateAll=False) -> int:
        if updateData is None:
            print('Nothing to save, because data parameter is empty')
            return 0
        
        if query is None:
            print('Nothing to update, query data parameter is empty')
            return 0
        
        if not isinstance(updateAll, bool):
            raise ValueError("updateAll must be a boolean")

        try:
            if updateAll: # updateAll is used to toggle between update_one and update_many
                result = self.database.animals.update_many(query, updateData)
            else:
                result = self.database.animals.update_one(query, updateData)
                
            return result.modified_count
                
        except Exception as e: 
            print(f'An error occured: {e}')
            return 0 # no updates where made

            
    # Method to implement D in CRUD. returns number of deleted objects
    def delete(self, deleteData, deleteAll=False) -> int:
        if deleteData is None:
            print('Nothing to save, becuase data paramter is empty')
            return 0
        
        if not isinstance(deleteAll, bool):
            raise ValueError("deleteAll must be a boolean")
            
        try:
            if deleteAll: # deleteAll is used to toggle between delete_one and delete_many
                result = self.database.animals.delete_many(deleteData)
            else:
                result = self.database.animals.delete_one(deleteData)
            
            return result.deleted_count
        
        except Exception as e: 
            print(f'An error occured: {e}')
            return 0 # no updates where made
        
        
        
                
                