# Creston Getz  7/13/26
# This file creates the Flask server for the APIs. It separates the backend logic from the old Jupyter notebook dashboard file.
# The APIs were built with Flask to handle the read in CRUD.
# The APIs are used to communicate with the Dash front end.


import os
import sys
import pandas as pd
from dotenv import load_dotenv
from flask import Flask
from app.CRUD_Python_Module import AnimalShelter
from app.api import register_animal_routes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

# Create Flask server
server = Flask(__name__)
server.config['SECRET_KEY'] = os.environ["FLASK_SECRET_KEY"]


# Loads the MongoDB connection using the env file and the CRUD file
shelter = AnimalShelter(
    os.environ["MONGO_USER"],
    os.environ["MONGO_PASS"],
    os.environ["MONGO_DB"],
    os.environ["MONGO_COLLECTION"],
)


# Register the routes we will use for backend API calls.
# See app/api.py for the routes.
register_animal_routes(server, shelter)


if __name__ == '__main__':
    # Run the API on port 5001.
    # On macOS, port 5000 is taken by the AirPlay Receiver.
    server.run(port=5001, debug=True)