# Animal Shelter Dashboard — Grazioso Salvare

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-0081CB?style=for-the-badge&logo=dash&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Overview

A dashboard for Grazioso Salvare, a fictional search and rescue dog training organization. It lets staff filter Austin Animal Center data to find dogs that match the criteria for their rescue programs without calling the shelter or sorting through new intakes by hand. It is a single-page web application with a Dash frontend, a Flask backend, and a MongoDB database.

This project is an enhanced version of the [Animal Shelter Dashboard](https://github.com/crestongetz/Animal-Shelter-WebDashboard-Grazioso-Salvare/tree/main). You can view all the changes made visually using the [commits page](https://github.com/crestongetz/Animal-Shelter-Dashboard-Grazioso-Salvare/commits/main/).

## Changes

- **Separated the logic into a backend and a frontend.** Dash is kept as the frontend in the Jupyter notebook file, and Flask is implemented as the backend in the `app` directory.
- **Made UI and UX improvements.**
- **Improved security** by adding a login popup, securing endpoints with an API key, and managing environment variables.
- **Created a database.** A MongoDB database was set up on Atlas for this application.
- **Performed ETL** on the Real Austin animal shelter API and loaded it into the database.
- Client-Server Architecture
