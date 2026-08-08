# Animal Shelter Dashboard — Grazioso Salvare

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-0081CB?style=for-the-badge&logo=dash&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Overview

This is a **full-stack web dashboard** created for Grazioso Salvare, a search-and-rescue dog training organization. It is an enhanced version of the original [Animal Shelter Dashboard](https://github.com/crestongetz/Animal-Shelter-WebDashboard-Grazioso-Salvare/tree/main). You can view all the changes made visually using the [commits page](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/commits/main/) or the [changes](#Changes-made) section for a text description.

The dashboard uses the **real API data** from the Austin Animal Shelter and loads it into a MongoDB Atlas collection. After being
loaded into the database, the [app](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/tree/0b82e2e1728767fb445a3d6af7321daa7f778a0a/app) directory or backend of the application can be used to communicate with the Dash front end via HTTP. This is a client-server architecture.

The dashboard provides a convenient way for Grazioso Salvare to filter dogs specifically for their dog training programs. The filters, which can be used in a dropdown menu on the dashboard, are stored in a dictionary in the api.py file. Doing so improves usability and prevents NoSQL injections.


## Getting Started
You will need the following software or libraries, all of which can be downloaded using [requirements.txt](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/blob/0b82e2e1728767fb445a3d6af7321daa7f778a0a/requirements.txt): 
- Flask
- Pymongo
- Python-dotenv
- Pandas
- Numpy
- Dash
- Plotly
- Matplotlib
- Requests
- Jupyter
- Dash_mantine_components
- Sodapy
- Geopy

**For the application to work, you will also need to create your own env file. The env file was not included in this application to show best practices. You can use all of the logic in the application as is, but you will need to make a Mongo database on Atlas and connect it through environment variables. Specifically, you will need to create and obtain the following:**
- MONGO_USER=aacuser
- MONGO_PASS=
- MONGO_HOST=
- MONGO_DB=aac
- MONGO_COLLECTION=animals
- FLASK_SECRET_KEY=
- DASH_PASSWORD=password123
- API_KEY=
- [SOCRATA_APP_TOKEN](https://data.austintexas.gov/)=


## Changes made

- **Separated the logic into a backend and a frontend.** Dash is kept as the frontend in the Jupyter notebook file, and Flask is implemented as the backend in the `app` directory.
- **Made UI and UX improvements.**
- **Improved security** by adding a login popup, securing endpoints with an API key, and managing environment variables.
- **Created a database.** A MongoDB database was set up on Atlas for this application.
- **Performed ETL** on the Real Austin animal shelter API and loaded it into the database.
- **Client-Server Architecture** instead of MVC.
