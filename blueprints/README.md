# T2A2 API Webserver - Travel Planner API
## Adam Hutt 
## Student Number - 14793

[Github Repository](https://github.com/huttadam/API-Webserver-Travel-Plan)

[Trello Board](https://trello.com/b/Sav7abed/api-webserver)

---

## Contents

* [Installation and Setup](#installation-and-setup)
* [R1: Problem Indentification](#r1-identify-the-problem-you-are-trying-to-solve-with-this-app)
* [R2: Problem Justification](#r2-why-is-it-a-problem-that-needs-solving)
* [R3: Database System](#r3-why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
* [R4: ORM Functionalities and Benefits](#r4-identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)
* [R5: Endpoints](#r5-endpoints)
    * [Auth/User Routes](#auth-routes)
    * [Trips Routes](#Trips-routes)
    * [Destinations Routes](#Destinations-routes)
    * [Activities Routes](#Activities-routes)
    * [Comments Routes](#Comments-routes)
* [R6: ERD](#r6-erd)
* [R7: Third Party Services](#r7-detail-any-third-party-services-that-your-app-will-use)
* [R8: Models and Relationships](#r8-describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
* [R9: Database Relations](#r9-discuss-the-database-relations-to-be-implemented-in-your-application)
* [R10: Planning and Tracking Tasks](#r10-describe-the-way-tasks-are-allocated-and-tracked-in-your-project)
* [References](#references)

---

### Installation and Setup

Inside the folder of the API application, type the following commands in terminal:

On Mac OS:
```
psql postgres
```
On WSL:
```
sudo -u postgres psql 
```
Then to create the database:
```
CREATE DATABASE travel_db;
```
Next, connect to the new database:
```
\c travel_db;
```
Create a user with a password, then grant all privileges, for example:
```
CREATE USER nomad_one WITH PASSWORD 'wander123';

GRANT ALL PRIVILEGES ON DATABASE travel_db TO nomad_one;
```
Open a new terminal window,enter the same folder as the source code, run the following to create and activate a virtual environment:
```
python3 -m venv .venv

source .venv/bin/activate
```
Install packages required:
```
python3 -m pip install -r requirements.txt
```
Change file '.flaskenv.sample' to just '.flaskenv', and update the contents, for example:
```
# Database connection string
DB_URI = "postgresql+psycopg2://nomad_one:wander123@localhost:5432/travel_db"

# JWT secret key
JWT_KEY="Anything Here"
```
Finally, run the following cli commands to set up and run the Flask app:
```
flask db create

flask db seed

flask run
```
The port has been set to 8000, now we should be able to connect to http://127.0.0.1:8000/ via our browser, Insomnia or Hoppscotch

---

### R1 Identify the problem you are trying to solve with this app