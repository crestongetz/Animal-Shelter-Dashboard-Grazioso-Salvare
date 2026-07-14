import os
from flask import jsonify, request
from bson.json_util import dumps
import json

# Global dict to store the filters for dropdown menu.
RESCUE_QUERIES = {
    'Water Rescue': {
        "animal_type": "Dog",
        "breed": {"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland"]},
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
    },

    'Mountain or Wilderness Rescue': {
        "animal_type": "Dog",
        "breed": {"$in":["German Shepherd","Alaskan Malamute","Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
    },

    'Disaster Rescue or Individual Tracking': {
        "animal_type": "Dog",
        "breed": {"$in":["Doberman Pinscher","German Shepherd", "Golden Retriever","Bloodhound","Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}
    }
}


def register_animal_routes(server, shelter):
    """Registers routes for the animal shelter API"""

    # Adds requirement for API key to access the API routes.
    # Method will be called before all requests to sever. Key must match env file.
    @server.before_request
    def require_key():
        """Adds requirement for API key to access the API routes"""
        if request.path.startswith('/api/'):
            expected = os.environ.get('API_KEY')
            if request.headers.get('x-api-key') != os.environ.get('API_KEY'):
                return jsonify({'error': 'Unauthorized access'}), 401


    # Route to return all animals in the database.
    @server.route('/api/animals', methods=['GET'])
    def get_all_animals():
        """Returns all animals in database"""
        try:
            animals = shelter.read({})
        except Exception as e:
            return jsonify({'error':str(e)}), 500
        return json.loads(dumps(animals)), 200 #return as JSON prevents typeError 
    

    # Route to return filtered animals
    @server.route('/api/animals/filter', methods=['GET'])
    def get_filtered_animals():
        """Returs a filtered list of dogs based on query request"""
        rescue_type_filter = request.args.get('rescue_type') # sends filter type via args in URL
        query = RESCUE_QUERIES.get(rescue_type_filter, {}) # will return empty dict if none is found
        try:
            animals = shelter.read(query)
        except Exception as e:
            return jsonify({'error':str(e)}), 500
        return json.loads(dumps(animals)), 200 #return as JSON prevents typeError 




