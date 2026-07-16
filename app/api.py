# Creston Getz 7/13/26
# This file implements the APIs for the dashboard.
# It allows the dropdown filtering to be separate from the dash application and allows the backend to communicate with Dash.
# There are only 3 GET methods; there is no way to update, delete, or create entries as of now.

import os
import secrets
from flask import jsonify, request
from bson.json_util import dumps
import json

# Global dict to store the filters for the dropdown menu.
# These are MongoDB queries that, when used with pyMongo, let us filter the dataset before we send it to the front-end Dash app.
# These used to be stored inside the dash app.
RESCUE_QUERIES = {
    'Water Rescue': {
        "animal_type": "Dog",
        "breed": {"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland"]},
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156} # in weeks
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


# Registers routes for the animal shelter API
# Inspired by https://flask.palletsprojects.com/en/stable/quickstart/#routing accessed 7/12/26 and examples from Claude
def register_animal_routes(server, shelter):
    """Registers routes for the animal shelter API"""

    # Adds requirement for API key to access the API routes.
    # Method will be called before all requests to server. Key must match env file.
    @server.before_request
    def require_key():
        """Adds requirement for API key to access the API routes"""
        if request.path.startswith('/api/'):
            expected_key = os.environ.get('API_KEY')
            provided_key = request.headers.get('x-api-key')

        if not expected_key or not provided_key: # ensure both keys exist
            return jsonify({'error': 'Unauthorized access'}), 401
            
        # secrets.compare_digest is better than a direct comparison for the API.
        # It helps prevent an attacker from performing a time-based attack.
        if not secrets.compare_digest(provided_key, expected_key):
            return jsonify({'error': 'Unauthorized access'}), 401


    # Route to return all animals in the database.
    @server.route('/api/animals', methods=['GET'])
    def get_all_animals():
        """Returns all animals in database"""
        try:
            animals = shelter.read({})
        except Exception as e:
            return jsonify({'error':str(e)}), 500
        return json.loads(dumps(animals)), 200 #return as JSON prevents TypeError
    

    # Route to return filtered animals. The rescue type requested is determined by the params in the request.
    @server.route('/api/animals/filter', methods=['GET'])
    def get_filtered_animals():
        """Returns a filtered list of dogs based on query request"""
        rescue_type_filter = request.args.get('rescue_type') # sends filter type via args in URL
        query = RESCUE_QUERIES.get(rescue_type_filter, {}) # will return empty dict if none is found
        try:
            animals = shelter.read(query)
        except Exception as e:
            return jsonify({'error':str(e)}), 500
        return json.loads(dumps(animals)), 200 #return as JSON prevents TypeError




