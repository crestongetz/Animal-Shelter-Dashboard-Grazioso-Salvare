# Animal-Shelter-Dashboard-Grazioso-Salvare
## Overview
This is a `full-stack web application` dashboard created for Grazioso Salvare, a search and rescue dog training organization. The dashboard uses a python CRUD module to connect with a mongo database allowing users to filter the Austin Animal Center shelter data in Austin, Texas. The dashboard provides a `user-friendly way to identify dogs` that meet certain profiles based on their age, sex and so on. The projects architecture uses the `MVC design pattern`, MongoDB serves as the Model, Dash widgets as the View, and the Python CRUD module as the Controller 

## Getting Started
You will need the following software or libraries:  
1. [Python ](https://www.python.org/downloads/)
2. Python CRUD module(add link to readME) 
3. [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)  
4. [MongoDB](https://www.mongodb.com/docs/get-started/?language=nodejs)
5. [Dash](https://dash.plotly.com/installation) 
6. [Dash_leaflet](https://www.dash-leaflet.com/) 
7. [Pandas](https://pandas.pydata.org/)

## Usage and Functionality
TODO

## Tools Used
### Python
Various python libraries such as pymongo, dash, pandas and dash leaflet were used in this application due to their flexibility and ease of connecting to MongoDB. In our Python CRUD module, we used pymongo and pandas to connect to Mongo.

### MongoDB
MongoDB was used for this project to implement the model in the MVC architecture. It accommodates the data needed for the animal shelter, including varied data and location data. By using MongoDB the application will be very easy to use with other datasets due to the flexibility of the document style. MongoDB also offers a lot of support for python, which makes working with the other tools used easier.

### Dash
Another powerful python library that acts as the view and controller part of the MVC design. It abstracts most of the front-end work of development allowing us to use built in features to display data such as the data table above.
Dash Leaflet – An extension library for dash that lets us implement the geolocation map using the GPS coordinates in the data. This makes the dashboard more interesting and interactive. 

### Pymongo
Used for its ease of use with MongoDB. It offers full support for MongoDB querying. And it is a very scalable library that lets Python dicts be mapped to Mongo’s BSON format.

### Pandas
Pandas is a very powerful data analysis library with the use of data frames. The library helps us connect the data we import from pymongo and display it on dash acting as the controller of the application.

## Challenges

## Future Improvements

## Reflection

