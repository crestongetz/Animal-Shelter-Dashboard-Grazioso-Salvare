# Animal Shelter Dashboard — Grazioso Salvare

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-0081CB?style=for-the-badge&logo=dash&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Overview

This is a **full-stack web dashboard** created for Grazioso Salvare, a search-and-rescue dog training organization. It is an enhanced version of the original [Animal Shelter Dashboard](https://github.com/crestongetz/Animal-Shelter-WebDashboard-Grazioso-Salvare/tree/main). You can view all the changes made visually using the [commits page](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/commits/main/) or the [narratives](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/tree/b3d9c51c5731dd6085e88693644d9970d8c9ce1f/narratives) for a deep dive into both the changes made and why.

The dashboard uses the **real API data** from the Austin Animal Shelter and loads it into a MongoDB Atlas collection. After being
loaded into the database, the [app](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/tree/0b82e2e1728767fb445a3d6af7321daa7f778a0a/app) directory or backend of the application can be used to communicate with the Dash front end via HTTP. This is a client-server architecture.

The dashboard provides a convenient way for Grazioso Salvare to filter dogs specifically for their dog training programs. The filters, which can be used in a dropdown menu on the dashboard, are stored in a dictionary in the api.py file. Doing so improves usability and prevents NoSQL injections.

[View this project in my ePortfolio](https://crestongetz.github.io/)

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
- MONGO_PASS= TODO: MongoDB Atlas aacuser password
- MONGO_HOST= TODO: Atlas cluster hostname
- MONGO_DB=aac
- MONGO_COLLECTION=animals
- FLASK_SECRET_KEY= TODO: Flask session signing key. Signs session cookies. Any long string
- DASH_PASSWORD=password123
- API_KEY= TODO: Shared secret between front and backend. Any long string.
- [SOCRATA_APP_TOKEN](https://data.austintexas.gov/)= TODO: App token allows for increased API requests but is not needed.

## How to Run
The dashboard runs as two processes: a Flask backend running on port 5001 (for mac) and a Dash frontend on port 8050. Both must run.
### Install
1. Clone repo: `git clone https://github.com/crestongetz/Animal-Shelter-WebDashboard-Grazioso-Salvare.git`
2. `cd Animal-Shelter-WebDashboard-Grazioso-Salvare`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`

### Config
1. [Create database](https://www.mongodb.com/products/platform/atlas-database) and set up user 
2. Set up .env file

### Load Database
1. Open `data/data.ipynb`
2. Run it. Re-run when you want to refresh data.

### Start Flask
1. Open a new terminal in the project root.
2. `python -m app.app`

### Start dashboard
1. Open a new terminal
2. Open `Grazioso_Dashboard.ipynb`
3. Hit `Run all cells`
4. The dashboard will load on http://127.0.0.1:8050
5. A login prompt will show. Use your DASH_PASSWORD from env. Username is `admin`

## Repository Files
- `app/CRUD.py` | Handles database connection
- `app/app.py` and `app/api.py` | Handles Flask logic
- `data/data.ipynb` | Handles ETL and Austin Animal Shelter API logic. This file loads the data into the MongoDB database.
- `narratives` | Deep dive into the design choices and changes made
- `Graziso_Dashbaord.ipynb` | Main application file. Handles the Dash frontend.

## Changes Made
- **Separated the logic into a backend and a frontend.** Dash is kept as the frontend in the Jupyter notebook file, and Flask is implemented as the backend in the `app` directory.
- **Made UI and UX improvements.**
- **Improved security** by adding a login popup, securing endpoints with an API key, and managing environment variables.
- **Created a database.** A MongoDB database was set up on Atlas for this application.
- **Performed ETL** on the Real Austin animal shelter API and loaded it into the database.
- **Client-Server Architecture** instead of MVC.

## Future Improvements:
1. Improve ETL data types. age_in_weeks should have no strings stored in the database.
2. Add a fail-safe for a failed database load.
3. Add automatic or scheduled loading from the API.
4. Split into two database users: one for loading and one for reading.
5. Use logging instead of print in various parts of the application such as the CRUD module.
6. Improve security for production in various parts.
7. Add testing.
8. Overall UI and UX.
