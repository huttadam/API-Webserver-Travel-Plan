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

### Installation and Setup Istructions

Inside the API Webserver project folder, type the following commands in terminal:

On Mac OS:
```psql postgres```

or

On WSL:
```sudo -u postgres psql ```

Then to create the database:

```CREATE DATABASE travel_db;```

Next, connect to the new database:

```\c travel_db;```

Create a user with a password:

```CREATE USER nomad_one WITH PASSWORD 'wander123';```

Grant all privileges to the user:

```GRANT ALL PRIVILEGES ON DATABASE travel_db TO nomad_one;```

Open a new terminal window, enter the same folder as the source code (src), run the following to create and activate a virtual environment:

```python3 -m venv .venv```

```source .venv/bin/activate```

Install packages required:

```python3 -m pip install -r requirements.txt```

Change file '.flaskenv.sample' to just '.flaskenv', and update the  fields:
```
# Database connection string
DB_URI = "postgresql+psycopg2://nomad_one:wander123@localhost:5432/travel_db"

# JWT secret key
JWT_KEY="Anything Here"
```
Run the following cli commands to set up and run the Flask app:

``` flask db create```

```flask db seed```

```flask run```

If any errors occur during seed process, you can run the below also.

```flask db drop```

The port has been set to 8000, please try connecting to http://127.0.0.1:8000/ via your browser, Insomnia or Hoppscotch

---

### R1 - Identify the problem you are trying to solve with this app

 The Tourism and Travel industries since the re-opening of countries borders for tourists since the COVID-19 pandemic are experiencing a a huge spike in popularity and income. These industries have always been strong and especially since the availability of the internet, it has made travel destinaton information a lot easier to access and utilize. The problem with all this new information is that it can be difficult to manage and keep track of what you actually want to do and where you want to go. There are so many many travel blogs/vlogs to consume, planning and packing  before travelling that you can lose track of your goals before or on a trip.

 As a keen traveller myself, I have experienced a lot of frustration trying to gather information about an activity/monument/restaurant and if is acheiveable to visit when you are in the same city or country as it.  Whether your on a strict time-frame, jet-lagged or have lost a lot of time due to unforseen events, the frustration is compounded in trying to remember the crucial information about this activity. e.g. What website you visited?, What video you watched? Where exactly it was? Why was it special ? is it really worth it?  Its often that after I left left a destination,  I experience thoughts of .. I was supposed to go ... , Why didnt I see ... . 

 My API webserver attempts to solve this disorganization and stress revolved around travel and give the user the ability to track, add, sort, and update the information they have researched to ultimately improve the planning and decision-making around the travel experience and make the most of the users time travelling. In addition, the user is also able to gather ideas and be an inspiration for other users. The API webserver will have a feature for the public and account holders to view other users activities (minus personal information) and gather inspiration from them. Account holders are also able to leave comments on activities and gather additional information about potential activities.


 ### R2 - Why is it a problem that needs solving?

 As mentioned above having all the information about a travel destination is not benefitial for a person unless they can organize their plans, store information they have recieved which in-turn will really increase the likelihood of following through on these plans. 

 This is a problem that needs solving as , in todays economic climate , the cost of travelling and goods have increased rapidly and when people have the oppurtunity to travel, they need to ensure the time and money they are spending is not wasted. Furthermore,In terms of the public discussion feature, I believe there is space in the market amongst other huge online travel tools ,(Youtube (travel vlogs), TripAdvisor) for a user-based platform for travellers to gather information from other travellers. I feel advertisment money and big corporate companies give way to fake reviews which give users a biased or unfaithable depiction of what an acitivty or detination is actually.

In summary, the solving of this problem can save users a lot of time and exhaustion when travelling as well as act as a community sounding board for traveller and tourists to organize travel information and gather travel information, which ultimately leads to a better travel experience.


 ### R2 - Why have you chosen your database system. What are the drawbacks compared to others?

Databases are an essential feature for API webservers and the storing and management of data needs to be a process that is functional and flexible. For my API travel planners database system I have selected PostgreSQL, which is a well-known, trusted program to manage data throughout the I.T industry. Some reasons for my choice as follows

#### Contraints
A key feature of PostgreSQL are its contraints . Contrainsts assist in controlling data types with rules. Some examples of these contraints are foreign key constraints, unique constraints, and check constraints. These features help ensure data integrity is kept at the  database level, preventing the inserting of inconsistent or invalid data and keeping structing when deletions are made. In my API project, the ability  ability to enforce and maintain data type and integrity with contraints is a an essential factor for is functionality.


#### Robustness
PostgreSQL has a large set of features that can be usedto facilitate multiple requirements. These features attribute to many many postives of PostgreSQL, and example would be its ACID ((Atomicity, Consistency, Isolation, Durability)) complicance which simply means that data integrity is maintained during interactions with the database when most common mistakes or problems would occur.
Another feature to explain its robustness is MVCC (Multi-Version Concurrency Control) which improves performance especially in a multi-user database. While handling muitple transactions the database does not lock, it simultaneously processes the transactions and records these versions in-case a rollback or data integrityis compromised in any way.

#### Scalability
PostgreSQL is suited for large and small datasets. While starting off with a small dataset , as data grows and become more complicated , postgreSQL is able to support this growth anf of course we can  adopt additional features to suite this change as required.


#### Compareable to other databases
As mentioned above, PostgreSQL has many benefits and well suited for my API project. However, when compared to other databases and their benfits, some noted drawbacks are noted when trying to acheive specfifc goals, these are as follows.

MySQL - Another database which uses SQL language. While not object relational like postgresql, MySQL as a smaller learning curve than PostgreSQL. As I am new to API's and manageing data the simpler syntax could be an added benefit for speed and going thorough a learning process. 
In addition to this, MySQL also utilizes cloud compatibility, which is attractive for projects/companies looking for the future and requiring a huge scaled database.

Oracle - A key featue of Oracle is it is a multi-model system. In simple terms this means that several applications utilise the same database and benfit from using the same models. Not only does this derease workload but streamlines application bulding to suite a already designed database. 





