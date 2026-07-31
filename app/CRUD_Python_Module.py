# Creston Getz 7/13/26
# This is a CRUD module for the Animal Shelter Dashboard.
# It connects to a MongoDB database running on Atlas and implements the CRUD operations for the animals collection.


import os
from urllib.parse import quote_plus
from pymongo import MongoClient
from bson.objectid import ObjectId


# JSON Schema validator for the animals collection
# Inspired by : https://json-schema.org/overview/what-is-jsonschema and examples from Claude
ANIMAL_SCHEMA = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["animal_id", "animal_type", "breed", "intake_date"],
        "properties": {
            "animal_id": {"bsonType": "string"},
            "intake_date": {"bsonType": ["date", "null"]},
            "date_of_birth": {"bsonType": ["date", "null"]},
            "name": {"bsonType": "string"},
            "age": {"bsonType": "string"},
            "animal_type": {"bsonType": "string"},
            "breed": {"bsonType": "string"},
            "color": {"bsonType": "string"},
            "sex_upon_outcome": {"bsonType": "string"},
            "found_address": {"bsonType": "string"},
            "health_condition_at_intake": {"bsonType": "string"},
            "source": {"bsonType": ["string"]},
            "age_in_weeks": {"bsonType": ["double", "int", "string"]},
        },
    }
}


# This class creates an object we can perform operations on easily and pass between methods/files.
# It connects to the database using env vars and implements CRUD methods we can use on the object via self.
# See api.py for its usage.
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, DB, COL):
        # Initializes the MongoClient, the database, and the collection.
        # Requires the aac database, the animals collection, and the aac user/password.

        # Atlas cluster address
        HOST = os.environ["MONGO_HOST"]

        # Credentials are URL-encoded in case they contain special characters.
        # quote_plus changes special characters to be URL safe.
        # This line was created by Claude Code with some edits by me. quote_plus helped fix some problems I was having.
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
            self.collection.insert_one(data)  # data should be a dictionary
            return True

        except Exception as e: # If data is not empty but not a dict
            print(f'An error occurred: {e}')
            return False


    # This method implements the Read in CRUD. It will return a Python list full of MongoDB query results.
    def read(self, data) -> list:
        if data is None:
            print('Nothing to read, because the data parameter is empty')
            return list()
        try:
            # Reads data from the database and adds it to a list
            results = self.collection.find(data)
            list_of_results = [doc for doc in results] # Change to a subset of the data for large datasets

            return list_of_results

        except Exception as e: # If data is not empty but not a dict
            print(f'An error occurred: {e}')
            return list()
    
    
    # This method implements the Update in CRUD. It returns the number of updated objects.
    # The optional parameter updateAll can be used to change many entries. The method updates one entry by default.
    def update(self, query, updateData, updateAll=False) -> int:
        if updateData is None:
            print('Nothing to update, because the updateData parameter is empty')
            return 0

        if query is None:
            print('Nothing to update, because the query parameter is empty')
            return 0
        
        if not isinstance(updateAll, bool):
            raise ValueError("updateAll must be a boolean")

        try:
            if updateAll: # updateAll is used to toggle between update_one and update_many
                result = self.collection.update_many(query, updateData)
            else:
                result = self.collection.update_one(query, updateData)
                
            return result.modified_count
                
        except Exception as e: 
            print(f'An error occurred: {e}')
            return 0 # no updates were made

            
    # This method implements the Delete in CRUD. It returns the number of deleted objects.
    # The optional parameter deleteAll can be used to delete many entries. The method deletes one entry by default.
    def delete(self, deleteData, deleteAll=False) -> int:
        if deleteData is None:
            print('Nothing to delete, because the deleteData parameter is empty')
            return 0
        
        if not isinstance(deleteAll, bool):
            raise ValueError("deleteAll must be a boolean")
            
        try:
            if deleteAll: # deleteAll is used to toggle between delete_one and delete_many
                result = self.collection.delete_many(deleteData)
            else:
                result = self.collection.delete_one(deleteData)
            
            return result.deleted_count

        except Exception as e:
            print(f'An error occurred: {e}')
            return 0 # No deletions were made


    # This method is used to bulk load data into the MongoDB database.
    # Returns the number of IDs entered, or 0 on error.
    def load_database(self, list_of_data) -> int:
        if not list_of_data:
            return 0

        try:
            result = self.collection.insert_many(list_of_data)
            return len(result.inserted_ids)
        except Exception as e:
            print(f"There was an error: {e}")
            return 0


    # Applies the JSON Schema validator to the collection.
    # Inspired by: https://json-schema.org/overview/what-is-jsonschema and examples from Claude
    def apply_schema(self, validation_action="error") -> bool:
        try:
            self.database.command("collMod", self.collection.name, validator=ANIMAL_SCHEMA, validationLevel="strict",
                                  validationAction=validation_action,
            )
            return True
        
        except Exception as e:
            print(f"Could not apply schema: {e}")
            return False

                
                