# T2A2 API Webserver - Travel Planner API
## Adam Hutt 
## Student Number - 14793

[Github Repository](https://github.com/huttadam/API-Webserver-Travel-Plan)

[Trello Board](https://trello.com/b/Sav7abed/api-webserver)

---

## Contents

* [Installation and Setup](#installation-and-setup-instructions)
* [R1: Problem Indentification](#r1---identify-the-problem-you-are-trying-to-solve-with-this-app)
* [R2: Problem Justification](#r2---why-is-it-a-problem-that-needs-solving-?)
* [R3: Database System](#r3---why-have-you-chosen-your-database-system-what-are-the-drawbacks-compared-to-others-?)
* [R4: ORM Functionalities and Benefits](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-ORM)
* [R5: Endpoints](#r5-documenting-api-endpoints)
    * [Auth/User Routes](#authuser-routes)
    * [Trips Routes](#trip-routes)
    * [Destinations Routes](#Destination-routes)
    * [Activities Routes](#Activity-routes)
    * [Comments Routes](#Comment-routes)
* [R6: ERD](#r6-erd)
* [R7: Third Party Services](#r7-detail-any-third-party-services-that-your-app-will-use)
* [R8: Models and Relationships](#r8-describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
* [R9: Database Relations](#r9-discuss-the-database-relations-to-be-implemented-in-your-application)
* [R10: Planning and Tracking Tasks](#r10-describe-the-way-tasks-are-allocated-and-tracked-in-your-project)
* [References](#references)

---

### Installation and Setup Instructions

Inside the API Webserver project folder, type the following commands in terminal:

On Mac OS:
```
psql postgres
```

or

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

Create a user with a password:

```
CREATE USER nomad_one WITH PASSWORD 'wander123';
```

Grant all privileges to the user:

```
GRANT ALL PRIVILEGES ON DATABASE travel_db TO nomad_one;
```

Open a new terminal window, enter the same folder as the source code (src), run the following to create and activate a virtual environment:

```
python3 -m venv .venv

source .venv/bin/activate

```

Install packages required:

```
python3 -m pip install -r requirements.txt
```

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


 ### R3 - Why have you chosen your database system, What are the drawbacks compared to others?

Databases are an essential feature for API webservers and the storing and management of data needs to be a process that is functional, flexible and tailored to my skill level. For my API travel planners database system I have selected PostgreSQL, which is a well-known,scalable, open-source and reputable database program which is utlized on a wide-range of applications throughout the I.T industry. Some reasons for my choice as follows

#### Contraints
A key feature of PostgreSQL are its contraints .In simple terms, contrainsts assist in controlling data types of data with rules. Some examples of these contraints are foreign key constraints, unique constraints, and check constraints. These features help ensure data integrity is kept at the  database level, preventing the inserting of inconsistent or invalid data and keeping structing when deletions are made. In my API project, the ability to enforce and maintain data types, relationships between tables (Primary/Foreign Key) and integrity with contraints is a an essential factor for is functionality.


#### Robustness
PostgreSQL has a large set of features that can be usedto facilitate multiple requirements. These features are attributed to the success and and popularity of PostgreSQL. An example of these features would be its ACID ((Atomicity, Consistency, Isolation, Durability)) complicance which simply means that data integrity is maintained during interactions with the database when most common mistakes or problems would occur.
Another feature to explain its robustness is MVCC (Multi-Version Concurrency Control) which improves performance especially in a multi-user database. While handling muitple transactions the database does not lock, it simultaneously processes the transactions and records these versions in-case a rollback or data integrityis compromised in any way.

#### Scalability
PostgreSQL is suited for large and small datasets. While starting off with a small dataset , as data grows and become more complicated , postgreSQL is able to support this growth anf of course we can  adopt additional features to suite this change as required.


#### Compareable to other databases
As mentioned above, PostgreSQL has many benefits and well suited for my API project. However, when compared to other databases and their benfits, some noted drawbacks are noted when trying to acheive specfifc goals, these are as follows.

MySQL - Another database which uses SQL language. While not object relational like postgresql, MySQL as a smaller learning curve than PostgreSQL. As I am new to API's and manageing data the simpler syntax could be an added benefit for speed and going thorough a learning process. In addition to this, MySQL also utilizes cloud compatibility, which is attractive for projects/companies looking for the future and requiring a huge scaled database.

Oracle - A key featue of Oracle is it is a multi-model system. In simple terms this means that several applications utilise the same database and benfit from using the same models. Not only does this derease workload but streamlines application bulding to suite a already designed database. 


### R4 - Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object-Relational Mapper) is a very poweful tool in programming. An ORM acts as the translater between the database and the programming language. The ORM enable the user to access the database from their preferred language rather than switch from one language to another. In the case of my API project we are communicating to the the database in a pythonic way to satisy postgreSQL database syntax.

#### Key functionalities of ORM

- Attributes from the database are mapped to programming language objects which gives the user a flexible interface to manipulate or view data from the database to a web application server.

- Data can be validated and handled through implementing rules, so data integrity errors or violations can be handled  graccefully using easier to understand language in error messages.

- Relationships between entities can be created and mapped from the ORM to the database. Relationships which are vital in the display and mangaing of data, these are relationships like  one to one , one to many etc. 

- CRUD operations are easily serviceable via an ORM , CRUD operations are essential in assisting with interactions from the client to the server in an API and form the bridge between them and the Database . For example the CRUD operations breakdown is as follows. 'C' in CRUD stands for Create, which services POST requests to the server, i.e adding data to the database, 'R' stands for Read which services GET requests to the server i.e. reading/acessing the information in the databse, 'U' stands for Update, which services PUT/PATCH requests to the server, i.e modifyiny/changing data in the database and finally 'D' stands for Delete which services DELETE requests to the server.

- Database queries can can be customized to pull data in a specific format to service specific requirements from the client side, for example , you want to access data from a certain date or a customer/product in the startbase starting with the letter 'Z'.

#### Benefits of an ORM

 As mentioned above, many of the ORM's features are core benefits of using however there are also some additional benefits to using an ORM.

 - The use of objects and function in programming language (OOP) allows us to create a general framework for queries, commands and routes, which means that code can be easily integrated to other applications with similiar database structures. Another key benefit of this is utilzing time to focus of the structure and function of the application rather than re-writing specific queries/commands.

 - Testing can be performed more easily in a programming languge which is essential for building applications for businesses which require a lot of evidence of testing and research to ensure the application is safe for public use and the protection of data.

 - Communication and readability are keys benfits of ORM. This means we can actively control messages from the database and client/server to be readable for the ley-person. These messages can also greatly assist the developer in interpreting Database languages to something they can understand easier.


### R5 Documenting API Endpoints

### Auth/User Routes

#### 1. /users/register

* Methods: POST

* Description: User can creat an account

* Request Parameters: None

* Authentication: None

* Authorisation: None

* Request Body: 

```
{
    "email": "testemail@connection.com",
    "f_name": "Victor",
    "l_name": "Vagabond",
    "username": "VictaDaVagabond",
    "password": "Testing145"
}
```

* Request Response:

HTTP Status Code: 201 CREATED

```
{
	"admin_acc": false,
	"email": "testemail@connection.com",
	"f_name": "Victor",
	"id": 6,
	"l_name": "Vagabond",
	"username": "VictaDaVagabond"
}

```

* Error Handling:

Scenario: This email address is already registered

Error code: 409 CONFLICT

Error Message: 
```
{
	"Error": " This Email address is already registered"
}
```

Scenario: Username already in use

Error code: 409 CONFLICT

Error Message: 
```
{
	"Error": "Someone already has this Username, Please change"
}
```

Scenario: Username and email already in use

Error code: 409 CONFLICT

Error Message: 
```
{
	"Error": "Both Username and Email already registered"
}
```

Scenario: Missing field for f_name (same applies to l_name, username, email and password)

Error code: 400 BAD REQUEST

Error Message:
```
{
	"Error": "The field 'f_name' is required."
}
```

Scenario: Password is invalid

Error code: 400 BAD REQUEST

Error Message:
```
{
	"error": {
		"password": [
			"Password must have a minimum of ten characters + At least one uppercase letter, lowercase letter and number"
		]
	}
}
```
I also have some customized validaton messages for , f_name, l_name, username and email address. 

```
{
	"Error": {
		"email": [
			"Invalid Email address, please check and re-enter"
		],
		"f_name": [
			"Please enter letters only."
		],
		"l_name": [
			"Please enter at least one character."
		],
		"username": [
			"Invalid username, Must be at least 3 Chars"
		]
	}
}

```

#### 2. /login

* Methods: POST

* Description: User login and developing a  JWT token

* Request Parameters: None

* Authentication: None

* Authorisation: None

* Request Body: 

```
{
    "email": "bazza@email.com",
    "password": "LetsgotoSpain22"
	
}
```

* Request Response: 

HTTP Status Code: 200 OK

```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMjU0OTgyOCwianRpIjoiYmJhNjM2ZGMtMmFiYi00Y2RkLWE5ZTMtNTRhYTYyZjkyYWUyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNzAyNTQ5ODI4LCJleHAiOjE3MDI1NjQyMjh9.CoLa30rCOBG8Rn0-O7kjib0GYwn18c7skpWG4O6Btgw",
  "user": {
    "email": "bazza@email.com",
    "f_name": "Barry",
    "l_name": "Backpacker",
    "username": "EuroStar44"
  }
}
```
* Error Handling:

Scenario: Email or password is incorrect

Error code: 401 UNAUTHORIZED

Error message:
```
{
  "Error": "Incorrect email address or password , Please try again"
}
```

```
{
  "Error": "Email and Password need to be provided."
}
```

#### 3. /users/A

* Methods: GET

* Description: Retrieves a list of all users, for Admins to look-upon, also displays admin information for all accounts

* Request Parameters: Capital letter A (Admin)

* Authentication: @jwt_required()

* Authorisation: Bearer token of admin_acc only

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

```
[
	{
		"admin_acc": false,
		"email": "sally@japantravel.com",
		"f_name": "Sally",
		"id": 1,
		"l_name": "Snowboarder",
		"username": "OyukiDaisuki"
	},
	{
		"admin_acc": false,
		"email": "bazza@email.com",
		"f_name": "Barry",
		"id": 2,
		"l_name": "Backpacker",
		"username": "EuroStar44"
	},
	{
		"admin_acc": false,
		"email": "vic@motobike.com",
		"f_name": "Victor",
		"id": 3,
		"l_name": "Vietnam",
		"username": "MotoManiac"
	},
	{
		"admin_acc": false,
		"email": "justbrowsing@gmail.com",
		"f_name": "Johnny",
		"id": 4,
		"l_name": "Commentalot",
		"username": "CommentKing"
	},
	{
		"admin_acc": true,
		"email": "undeleteable@admin.com",
		"f_name": "Admin",
		"id": 5,
		"l_name": "Administrator",
		"username": "SuperAdmin"
	}
]

```

* Error Handling:

Scenario: User isn't admin

Error Code: 401 UNAUTHORIZED

Error Message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 4. /users/user_id

* Methods: GET

* Description: Retrieves a list of all users information for the specified user

* Request Parameters: User id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of users ID or Admin

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

```

{
	"email": "bazza@email.com",
	"f_name": "Barry",
	"id": 2,
	"l_name": "Backpacker",
	"username": "EuroStar44"
}
```
* Error Handling:

Scenario: User trying to access another accounts 

Error Code: 401 UNAUTHORIZED

Error Message:

```
{
	"Error": "You are not authorized to access this information"
}
```

Scenario: User doesnt enter user_id integer or mis-types as letter 

Error Code: 404 NOT FOUND

Error Message:

```
{
	"Error": "Page not found, please try again"
}
```
#### 5. /users/user_id

* Methods: PUT, PATCH

* Description: Updating a user's information (except username)

* Request Parameters: User id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of users ID or Admin

* Request Body:

Requires some on the users details to update (including password)

```
{
	"f_name": "Baz"
}
```

* Request Response:

Status Code: 200 OK

```
{
	"admin_acc": false,
	"email": "bazza@email.com",
	"f_name": "Baz",
	"id": 2,
	"l_name": "Backpacker",
	"username": "EuroStar44"
}
```
* Error Handling:

Scenario: The User ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
	"Error": "User not found, please check ID"
}
```

Scenario: User isn't admin or the person they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```
#### 6. /users/user_id

* Methods: DELETE

* Description: Deletes a user and related details from the database

* Request Parameters: User id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of users ID or Admin

* Request Body: None

* Request Response: Status code 200 OK

* Error Handling: Same potential errors and messages as users update.

Scenario: The User ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
	"Error": "User not found, please check ID"
}
```

Scenario: User isn't admin or the person they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```

### Trip Routes

#### 1. /trips/A

* Methods: GET

* Description: Retrieves a list of all trips as well as there related Destinations. For Admins to monitor content.

* Request Parameters: Capital letter A (Admin)

* Authentication: @jwt_required()

* Authorisation: Bearer token of admin_acc only

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

* Please note only one example shown (original data very long)

```
[
	{
		"destinations": [
			{
				"continent": "Asia",
				"dest_country": "Vietnam",
				"dest_name": "Hanoi",
				"id": 10,
				"trip_id": 3
			},
			{
				"continent": "Asia",
				"dest_country": "Vietnam",
				"dest_name": "Bai Bien Vinh Thai beach",
				"id": 11,
				"trip_id": 3
			},
			{
				"continent": "Asia",
				"dest_country": "Vietnam",
				"dest_name": "Hue",
				"id": 12,
				"trip_id": 3
			},
			{
				"continent": "Asia",
				"dest_country": "Vietnam",
				"dest_name": "Hoi An",
				"id": 13,
				"trip_id": 3
			}
		],
		"estimated_budget": 2000,
		"finish_date": "2023-08-15",
		"id": 3,
		"start_date": "2023-08-10",
		"trip_desc": "Riding from Hanoi to Hoi An",
		"trip_name": "Vietnam on Motorbike",
		"user": {
			"username": "MotoManiac"
		}
	}
]
```

* Error Handling:

Scenario: User isn't admin

Error Code: 401 UNAUTHORIZED

Error Message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 2. /trips/user_id

* Methods: GET

* Description: Retrieves a list of all trips with associated destinations that have been created by a user. This will depict multiple tripsif the user has more than one.

* Request Parameters: user_id integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of user_id or admin_acc token

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

* Please note below, Username OyukiDaisuki has two trips.

```
[
	{
		"destinations": [
			{
				"continent": "Asia",
				"dest_country": "Japan",
				"dest_name": "Niseko Ski Resort",
				"id": 1,
				"trip_id": 1
			},
			{
				"continent": "Asia",
				"dest_country": "Japan",
				"dest_name": "Nozawa Onsen Ski Resort",
				"id": 2,
				"trip_id": 1
			},
			{
				"continent": "Asia",
				"dest_country": "Japan",
				"dest_name": "Tokyo",
				"id": 3,
				"trip_id": 1
			}
		],
		"estimated_budget": 7000,
		"finish_date": "2023-01-29",
		"id": 1,
		"start_date": "2023-01-15",
		"trip_desc": "Snowboarding in two resorts on the northern island of Hokkaido + a few days in Tokyo",
		"trip_name": "Winter Snowboarding + Tokyo",
		"user": {
			"username": "OyukiDaisuki"
		}
	},
	{
		"destinations": [
			{
				"continent": "NorthAmerica",
				"dest_country": "Canada",
				"dest_name": "La Crete",
				"id": 14,
				"trip_id": 4
			}
		],
		"estimated_budget": 6500,
		"finish_date": "2024-03-11",
		"id": 4,
		"start_date": "2024-02-04",
		"trip_desc": "Camping in the wilderness and hoping to see the Aurora Borealis",
		"trip_name": "Nothern Lights Trip",
		"user": {
			"username": "OyukiDaisuki"
		}
	}
]

```

* Error Handling:

Scenario: User doesnt enter user_id for example ... trips/

Error Code: 405 METHOD NOT ALLOWED

Error Message:
```
{
	"Error": "405 Method Not Allowed: The method is not allowed for the requested URL."
}
```

#### 3. /trips/user_id/trip_id

* Methods: GET

* Description: Retrieves a specific Trip of user. The trip the user has selected will display some activity information also.

* Request Parameters: user_id integer / trip_id integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of user_id or admin_acc token

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

* Please note below, this is Sally's (OyukiDaisuki) trip , so the URL http://127.0.0.1:8000/trips/1/4
which is = 1(Sallys user_id)/4(The Northern lights Trip trip_id)
```
{
	"destinations": [
		{
			"activities": [
				{
					"activity_desc": "Make a campfire everynight and wait for the Northern lights",
					"activity_name": "Camp and watch the Aurora Borealis",
					"budget": 500,
					"date_available": "Late August to mid April",
					"destination_id": 14,
					"id": 20
				}
			],
			"dest_country": "Canada",
			"dest_name": "La Crete",
			"id": 14,
			"trip_id": 4
		}
	],
	"estimated_budget": 6500,
	"finish_date": "2024-03-11",
	"id": 4,
	"start_date": "2024-02-04",
	"trip_desc": "Camping in the wilderness and hoping to see the Aurora Borealis",
	"trip_name": "Nothern Lights Trip"
}
```

* Error Handling:

Scenario: User enters an incorrect trip ID number

Error Code: 404 NOT FOUND

This error will display a more specific error message with information about the ID number received.

Error Message:
```
{
	"Error": "Trip ID 8 not found"
}
```

#### 4. /trips

* Methods: POST

* Description: Users create a new trip

* Request Parameters: None

* Authentication: @jwt_required

* Authorisation: Bearer token of user

* Request Body:

All Below Fields are required and using the bearer and token and get_jwt_identity method , the user_id field will be generated automatically. The users username will also be dispalyed.

```
{
 "trip_name" : "New Zealand South Island",
 "start_date" : "2024-07-31",
 "finish_date" : "2024-07-11",
 "estimated_budget" : 5000 ,
 "trip_desc": "Travelling, Snowboarding and meeting friends"
}
```

* Request Response:

Status code: 201 CREATED

```
{
	"estimated_budget": 5000,
	"finish_date": "2024-07-11",
	"id": 6,
	"start_date": "2024-07-31",
	"trip_desc": "Travelling, Snowboarding and meeting friends",
	"trip_name": "New Zealand South Island",
	"user": {
		"username": "OyukiDaisuki"
    }
}

```

* Error Handling:

Scenario: A required parameter is missing.

Error Code: 409 CONFLICT

This error will display a more specific error message with information about the ID number received.

Error Message:
```
{
	"Error": "Integrity Error, please check inputs and not already created"
}
```

Scenario: A user incorrectly writes a parameter

Error Code: 400 BAD REQUEST

Error Message:
```
{
	"Error": {
		"trip_nam": [
			"Unknown field."
		]
	}
}
```
Scenario: Incorrect Date Format is written

Error Code: 400 BAD REQUEST

Error Message:
```
{
	"Error": "Data formatted incorrectly, please check"
}
```


#### 5. /trips/trip_id

* Methods: PUT, PATCH

* Description: Updating the trip information and display any destination info also

* Request Parameters: Trip id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of users ID or admin_acc

* Request Body:

Requires some on the trip details to update.

```
{
    "trip_name" : "New Zealand North Island",
}
```

* Request Response:

Status Code: 200 OK

```
{
	"estimated_budget": 5000,
	"finish_date": "2024-07-11",
	"id": 6,
	"start_date": "2024-07-31",
	"trip_desc": "Travelling, Snowboarding and meeting friends",
	"trip_name": "New Zealand North Island"
	"user": {
		"username": "OyukiDaisuki"
	}
}
```
* Error Handling:

Scenario: The Trip ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
	"Error": "Trip 88 not found"
}
```

Scenario: User isn't owner/creator/admin of the trip they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```
#### 6. /trips/trip_id

* Methods: DELETE

* Description: Deletes a trip and all related details (Destination, Activities, Comments), if any from the database

* Request Parameters: Trip id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of users ID or Admin

* Request Body: None

* Request Response: Status code 200 OK

* Error Handling: Same potential errors and messages as trip update.

Scenario: The Trip ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
    "Error": "Trip {trip_id} not found"
}
```

Scenario: User isn't admin or the person they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```

### Destination Routes

#### 1. /destinations/A

* Methods: GET

* Description: Retrieves a list of all destinaions of all users, For Admins to monitor content. This content is public so its important an Authority can check , update and delete if necessary.

* Request Parameters: Capital letter A (Admin)

* Authentication: @jwt_required()

* Authorisation: Bearer token of admin_acc only

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK


```
[
	{
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Niseko Ski Resort",
		"id": 1,
		"trip_id": 1
	},
	{
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Nozawa Onsen Ski Resort",
		"id": 2,
		"trip_id": 1
	},
	{
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Tokyo",
		"id": 3,
		"trip_id": 1
	},
	{
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Bunol",
		"id": 4,
		"trip_id": 2
	},
	{
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Pamplona",
		"id": 5,
		"trip_id": 2
	},
	{
		"continent": "Europe",
		"dest_country": "France",
		"dest_name": "Chamonix",
		"id": 6,
		"trip_id": 2
	},
	{
		"continent": "Europe",
		"dest_country": "Italy",
		"dest_name": "Rome",
		"id": 7,
		"trip_id": 2
	},
	{
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Munich",
		"id": 8,
		"trip_id": 2
	},
	{
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Hohenschwangau",
		"id": 9,
		"trip_id": 2
	},
	{
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hanoi",
		"id": 10,
		"trip_id": 3
	},
	{
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Bai Bien Vinh Thai beach",
		"id": 11,
		"trip_id": 3
	},
	{
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hue",
		"id": 12,
		"trip_id": 3
	},
	{
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hoi An",
		"id": 13,
		"trip_id": 3
	},
	{
		"continent": "NorthAmerica",
		"dest_country": "Canada",
		"dest_name": "La Crete",
		"id": 14,
		"trip_id": 4
	}
]
```

* Error Handling:

Scenario: User (token) isn't admin

Error Code: 401 UNAUTHORIZED

Error Message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 2. /destinations/destination_id

* Methods: GET

* Description: Retrieves a list of the destination information associated with the ID number, It will also show acitivities related to the destination without comments for for readability and srictly organizational purposes.

* Request Parameters: destination_id integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of user_id or admin_acc token

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK


```
{
	"activities": [
		{
			"activity_desc": "Explore the resort and ride the backcountry",
			"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
			"activity_name": "Snowboarding Nozawa Onsen Resort",
			"budget": 1700,
			"date_available": "December to March",
			"destination_id": 2,
			"id": 3
		},
		{
			"activity_desc": "Use of the many free public baths to relax , post snowboarding",
			"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
			"activity_name": "Have an onsen in a Soto-yu",
			"budget": 0,
			"date_available": "Anytime",
			"destination_id": 2,
			"id": 4
		}
	],
	"continent": "Asia",
	"dest_country": "Japan",
	"dest_name": "Nozawa Onsen Ski Resort",
	"id": 2,
	"trip_id": 1
}

```

* Error Handling:

Scenario: User doesnt enter destination_id into URL, for example ... destinations/

Error Code: 405 METHOD NOT ALLOWED

Error Message:
```
{
	"Error": "405 Method Not Allowed: The method is not allowed for the requested URL."
}
```


#### 3. /destinations/

* Methods: POST

* Description: Users create a new destination for a trip

* Request Parameters: None

* Authentication: @jwt_required

* Authorisation: Bearer token of owner of Trip or an Admin

* Request Body:

All Below Fields are required., the trip_id field will checked against the Trip_ID's user token, meaning: Only the owner of the trip or the admin can add a destination to the trip.

```
{ 
"dest_country": "Japan",
"dest_name": "Kamakura",
"continent": "Asia",
"trip_id": 1
}
```

* Request Response:

Status code: 201 CREATED

```
{
	"continent": "Asia",
	"dest_country": "Japan",
	"dest_name": "Kamakura",
	"id": 16,
	"trip_id": 1
}
```

* Error Handling:

Scenario: A required parameter is missing.

Error Code: 409 CONFLICT

This error will display a more general error message with information about the ID number received.

Error Message:
```
{
	"Error": "Integrity Error, please check inputs and not already created"
}
```

Scenario: A user tries to add to a Trip they do not own or the Trip_id does not exist.

Error Code: 401 UNAUTHROIZED

Error Message:
```
{
	"Error": "Invalid trip ID or unauthorized access"
}
```
Scenario: A user tries to enter a continent ,outside the accepted values.

Error Code: 409 CONFLICT

Error Message:
```
{
	"Error": {
		"continent": [
			"Must be one of: NorthAmerica, SouthAmerica, Asia, Oceania, Europe, Africa, Antartica."
		]
	}
}
```

#### 4. /destinations/destination_id

* Methods: PUT, PATCH

* Description: Updating the destination information.

* Request Parameters: Destination id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of the Trip IDs owner (user_id) or admin_acc

* Request Body:

Requires some on the trip details to update. If the same details are entered, no change will occur.

```
{ 
"dest_country": "Japan",
"dest_name": "Yokohama",
"continent": "Asia",
}
```

* Request Response:

Status Code: 200 OK

```
{
	"continent": "Asia",
	"dest_country": "Japan",
	"dest_name": "Yokohama",
	"id": 15,
	"trip_id": 1
}
```
* Error Handling:

Scenario: The destination ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
	"Error": "Destination ID: 48 not found"
}
```

Scenario: User isn't owner/admin of the trip they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```
Scenario: Additional field is added.

Error code: 409 CONFLICT

Error message:
```
{
	"Error": {
		"City": [
			"Unknown field."
		]
	}
}
```

#### 5. /destinations/destination_id

* Methods: DELETE

* Description: Deletes a Destination and all related details (Activities, Comments), if any from the database

* Request Parameters: Trip id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of the Trip IDs owner (user_id) or admin_acc

* Request Body: None

* Request Response: Status code 200 OK
```
{
	"Success": "Destination ID: 15 and all related Activities deleted"
}
```

* Error Handling: Same potential errors and messages as destination update (Authorization and Incorrect ID).

Scenario: The Destination ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
    "Error": "Destination 88 not found"
}
```

Scenario: User isn't owner/admin of the destination they are trying to delete

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```

### Activity Routes

#### 1. /activities/A

* Methods: GET

* Description: Retrieves a list of all Activities of all users, For Admins to monitor content. This content is public so its important an Authority can check and delete if necessary.

* Request Parameters: Capital letter A (Admin)

* Authentication: @jwt_required()

* Authorisation: Bearer token of admin_acc only

* Request Body: None

* Request Response: 22

HTTP Status Code: 200 OK


```
[
	{
		"activity_desc": "Explore the resort and riding from the peak to the bottom",
		"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
		"activity_name": "Snowboarding Niseko resort",
		"budget": 2000,
		"date_available": "December to April",
		"destination_id": 1,
		"id": 1
	},
	{
		"activity_desc": "Rent snowshoes/poles and and a guide to take us to the top to ride down",
		"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
		"activity_name": "Hike Mt Yotei",
		"budget": 500,
		"date_available": "Late January, Early February (best time)",
		"destination_id": 1,
		"id": 2
	},
	{
		"activity_desc": "Explore the resort and ride the backcountry",
		"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
		"activity_name": "Snowboarding Nozawa Onsen Resort",
		"budget": 1700,
		"date_available": "December to March",
		"destination_id": 2,
		"id": 3
	},
	{
		"activity_desc": "Use of the many free public baths to relax , post snowboarding",
		"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
		"activity_name": "Have an onsen in a Soto-yu",
		"budget": 0,
		"date_available": "Anytime",
		"destination_id": 2,
		"id": 4
	},
	{
		"activity_desc": "Go to as many bars as possible and meet new people",
		"activity_location_URL": "https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA",
		"activity_name": "Drinking in Golden Gai, Shinjuku",
		"budget": 200,
		"date_available": "Anytime",
		"destination_id": 3,
		"id": 5
	},
	{
		"activity_desc": "Walk around and look for some crazy fashion to buy",
		"activity_location_URL": "https://maps.app.goo.gl/K4uuJJYzsR9ek8Fh9",
		"activity_name": "Shopping in Harajuku",
		"budget": 500,
		"date_available": "Anytime",
		"destination_id": 3,
		"id": 6
	},
	{
		"activity_desc": "Throw tomatoes at everyone",
		"activity_location_URL": "https://maps.app.goo.gl/gkoE1mjfwye2wAjF8",
		"activity_name": "Joining La Tomatina Festival",
		"budget": 200,
		"date_available": "Late August",
		"destination_id": 4,
		"id": 7
	},
	{
		"activity_desc": "Join one of the daily bull runs and run around in the stadium with bulls",
		"activity_location_URL": "https://maps.app.goo.gl/ECajwSUKBF1Bq9zY7",
		"activity_name": "Run with Bulls",
		"budget": 150,
		"date_available": "July 7th - 14th",
		"destination_id": 5,
		"id": 8
	},
	{
		"activity_desc": "Join the festival and get amognst the festivities",
		"activity_location_URL": "https://maps.app.goo.gl/uFgp5LcguFTFnM1f7",
		"activity_name": "The San Fermin Festival opening ceremony",
		"budget": 120,
		"date_available": "July 6th",
		"destination_id": 5,
		"id": 9
	},
	{
		"activity_desc": "Try a lot of wines, foods and watch live music",
		"activity_location_URL": "https://maps.app.goo.gl/X9yzp921LR7uMCuV8",
		"activity_name": "Chamonix Jazz Music Festival",
		"budget": 300,
		"date_available": "22nd July to 29th July",
		"destination_id": 6,
		"id": 10
	},
	{
		"activity_desc": "Do the coleseum tour and eat and drink afterwards",
		"activity_location_URL": "https://maps.app.goo.gl/ajUedXi4puh2fGeT7",
		"activity_name": "Visit the coleseum",
		"budget": 330,
		"date_available": "Anytime",
		"destination_id": 7,
		"id": 11
	},
	{
		"activity_desc": "Buy and wear traditional clothes, try at least three different beer tents",
		"activity_location_URL": "https://maps.app.goo.gl/qUGNxXha6GBBifM88",
		"activity_name": "Join the Oktoberfest Beer Festival",
		"budget": 450,
		"date_available": "Mid September until the first Sunday of October",
		"destination_id": 8,
		"id": 12
	},
	{
		"activity_desc": "Go to the original location for the festival, drink beer and try the pork-knuckle",
		"activity_location_URL": "https://maps.app.goo.gl/t1WUTGm58fXPG22D9",
		"activity_name": "Visit original Hof Brau Haus",
		"budget": 70,
		"date_available": "Anytime",
		"destination_id": 8,
		"id": 13
	},
	{
		"activity_desc": "Go on a tour of the Neuscwanstein Castle",
		"activity_location_URL": "https://maps.app.goo.gl/XPuQrZLhW1rdUyZz8",
		"activity_name": "Visit the inspiration for the Disney Castle",
		"budget": 120,
		"date_available": "Anytime",
		"destination_id": 9,
		"id": 14
	},
	{
		"activity_desc": "Buy tickets for the show in central Hanoi",
		"activity_location_URL": "https://maps.app.goo.gl/57rr6wfoyJTuk98x8",
		"activity_name": "See water puppet show",
		"budget": 20,
		"date_available": "Anytime",
		"destination_id": 10,
		"id": 15
	},
	{
		"activity_desc": "Walk around the markets, bars and restaurants around central Hanoi",
		"activity_location_URL": "https://maps.app.goo.gl/oWWij22p9awGZZQe8",
		"activity_name": "Wander around Hanoi city",
		"budget": 60,
		"date_available": "Anytime",
		"destination_id": 10,
		"id": 16
	},
	{
		"activity_desc": "Stop off and spend some time relaxing",
		"activity_location_URL": "https://maps.app.goo.gl/XdfBCrXYfUKgvGyy8",
		"activity_name": "Visit the Beach and Swim",
		"budget": 20,
		"date_available": "Anytime",
		"destination_id": 11,
		"id": 17
	},
	{
		"activity_desc": "Walk around the park, climb on the attractions, take some cool photos",
		"activity_location_URL": "https://maps.app.goo.gl/u4cmPtRF4C2nqHv6A",
		"activity_name": "Hue abondoned Water Park",
		"budget": 10,
		"date_available": "Anytime",
		"destination_id": 12,
		"id": 18
	},
	{
		"activity_desc": "Stroll through Hoi an, take in the atmosphere and eat Banh Mi",
		"activity_location_URL": "https://maps.app.goo.gl/ayM4FLZUnqoseNjE6",
		"activity_name": "Watch the lanterns being lit on the river at the night market",
		"budget": 50,
		"date_available": "Anytime",
		"destination_id": 13,
		"id": 19
	},
	{
		"activity_desc": "Make a campfire everynight and wait for the Northern lights",
		"activity_location_URL": "https://maps.app.goo.gl/ZKrMLLTLNWz99WET6",
		"activity_name": "Camp and watch the Aurora Borealis",
		"budget": 500,
		"date_available": "Late August to mid April",
		"destination_id": 14,
		"id": 20
	}
]
```

* Error Handling:

Scenario: User (token) isn't admin

Error Code: 401 UNAUTHORIZED

Error Message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 2. /activities/activity_id

* Methods: GET

* Description: Retrieves a list of the Activity information associated with the ID number, It will also show acitivities related to the destination without comments for for readability and srictly organizational purposes.

* Request Parameters: destination_id integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of owner of Destination (In-turn owner of Trip the token user) or an Admin

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK


```
{
	"activity_desc": "Go to as many bars as possible and meet new people",
	"activity_location_URL": "https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA",
	"activity_name": "Drinking in Golden Gai, Shinjuku",
	"budget": 200,
	"date_available": "Anytime",
	"destination_id": 3,
	"id": 5
}
```

* Error Handling:

Scenario: User doesnt enter Activity Id into URL, for example ... activities/

Error Code: 405 METHOD NOT ALLOWED

Error Message:
```
{
	"Error": "405 Method Not Allowed: The method is not allowed for the requested URL."
}
```


#### 3. /activities/

* Methods: POST

* Description: Users create a new activity assigned to a destination.

* Request Parameters: None

* Authentication: @jwt_required

* Authorisation: Bearer token of owner of Destination (In-turn owner of Trip the token user) or an Admin

* Request Body:

Please see feilds below. The destination_id field will checked against the trip_ID's and user_id's token which need to match, meaning: Only the owner of the trip/destination or the admin can add an activity to a destination.

The feild "date_available" is not necessary and only specified for events at a particular time. If nothing is entered it will default to "Anytime".The feild "activity_location_URL" is also optional to add.


```
{ 

    "activity_desc": "Walk around the temple grounds, buy some souveineirs and try go inside the statue ",
    "activity_location_URL": "https://maps.app.goo.gl/x9zf22MePnxds4157",
    "activity_name": "See the Giant Buddha Statue ",
    "budget": 100,
    "destination_id": 16
}
```

* Request Response:

Status code: 201 CREATED

```
{
{
	"activity_desc": "Walk around the temple grounds, buy some souveineirs and try go inside the statue ",
	"activity_location_URL": "https://maps.app.goo.gl/x9zf22MePnxds4157",
	"activity_name": "See the Giant Buddha Statue ",
	"budget": 100,
	"date_available": "Anytime",
	"destination_id": 16,
	"id": 21
}
}
```

* Error Handling:

Scenario: A required parameter is missing.

Error Code: 409 CONFLICT

This error will display a more general error message with information about the ID number received.

Error Message:
```
{
	"Error": "Integrity Error, please check inputs and not already created"
}
```

Scenario: A user tries to add to a Destination they do not own or the destination_id does not exist.

Error Code: 401 UNAUTHROIZED

Error Message:
```
{
	"Error": "Invalid destination ID or unauthorized access"
}
```
Scenario: A user tries to type an activity_name or activity_description that is too long.

Error Code: 400 BAD REQUEST

Error Message:
```
{
	"Error": "Data formatted incorrectly, please check"
}
```
Scenario: A user tries to enter an activity_location_URL that isnt from google maps and short-formed.

Error Code: 409 CONFLICT

Error Message:
```
{
	"Error": {
		"activity_location_URL": [
			"Invalid URL format, please only use Google Maps, Short URL"
		]
	}
}
```

#### 4. /activities/activity_id

* Methods: PUT, PATCH

* Description: Updating the activity information

* Request Parameters: Activity Id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of owner of Destination (In-turn owner of Trip and the token user) or an Admin

* Request Body:

Requires some on the trip details to update. If the same details are entered, no change will occur.

```
{ 
		"activity_desc": "Walk around the temple grounds, buy ALOT OF souveineirs and try go inside the statue",
		"budget": 300,

}
```

* Request Response:

Status Code: 200 OK

```
{
	"activity_desc": "Walk around the temple grounds, buy ALOT OF souveineirs and try go inside the statue",
	"activity_location_URL": "https://maps.app.goo.gl/x9zf22MePnxds4157",
	"activity_name": "See the Giant Buddha Statue ",
	"budget": 300,
	"date_available": "Anytime",
	"destination_id": 16,
	"id": 22
}
```
* Error Handling:

Scenario: The activity ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
	"Error": "Activity ID : 88 not found"
}
```

Scenario: User isn't owner/admin of the activity they are trying to update

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 5. /activities/activity_id

* Methods: DELETE

* Description: Deletes an Activity and all related details (Comments), if any from the database

* Request Parameters: Activity Id, integer

* Authentication: @jwt_required()

* Authorisation: Bearer token of owner of Destination (In-turn owner of Trip and the token user) or an Admin

* Request Body: None

* Request Response: Status code 200 OK
```
{
	"Success": "Activity ID: 21 and all related Activities deleted"
}
```

* Error Handling: Same potential errors and messages as Activity delete (Authorization and Incorrect ID).

Scenario: The Destination ID in URL doesnt exist

Error code: 404 NOT FOUND

Error message:

```
{
    "Error": "Activity ID:  88 not found"
}
```

Scenario: User isn't owner/admin of the activity they are trying to delete

Error code: 401 UNAUTHORIZED

Error message:
```
{
	"Error": "You are not authorized to access this information"
}
```

#### 6. /activities/public

* Methods: GET

* Description: Retrieves a list of all created Activitys with their destinations. It will hide budget information but display comments on each Activity and the commenters username. This is for the public and account holders to get ideas and entice them to sign up and comment or create a trip.

* Request Parameters: just the word /public

* Authentication: None

* Authorisation: None

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK


```
[
	{
		"activities": [
			{
				"activity_desc": "Explore the resort and riding from the peak to the bottom",
				"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
				"activity_name": "Snowboarding Niseko resort",
				"comments": [
					{
						"activity_id": 1,
						"message": "This resort is so crowded 😮",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 1,
						"message": "Its not as crowded in late January.",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "December to April",
				"destination_id": 1,
				"id": 1
			},
			{
				"activity_desc": "Rent snowshoes/poles and and a guide to take us to the top to ride down",
				"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
				"activity_name": "Hike Mt Yotei",
				"comments": [
					{
						"activity_id": 2,
						"message": "Seems fun, Can you recommmend a guide?",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Late January, Early February (best time)",
				"destination_id": 1,
				"id": 2
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Niseko Ski Resort",
		"id": 1
	},
	{
		"activities": [
			{
				"activity_desc": "Explore the resort and ride the backcountry",
				"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
				"activity_name": "Snowboarding Nozawa Onsen Resort",
				"comments": [],
				"date_available": "December to March",
				"destination_id": 2,
				"id": 3
			},
			{
				"activity_desc": "Use of the many free public baths to relax , post snowboarding",
				"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
				"activity_name": "Have an onsen in a Soto-yu",
				"comments": [
					{
						"activity_id": 4,
						"message": "My favorite onsen was Ogama, its the oldest and biggest?",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 2,
				"id": 4
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Nozawa Onsen Ski Resort",
		"id": 2
	},
	{
		"activities": [
			{
				"activity_desc": "Go to as many bars as possible and meet new people",
				"activity_location_URL": "https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA",
				"activity_name": "Drinking in Golden Gai, Shinjuku",
				"comments": [
					{
						"activity_id": 5,
						"message": "Im going Golden Gai tomorrow night , Whats the best bar for sake? 🍶",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 5,
						"message": "Try this one ...https://maps.app.goo.gl/2RfcE5WScpHyqWMq8",
						"user": {
							"username": "OyukiDaisuki"
						}
					},
					{
						"activity_id": 5,
						"message": "Thanks! 🙏",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 3,
				"id": 5
			},
			{
				"activity_desc": "Walk around and look for some crazy fashion to buy",
				"activity_location_URL": "https://maps.app.goo.gl/K4uuJJYzsR9ek8Fh9",
				"activity_name": "Shopping in Harajuku",
				"comments": [
					{
						"activity_id": 6,
						"message": "Cant miss this , Its a must-do in Tokyo",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 3,
				"id": 6
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Tokyo",
		"id": 3
	},
	{
		"activities": [
			{
				"activity_desc": "Throw tomatoes at everyone",
				"activity_location_URL": "https://maps.app.goo.gl/gkoE1mjfwye2wAjF8",
				"activity_name": "Joining La Tomatina Festival",
				"comments": [
					{
						"activity_id": 7,
						"message": "Dont wear anything valuable and wear goggles 🍅",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Late August",
				"destination_id": 4,
				"id": 7
			}
		],
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Bunol",
		"id": 4
	},
	{
		"activities": [
			{
				"activity_desc": "Join one of the daily bull runs and run around in the stadium with bulls",
				"activity_location_URL": "https://maps.app.goo.gl/ECajwSUKBF1Bq9zY7",
				"activity_name": "Run with Bulls",
				"comments": [
					{
						"activity_id": 8,
						"message": "If your not into running and danger, the bars and parties after the run are great!",
						"user": {
							"username": "MotoManiac"
						}
					}
				],
				"date_available": "July 7th - 14th",
				"destination_id": 5,
				"id": 8
			},
			{
				"activity_desc": "Join the festival and get amognst the festivities",
				"activity_location_URL": "https://maps.app.goo.gl/uFgp5LcguFTFnM1f7",
				"activity_name": "The San Fermin Festival opening ceremony",
				"comments": [
					{
						"activity_id": 9,
						"message": "Best atmoshphere Ive been in. Try the sangria !!",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "July 6th",
				"destination_id": 5,
				"id": 9
			}
		],
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Pamplona",
		"id": 5
	},
	{
		"activities": [
			{
				"activity_desc": "Try a lot of wines, foods and watch live music",
				"activity_location_URL": "https://maps.app.goo.gl/X9yzp921LR7uMCuV8",
				"activity_name": "Chamonix Jazz Music Festival",
				"comments": [
					{
						"activity_id": 10,
						"message": "Wheres a good place to stay for the festival?",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 10,
						"message": "You should stay around Cham Sud, theres a lot of good hotels there!",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "22nd July to 29th July",
				"destination_id": 6,
				"id": 10
			}
		],
		"continent": "Europe",
		"dest_country": "France",
		"dest_name": "Chamonix",
		"id": 6
	},
	{
		"activities": [
			{
				"activity_desc": "Do the coleseum tour and eat and drink afterwards",
				"activity_location_URL": "https://maps.app.goo.gl/ajUedXi4puh2fGeT7",
				"activity_name": "Visit the coleseum",
				"comments": [],
				"date_available": "Anytime",
				"destination_id": 7,
				"id": 11
			}
		],
		"continent": "Europe",
		"dest_country": "Italy",
		"dest_name": "Rome",
		"id": 7
	},
	{
		"activities": [
			{
				"activity_desc": "Buy and wear traditional clothes, try at least three different beer tents",
				"activity_location_URL": "https://maps.app.goo.gl/qUGNxXha6GBBifM88",
				"activity_name": "Join the Oktoberfest Beer Festival",
				"comments": [
					{
						"activity_id": 12,
						"message": "Dont ride the rollercoaster after beer 🤮",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Mid September until the first Sunday of October",
				"destination_id": 8,
				"id": 12
			},
			{
				"activity_desc": "Go to the original location for the festival, drink beer and try the pork-knuckle",
				"activity_location_URL": "https://maps.app.goo.gl/t1WUTGm58fXPG22D9",
				"activity_name": "Visit original Hof Brau Haus",
				"comments": [
					{
						"activity_id": 13,
						"message": "Do you need to make a reservation?",
						"user": {
							"username": "OyukiDaisuki"
						}
					},
					{
						"activity_id": 13,
						"message": "On the weekend, you might have to. Enjoy! 🍖 🍻?",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 8,
				"id": 13
			}
		],
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Munich",
		"id": 8
	},
	{
		"activities": [
			{
				"activity_desc": "Go on a tour of the Neuscwanstein Castle",
				"activity_location_URL": "https://maps.app.goo.gl/XPuQrZLhW1rdUyZz8",
				"activity_name": "Visit the inspiration for the Disney Castle",
				"comments": [
					{
						"activity_id": 14,
						"message": "Pretty Boring, Doest even look like the Disney Castle! 🙁",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 9,
				"id": 14
			}
		],
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Hohenschwangau",
		"id": 9
	},
	{
		"activities": [
			{
				"activity_desc": "Buy tickets for the show in central Hanoi",
				"activity_location_URL": "https://maps.app.goo.gl/57rr6wfoyJTuk98x8",
				"activity_name": "See water puppet show",
				"comments": [
					{
						"activity_id": 15,
						"message": "Amazing Show, You have to do this in Hanoi",
						"user": {
							"username": "MotoManiac"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 10,
				"id": 15
			},
			{
				"activity_desc": "Walk around the markets, bars and restaurants around central Hanoi",
				"activity_location_URL": "https://maps.app.goo.gl/oWWij22p9awGZZQe8",
				"activity_name": "Wander around Hanoi city",
				"comments": [
					{
						"activity_id": 16,
						"message": "Dont eat the fruit, it will make you sick",
						"user": {
							"username": "MotoManiac"
						}
					},
					{
						"activity_id": 16,
						"message": "Where did you buy the motorbike and around How much?",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 10,
				"id": 16
			}
		],
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hanoi",
		"id": 10
	},
	{
		"activities": [
			{
				"activity_desc": "Stop off and spend some time relaxing",
				"activity_location_URL": "https://maps.app.goo.gl/XdfBCrXYfUKgvGyy8",
				"activity_name": "Visit the Beach and Swim",
				"comments": [
					{
						"activity_id": 17,
						"message": "Water is not so clean, but a great spot for lunch",
						"user": {
							"username": "MotoManiac"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 11,
				"id": 17
			}
		],
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Bai Bien Vinh Thai beach",
		"id": 11
	},
	{
		"activities": [
			{
				"activity_desc": "Walk around the park, climb on the attractions, take some cool photos",
				"activity_location_URL": "https://maps.app.goo.gl/u4cmPtRF4C2nqHv6A",
				"activity_name": "Hue abondoned Water Park",
				"comments": [
					{
						"activity_id": 18,
						"message": "A real hidden gem",
						"user": {
							"username": "MotoManiac"
						}
					},
					{
						"activity_id": 18,
						"message": "Be careful after the rain, some of the structures are really slippery",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 12,
				"id": 18
			}
		],
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hue",
		"id": 12
	},
	{
		"activities": [
			{
				"activity_desc": "Stroll through Hoi an, take in the atmosphere and eat Banh Mi",
				"activity_location_URL": "https://maps.app.goo.gl/ayM4FLZUnqoseNjE6",
				"activity_name": "Watch the lanterns being lit on the river at the night market",
				"comments": [],
				"date_available": "Anytime",
				"destination_id": 13,
				"id": 19
			}
		],
		"continent": "Asia",
		"dest_country": "Vietnam",
		"dest_name": "Hoi An",
		"id": 13
	},
	{
		"activities": [
			{
				"activity_desc": "Make a campfire everynight and wait for the Northern lights",
				"activity_location_URL": "https://maps.app.goo.gl/ZKrMLLTLNWz99WET6",
				"activity_name": "Camp and watch the Aurora Borealis",
				"comments": [
					{
						"activity_id": 20,
						"message": "Its so beautiful , you need a real clear sky to see it",
						"user": {
							"username": "EuroStar44"
						}
					},
					{
						"activity_id": 20,
						"message": "I was there three days and missed it! hopefully you see it",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Late August to mid April",
				"destination_id": 14,
				"id": 20
			}
		],
		"continent": "NorthAmerica",
		"dest_country": "Canada",
		"dest_name": "La Crete",
		"id": 14
	}
]
```

* Error Handling:

Scenario: User doesnt enter URL correctly, for example ... /public*&^%

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": "Page not found, please try again"
}
```

#### 7. /activities/public/activity_id

* Methods: GET

* Description: Retrieves a specific created Activitys with its destinations. It will hide budget information and display comments on each Activity and the commenters username. Similiar to previous endpoint but easier to view information.

* Request Parameters: the word /public and Activity Id - Integer

* Authentication: None

* Authorisation: None

* Request Body: None

* Request Response: 

HTTP Status Code: 200 OK

```
{
	"activity_desc": "Explore the resort and riding from the peak to the bottom",
	"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
	"activity_name": "Snowboarding Niseko resort",
	"budget": 2000,
	"comments": [
		{
			"activity_id": 1,
			"message": "This resort is so crowded 😮",
			"user": {
				"username": "CommentKing"
			}
		},
		{
			"activity_id": 1,
			"message": "Its not as crowded in late January.",
			"user": {
				"username": "OyukiDaisuki"
			}
		}
	],
	"date_available": "December to April",
	"destination_id": 1,
	"id": 1
}

```

* Error Handling:

Scenario: enters an invalid Activity Id in URL

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": "No Result for this reference, please check again."
}
```

#### 8. /activities/public/country/dest_country

* Methods: GET

* Description: Retrieves a specific list of Activitys along with there destinations. It will hide budget information and display any comments on each Activity and the commenters username. The list of Activities shown is based off the name of the destination country

* Request Parameters: the words /public/country/ and then dest_country - String

* Authentication: None

* Authorisation: None

* Request Body: None

* Request Response: 

* For example the below pulls our recently created Trip/Destinaion/Activity along with list of activities from two different users under activties/public/country/Japan, as they both have Japan set as there dest_country.

HTTP Status Code: 200 OK

```
[
	{
		"activities": [
			{
				"activity_desc": "Explore the resort and riding from the peak to the bottom",
				"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
				"activity_name": "Snowboarding Niseko resort",
				"comments": [
					{
						"activity_id": 1,
						"message": "This resort is so crowded 😮",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 1,
						"message": "Its not as crowded in late January.",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "December to April",
				"destination_id": 1,
				"id": 1
			},
			{
				"activity_desc": "Rent snowshoes/poles and and a guide to take us to the top to ride down",
				"activity_location_URL": "https://maps.app.goo.gl/WN9YHnqVA7MSowBT8",
				"activity_name": "Hike Mt Yotei",
				"comments": [
					{
						"activity_id": 2,
						"message": "Seems fun, Can you recommmend a guide?",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Late January, Early February (best time)",
				"destination_id": 1,
				"id": 2
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Niseko Ski Resort",
		"id": 1
	},
	{
		"activities": [
			{
				"activity_desc": "Explore the resort and ride the backcountry",
				"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
				"activity_name": "Snowboarding Nozawa Onsen Resort",
				"comments": [],
				"date_available": "December to March",
				"destination_id": 2,
				"id": 3
			},
			{
				"activity_desc": "Use of the many free public baths to relax , post snowboarding",
				"activity_location_URL": "https://maps.app.goo.gl/xkqVSWxRvw1zS85W9",
				"activity_name": "Have an onsen in a Soto-yu",
				"comments": [
					{
						"activity_id": 4,
						"message": "My favorite onsen was Ogama, its the oldest and biggest?",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 2,
				"id": 4
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Nozawa Onsen Ski Resort",
		"id": 2
	},
	{
		"activities": [
			{
				"activity_desc": "Go to as many bars as possible and meet new people",
				"activity_location_URL": "https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA",
				"activity_name": "Drinking in Golden Gai, Shinjuku",
				"comments": [
					{
						"activity_id": 5,
						"message": "Im going Golden Gai tomorrow night , Whats the best bar for sake? 🍶",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 5,
						"message": "Try this one ...https://maps.app.goo.gl/2RfcE5WScpHyqWMq8",
						"user": {
							"username": "OyukiDaisuki"
						}
					},
					{
						"activity_id": 5,
						"message": "Thanks! 🙏",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 3,
				"id": 5
			},
			{
				"activity_desc": "Walk around and look for some crazy fashion to buy",
				"activity_location_URL": "https://maps.app.goo.gl/K4uuJJYzsR9ek8Fh9",
				"activity_name": "Shopping in Harajuku",
				"comments": [
					{
						"activity_id": 6,
						"message": "Cant miss this , Its a must-do in Tokyo",
						"user": {
							"username": "OyukiDaisuki"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 3,
				"id": 7
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Tokyo",
		"id": 3
	},
	{
		"activities": [
			{
				"activity_desc": "Walk around the temple grounds, buy some souveineirs and try go inside the statue",
				"activity_location_URL": "https://maps.app.goo.gl/x9zf22MePnxds4157",
				"activity_name": "See the Giant Buddha Statue",
				"comments": [],
				"date_available": "Anytime",
				"destination_id": 16,
				"id": 21
			}
		],
		"continent": "Asia",
		"dest_country": "Japan",
		"dest_name": "Kamakura",
		"id": 16
	}
]
```

* Error Handling:

Scenario: Country information cant be retrieved

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": "Country not found"
}
```

Scenario: URL address incorrect

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": "Page not found, please try again"
}
```


#### 8. /activities/public/continent/(continent_name)

* Methods: GET

* Description: Retrieves a specific list of Activitys along with there destinations. It will hide budget information and display any comments on each Activity and the commenters username. The list of Activities shown is based off the name of the continent

* Request Parameters: the words /public/continent/ and then continent - String

* Authentication: None

* Authorisation: None

* Request Body: None

* Request Response: 

* For example the below pulls a list of activities from two different users under activties/public/continent/Europe

HTTP Status Code: 200 OK

```
[
	{
		"activities": [
			{
				"activity_desc": "Throw tomatoes at everyone",
				"activity_location_URL": "https://maps.app.goo.gl/gkoE1mjfwye2wAjF8",
				"activity_name": "Joining La Tomatina Festival",
				"comments": [
					{
						"activity_id": 7,
						"message": "Dont wear anything valuable and wear goggles 🍅",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Late August",
				"destination_id": 4,
				"id": 7
			}
		],
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Bunol",
		"id": 4
	},
	{
		"activities": [
			{
				"activity_desc": "Join one of the daily bull runs and run around in the stadium with bulls",
				"activity_location_URL": "https://maps.app.goo.gl/ECajwSUKBF1Bq9zY7",
				"activity_name": "Run with Bulls",
				"comments": [
					{
						"activity_id": 8,
						"message": "If your not into running and danger, the bars and parties after the run are great!",
						"user": {
							"username": "MotoManiac"
						}
					}
				],
				"date_available": "July 7th - 14th",
				"destination_id": 5,
				"id": 8
			},
			{
				"activity_desc": "Join the festival and get amognst the festivities",
				"activity_location_URL": "https://maps.app.goo.gl/uFgp5LcguFTFnM1f7",
				"activity_name": "The San Fermin Festival opening ceremony",
				"comments": [
					{
						"activity_id": 9,
						"message": "Best atmoshphere Ive been in. Try the sangria !!",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "July 6th",
				"destination_id": 5,
				"id": 9
			}
		],
		"continent": "Europe",
		"dest_country": "Spain",
		"dest_name": "Pamplona",
		"id": 5
	},
	{
		"activities": [
			{
				"activity_desc": "Try a lot of wines, foods and watch live music",
				"activity_location_URL": "https://maps.app.goo.gl/X9yzp921LR7uMCuV8",
				"activity_name": "Chamonix Jazz Music Festival",
				"comments": [
					{
						"activity_id": 10,
						"message": "Wheres a good place to stay for the festival?",
						"user": {
							"username": "CommentKing"
						}
					},
					{
						"activity_id": 10,
						"message": "You should stay around Cham Sud, theres a lot of good hotels there!",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "22nd July to 29th July",
				"destination_id": 6,
				"id": 10
			}
		],
		"continent": "Europe",
		"dest_country": "France",
		"dest_name": "Chamonix",
		"id": 6
	},
	{
		"activities": [
			{
				"activity_desc": "Do the coleseum tour and eat and drink afterwards",
				"activity_location_URL": "https://maps.app.goo.gl/ajUedXi4puh2fGeT7",
				"activity_name": "Visit the coleseum",
				"comments": [],
				"date_available": "Anytime",
				"destination_id": 7,
				"id": 11
			}
		],
		"continent": "Europe",
		"dest_country": "Italy",
		"dest_name": "Rome",
		"id": 7
	},
	{
		"activities": [
			{
				"activity_desc": "Buy and wear traditional clothes, try at least three different beer tents",
				"activity_location_URL": "https://maps.app.goo.gl/qUGNxXha6GBBifM88",
				"activity_name": "Join the Oktoberfest Beer Festival",
				"comments": [
					{
						"activity_id": 12,
						"message": "Dont ride the rollercoaster after beer 🤮",
						"user": {
							"username": "CommentKing"
						}
					}
				],
				"date_available": "Mid September until the first Sunday of October",
				"destination_id": 8,
				"id": 12
			},
			{
				"activity_desc": "Go to the original location for the festival, drink beer and try the pork-knuckle",
				"activity_location_URL": "https://maps.app.goo.gl/t1WUTGm58fXPG22D9",
				"activity_name": "Visit original Hof Brau Haus",
				"comments": [
					{
						"activity_id": 13,
						"message": "Do you need to make a reservation?",
						"user": {
							"username": "OyukiDaisuki"
						}
					},
					{
						"activity_id": 13,
						"message": "On the weekend, you might have to. Enjoy! 🍖 🍻?",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 8,
				"id": 13
			}
		],
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Munich",
		"id": 8
	},
	{
		"activities": [
			{
				"activity_desc": "Go on a tour of the Neuscwanstein Castle",
				"activity_location_URL": "https://maps.app.goo.gl/XPuQrZLhW1rdUyZz8",
				"activity_name": "Visit the inspiration for the Disney Castle",
				"comments": [
					{
						"activity_id": 14,
						"message": "Pretty Boring, Doest even look like the Disney Castle! 🙁",
						"user": {
							"username": "EuroStar44"
						}
					}
				],
				"date_available": "Anytime",
				"destination_id": 9,
				"id": 14
			}
		],
		"continent": "Europe",
		"dest_country": "Germany",
		"dest_name": "Hohenschwangau",
		"id": 9
	},
	{
		"activities": [
			{
				"activity_desc": "Visiting the hundreds of bomb shelters and looking at butalist Yugo architecture",
				"activity_location_URL": "https://maps.app.goo.gl/WVbLfU9hzK5idHhk6",
				"activity_name": "Bussing Around Albania",
				"comments": [],
				"date_available": "Anytime",
				"destination_id": 15,
				"id": 21
			}
		],
		"continent": "Europe",
		"dest_country": "Albania",
		"dest_name": "Tirana",
		"id": 15
	}
]

```

* Error Handling:

Scenario: Country information cant be retrieved

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": " No activities in this Country as yet"
}
```

Scenario: URL address incorrect

Error Code: 404 NOT FOUND

Error Message:
```
{
	"Error": "Page not found, please try again"
}
```
