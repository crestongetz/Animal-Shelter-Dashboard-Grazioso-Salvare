# Animal-Shelter-Dashboard-Grazioso-Salvare
## Overview
This is a `full-stack web application` dashboard created for Grazioso Salvare, a search and rescue dog training organization. The dashboard uses a python CRUD module to connect with a mongo database allowing users to filter the Austin Animal Center shelter data in Austin, Texas. The dashboard provides a `user-friendly way to identify dogs` that meet certain profiles based on their age, sex and so on. The projects architecture uses the `MVC design pattern`, MongoDB serves as the Model, Dash widgets as the View, and the Python CRUD module as the Controller 

## Getting Started
You will need the following software or libraries:  
1. [Python ](https://www.python.org/downloads/)
2. [Python CRUD module](CRUD_Python_Module.py)
3. [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)  
4. [MongoDB](https://www.mongodb.com/docs/get-started/?language=nodejs)
5. [Dash](https://dash.plotly.com/installation) 
6. [Dash_leaflet](https://www.dash-leaflet.com/) 
7. [Pandas](https://pandas.pydata.org/)

## Usage and Functionality
See [README PDF](Grazioso-Salvare_README_PDF.pdf)

## Methodology of Tools Used
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

## Steps to Complete Project
1. Before any work was done on the dashboard, the specs and requirements were heavily reviewed. From the specs and requirements, we created a plan to create the dashboard. 
2. The first step of the plan was to use the Python CRUD module to connect with MongoDB and display an unfiltered view of the data. From there, we can add more complex logic. 
3. After we added the unfiltered view of the MongoDB data using a dash data table, pymongo, and our CRUD module, we worked on the formatting and styling of the table. We added the ability to perform basic filtering, limited the number of rows, enabled pagination, formatted the headers, added the logo, and so on. 
4. Once the data table was displayed neatly and correctly, we created the queries to filter specific types of training dogs. The queries where created from the spec sheet given to us by Grazioso Salvare. Such as water rescue or mountain and wilderness tracking. With these queries, we implemented a dropdown menu so users can easily select what filter they want to use. With the dropdown and our queries, we can use a dash call back to change the data shown on the data table. 
5. Next, we implemented the dash leaflet geolocation chart. Again, using a callback and the GPS coordinates in the data, we can display the location of the animal as well as various info about it using a popup. 
6. Lastly, we created a pie chart that will show the top 10 dog breeds in the data table. It will change based on the filter used. If a filter is used that removes the dog breeds or animal type from the data table, then no chart will be shown. 

## Challenges
* Throughout this project, we encountered many challenges and obstacles. 
* The formatting of the header and logo proved to be difficult. We used flexbox in CSS to neatly display the two next to each other. 
* When creating the queries, it required some trial and error to correctly connect the callback using the filter_type variable. In the end, using an if else branch seemed like an easy way to create it. Future improvements to this are likely possible. 
* Like formatting the headers and logo, when working on geolocation chart and pie chart we had to research some CSS to style them well. We also reviewed the dash documentation a lot to create the various styling features for the data table. For example, we wanted to make the drop-down filter menu more intuitive for users. We found that dash lets us add a placeholder value so we can let the user know what it does. 
* When creating the pie chart, we had to review the pyplot documentation as the plain pie chart was showing data in the entire data set and un-readable. After creating some subsets in pandas and filtering just the top 10 dog breeds, the chart is significantly more readable. 

## Future Improvements
1. Removed Hard Coded Login
2. Improve Style of page

## Reflection
Writing software that is maintainable, readable, and adaptable is a key part of software development. It helps prevent us from reinventing the wheel. I was able to build this project because other engineers created Python, Dash, and MongoDB. I did not have to implement these technologies from scratch. I applied this principle when creating my Python CRUD module. By making it maintainable, adaptable, and readable, I (or anyone else) can reuse the module whenever I need to connect a MongoDB database with Python code.
This project had a specific set of requirements that Grazioso Salvare wanted the dashboard to meet, both functionally and visually. As a computer scientist, breaking the problem down and working on it in parts was the way to go. Doing so allowed me to iterate and refine the solution step by step. I used several different approaches compared to previous projects. Because this project involved multiple technologies, I knew I would not remember every detail. Learning how to effectively read and apply documentation was extremely valuable and helped me integrate all the pieces together. In the future, I can apply this process to meet other client requirements more efficiently.
This project was insightful in showing that even relatively small tools can have meaningful impact. At the core, a computer scientist or software engineer solves problems with code. We build systems that make data more accessible and actionable. This dashboard allows Grazioso Salvare to quickly filter a large dataset for specific types of rescue dogs and visualize relevant information on a map, improving both efficiency and decision-making.

