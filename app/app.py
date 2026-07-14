# Creston Getz  7/13/26
# This file implements the API for the dashbaord. It seperates the backend logic from the old jupyter notebook dashbaord file.
# This API built with Flask will handle CRUD operations and send a API back to the front end of the daashbarod which will be created using Dash.
# Security will be implemented in Dash.
#
# 
#
import os
import sys
import pandas as pd
from dotenv import load_dotenv
from flask import Flask

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.CRUD_Python_Module import AnimalShelter
from app.api import register_animal_routes

load_dotenv()

# Create Flask sever
server = Flask(__name__)
server.config['SECRET_KEY'] = os.environ["FLASK_SECRET_KEY"]


# Loads mongoDB connection using env file and CRUD file
shelter = AnimalShelter(
    os.environ["MONGO_USER"],
    os.environ["MONGO_PASS"],
    os.environ["MONGO_DB"],
    os.environ["MONGO_COLLECTION"],
)


# Register the routes we will use for backend API calls.
# see app/api.py for routes
register_animal_routes(server, shelter)


if __name__ == '__main__':
    # Run the API on port 5001
    # On mac port 5000 is taken by air drop
    server.run(port=5001, debug=True)