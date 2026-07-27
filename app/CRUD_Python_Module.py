# Creston Getz 7/13/26
# This is a CRUD module for the Animal Shelter Dashboard.
# It connects to a MongoDB database running on Atlas and implements the CRUD operations for the animals collection.


import os
from urllib.parse import quote_plus
from pymongo import MongoClient
from bson.objectid import ObjectId


# This class creates an object we can perform operations on easily and pass between methods/files.
# It connects to the database using env vars and implements CRUD methods we can use on the object via self.
# see api.py for its usage.
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, DB, COL):
        # Initializing the MongoClient.
        # databases and collections. Requires the aac database, animals collection, and the aac user/pass.

        # Atlas cluster address
        HOST = os.environ["MONGO_HOST"]

        # Credentials are URL-encoded in case they contain special characters
        # quote plus changes special chars to be url safe. 
        # This line was created by Claude code with some edits by me. Quote plus helped fix some problems I was having.
        uri = "mongodb+srv://%s:%s@%s/?appName=Cluster0" % (quote_plus(USER), quote_plus(PASS), HOST)

        self.client = MongoClient(uri)
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

            
    # This method implements the Create in CRUD. It returns a boolean if the query created the entry or not.
    def create(self, data) -> bool:
        if data is None:
            print('Nothing to save, because data parameter is empty')
            return False
        try:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
            
        except Exception as e: #if data is not empty but not a dict
            print(f'An error occurred: {e}')
            return False


    # This method implements the Read in CRUD. It will return a python list full of MongoDB query results.
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
            print(f'An error occurred: {e}')
            return list()
    
    
    # This method implements Update in CRUD. It returns number of updated objects.
    # An optional parameter updateAll can be used to change many entries. Method will update one entry by default.
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
            print(f'An error occurred: {e}')
            return 0 # no updates were made

            
    # This method implements Delete in CRUD. It returns number of deleted objects.
    # An optional parameter deleteAll can be used to delete many entries. Method will delete one entry by default.
    def delete(self, deleteData, deleteAll=False) -> int:
        if deleteData is None:
            print('Nothing to save, because data parameter is empty')
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
            print(f'An error occurred: {e}')
            return 0 # no updates were made


    # This method is used to bulk load data into the Mongo Database
    # Returns the number of ids entered or 0 on error
    def load_database(self, list_of_data) -> int:
        if not list_of_data:
            return 0

        try: 
            result = self.database.animals.insert_many(list_of_data)
            return len(result.inserted_ids)
        except Exception as e:
            print(f"There was an error: {e}" )
            return 0
                
                