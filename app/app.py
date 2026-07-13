# Creston Getz  7/13/26
# This file implements the API for the dashbaord. It seperates the backend logic from the old jupyter notebook dashbaord file.
# This API built with Flask will handle CRUD operations and send a API back to the front end of the daashbarod which will be created using Dash.
# Security will be implemented in Dash.
#
# 
#
import os
import pandas as pd
from dotenv import load_dotenv
from flask import Flask
from CRUD_Python_Module import AnimalShelter
from api import register_animal_routes

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
register_animal_routes(server, shelter)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(shelter.read({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an
# invlaid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will reeturn a new dataframe that does not contain the dropped column(s)
df.drop(columns=['_id'], inplace=True)