# T2A2 API Webserver - Travel Planner API
## Adam Hutt 
## Student Number - 14793

[Github Repository](https://github.com/huttadam/API-Webserver-Travel-Plan)

[Trello Board](https://trello.com/b/Sav7abed/api-webserver)

---

## Table of Contents

* [Installation and Setup Instructions](#installation-and-setup-instructions)
* [R1: Identify the problem](#r1---identify-the-problem-you-are-trying-to-solve-with-this-app)
* [R2: Justify the problem](#r2---why-is-it-a-problem-that-needs-solving-?)
* [R3: Database System Information](#r3---why-have-you-chosen-your-database-system-what-are-the-drawbacks-compared-to-others-?)
* [R4: ORM Functionalities and Benefits](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-ORM)
* [R5: API Endpoints](#r5-documenting-api-endpoints)
* [R6: ERD](#R6-ERD---Travel-Planner-API)
* [R7: Third Party Services](#r7-third-party-services-utilized)
* [R8: Models and Relationships](#R8-Describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
* [R9: Database Relations](#r9-discuss-the-database-relations-to-be-implemented-in-your-application)
* [R10: Planning and Tracking Task Progress](#r10-describe-the-way-tasks-are-allocated-and-tracked-in-your-project)
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

```flask db create``` Drops and creates all tables

```flask db seed``` Seeds the data into the created tables

```flask run``` Runs the application

If any errors occur during seed process, you can run the below also.

```flask db drop``` Only necessary , if issues during creation, to force dropping without creating.

The port has been set to 8000, please try connecting to http://127.0.0.1:8000/ via your browser, Insomnia or Hoppscotch

---

### R1 - Identify the problem you are trying to solve with this app

 The Tourism and Travel industries since the re-opening of countries borders for tourists since the COVID-19 pandemic are experiencing a a huge spike in popularity and income. These industries have always been strong and especially since the availability of the internet, it has made travel destinaton information a lot easier to access and utilize. The problem with all this new information is that it can be difficult to manage and keep track of what you actually want to do and where you want to go. There are so many travel blogs/vlogs to consume, planning and packing  before travelling that you can lose track of your goals before or on a trip.

 As a keen traveller myself, I have experienced a lot of frustration trying to gather information about an activity/monument/restaurant and if is acheiveable to visit when you are in the same city or country as it.  Whether your on a strict time-frame, jet-lagged or have lost a lot of time due to unforseen events, the frustration is compounded in trying to remember the crucial information about this activity. e.g. What website you your read about it?, What video you watched? Where exactly it was? Why was it special ? is it really worth it?  Its often that after I left left a destination,  I experience thoughts of .. I was supposed to go ... , Why didnt I see ... . 

 My API webserver attempts to solve this disorganization and stress revolved around travel and give the user the ability to track, add, sort, and update the information they have researched to ultimately improve the planning and decision-making around the travel experience and make the most of the users time travelling. In addition, the user is also able to gather ideas and be an inspiration for other users. The API webserver will have a feature for the public and account holders to view other users activities (minus personal information) and gather inspiration from them. Account holders are also able to leave comments on activities and gather additional information about potential activities.


 ### R2 - Why is it a problem that needs solving?

 As mentioned above having all the information about a travel destination is not benefitial for a person unless they can organize their plans, store information they have recieved which in-turn will really increase the likelihood of following through on these plans. 

 This is a problem that needs solving as , in todays economic climate , the cost of travelling and goods have increased rapidly and when people have the oppurtunity to travel, they need to ensure the time and money they are spending is not wasted. Furthermore,In terms of the public discussion feature, I believe there is space in the market amongst other huge online travel tools ,(Youtube (travel vlogs), TripAdvisor), for a user-based platform for travellers to gather information from other travellers. I feel advertisment money and big corporate companies give way to fake reviews which give users a biased or unfaithable depiction of what an acitivty or detination is actually.

In summary, the solving of this problem can save users a lot of time and exhaustion when travelling as well as act as a community sounding board for traveller and tourists to organize travel information and gather travel information, which ultimately leads to a better travel experience.


 ### R3 - Why have you chosen your database system, What are the drawbacks compared to others?

Databases are an essential feature for API webservers and the storing and management of data needs to be a process that is functional, flexible and tailored to my skill level. For my API travel planners database system I have selected PostgreSQL, which is a well-known,scalable, open-source and reputable database program which is utlized on a wide-range of applications throughout the I.T industry. Some reasons for my choice as follows

#### Contraints
A key feature of PostgreSQL are its contraints .In simple terms, contrainsts assist in controlling types of data with rules. Some examples of these contraints are foreign key constraints, unique constraints, and check constraints. These features help ensure data integrity is kept at the  database level, preventing the inserting of inconsistent or invalid data and keeping structing when deletions are made. In my API project, the ability to enforce and maintain data types, relationships between tables (Primary/Foreign Key) and integrity with contraints is a an essential factor for is functionality.


#### Robustness
PostgreSQL has a large set of features that can be used to facilitate multiple requirements. These features are attributed to the success and and popularity of PostgreSQL. An example of these features would be its ACID (Atomicity, Consistency, Isolation, Durability) complicance which simply means that data integrity is maintained during interactions with the database when most common mistakes or problems would occur.
Another feature to explain its robustness is MVCC (Multi-Version Concurrency Control) which improves performance especially in a multi-user database. While handling muitple transactions the database does not lock, it simultaneously processes the transactions and records these versions in-case a rollback or data integrity is compromised in any way.

#### Scalability
PostgreSQL is suited for large and small datasets. While starting off with a small dataset , as data grows and become more complicated , postgreSQL is able to support this growth and of course we can  adopt additional features to suite this change as required.


#### Compareable to other databases
As mentioned above, PostgreSQL has many benefits and well suited for my API project. However, when compared to other databases and their benfits, some noted drawbacks are noted when trying to acheive specfifc goals, these are as follows.

MySQL - Another database which uses SQL language. While not object relational like postgresql, MySQL has a smaller learning curve than PostgreSQL. As I am new to API's and manageing data the simpler syntax could be an added benefit for speed and going thorough a learning process. In addition to this, MySQL also utilizes cloud compatibility, which is attractive for projects/companies looking for the future and requiring a huge scaled database.

Oracle - A key featue of Oracle is it is a multi-model system. In simple terms this means that several applications utilise the same database and benefit from using the same models. Not only does this decrease workload but streamlines application building to suite a already designed database. 


### R4 - Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object-Relational Mapper) is a very poweful tool in programming. An ORM acts as the translater between the database and the programming language. The ORM enable the user to access the database from their preferred language rather than switch from one language to another. In the case of my API project we are communicating to the the database in a pythonic way to satisy postgreSQL database syntax.

#### Key functionalities of ORM

- Attributes from the database are mapped to programming language objects which gives the user a flexible interface to manipulate or view data from the database to a web application server.

- Data can be validated and handled through implementing rules, so data integrity errors or violations can be handled  graccefully using easier to understand language in error messages.

- Relationships between entities can be created and mapped from the ORM to the database. Relationships which are vital in the display and mangaing of data, these are relationships like  one to one , one to many etc. 

- CRUD operations are easily serviceable via an ORM , CRUD operations are essential in assisting with interactions from the client to the server in an API and form the bridge between them and the Database . For example the CRUD operations breakdown is as follows. 'C' in CRUD stands for Create, which services POST requests to the server, i.e adding data to the database, 'R' stands for Read which services GET requests to the server i.e. reading/acessing the information in the databse, 'U' stands for Update, which services PUT/PATCH requests to the server, i.e modifyiny/changing data in the database and finally 'D' stands for Delete which services DELETE requests to the server.

- Database queries can can be customized to pull data in a specific format to service specific requirements from the client side, for example , you want to access data from a certain date or a customer/product in the database starting with the letter 'Z'.

#### Benefits of an ORM

 As mentioned above, many of the ORM's features are core benefits of its use, however there are also some additional benefits to using an ORM.

 - The use of objects and function in programming language (OOP) or general python code allows us to create a general framework for queries, commands and routes, which means that code can be easily integrated to other applications with similiar database structures. Another key benefit of this is utilzing time to focus of the structure and function of the application rather than re-writing specific queries/commands.

 - Testing can be performed more easily in a programming languge which is essential for building applications for businesses which require a lot of evidence of testing and research to ensure the application is safe for public use and the protection of data for the business.

 - Communication and readability are keys benfits of ORM. This means we can actively control messages from the database and client/server to be readable for the ley-person. These messages can also greatly assist the developer in interpreting Database languages to something they can understand easier.


### R5 Documenting API Endpoints

API's documented on a seperate document due to size. Please click link below to see.

[Authentication routes endpoints](./docs/api_endpoints.md##travel-planner-api-routes)   


### R6 ERD - Travel Planner API

![ERD](./docs/ERDAPI.png)

### R7 Third party services utilized


#### Flask
Flask is a web framework program that provides the user multiple tools to build and facilitate web applications. It is well-known for being light-weight and flexible to the user. It achieves this by having the user import and integrate tools as needed from a large selection of features. This allows the user to operate in a very free way , without satisfying multiple requirements of tools that are not being used. It is designed to be a simple and scalable option for developers to efficiently create web applications. Throughtout my project I will be importing many modules and libraries from Flask.

#### SQLAlchemy
As discussed previously , part of my project will involve using a database to interact with and store and manage data. SQLAlchemy is a library in Python that facilitates this need. It is what was previously discussed in R4 ; an ORM (Object relational mapper). SQLAlchemy provides the user the tools to communicate and manage data in an SQL database in Pythonic language. So we get all the benefits of Python , objects, methods, function, automation , to manage our stored data within an SQL database and have it link to a web API server. SQLAlchemy streamlines the API creation and utlization process and allows as the handle SQL database interactions from a Python file.


#### PostgreSQL
PostgreSQL is a relational database management system that is scalable, flexible and efficient. We will use its features to create relationships between our entitites , facilitate data transactions and maintain data integrity throughout the project. As mentioned in R3 , Postgresql contains many features which have been utilised and due to its performance and scalability capabilities, my completed API project has room for growth.

#### Marshmallow
Marshmallow is a tool from both the Flask library and also the used from SQLAlchemy. It allows developers to validate complex data types into formats to use as required. In our case marshmallow is serializing data from our database along with SQLalchemy serialized and structured in Python language through a marshmallow feature called a schema. From this schema , we can receive the data as JSON and output when requested for API endpoints.


#### Psycopg2
In API's there needs to be a connection point from the Postgresql database. This function is performed by an adapter. Pyscopg2 is a popular Postgresql adapter for python that establishes the connection to the Postgresql database and facilitates data transactions performed by the ORM-SQlAlchemy and Python.


#### Bcrypt
A popular and widely used password hashing algoritihim , that will allow us to have the users password protected by encryption. The encryption is very complex and not only hides from potential threats but also from developers. The encrypted passwords will be stored within the database and accessed and stored as an encrypted hash.

#### JWT Manager
Authentication is required in the project to ensure users can keep their credentials/data safe from other users. JWT Manager is a python library that will utilizes JSON Web Tokens to ensure this happens. With this library we are able to create tokens and assign them to a variable that can is used as a represenatative of the token and authorizes or denies the user in the client/server communication process.

#### Trello
Trello is a project management web application that allows the user to create and customize tasks and assign them to certain stages. They provide a great visual representation of the project and help developers track progress of a project.

#### Insomnia
Insomnia is an API client and testing application that is used to test HTTP requests and recieve and debug the messages, for web API's in a controlled and safe environment.



### R8 Describe your projects models in terms of the relationships they have with each other

Below are the model classes representing the entities from the database and like all models in the project is written using SQLAlchemy and in a Python. By this it means that the columns represent the attributes in the database and vice versa. Generally to define an entity relationship or just create an attribute in the model, SQLAlchemy is used(db).

The db.Column object allows as to create the feilds in the entity and relevant relation information i.e assigning the attribute as a Primary key or as a foreign key. In the case of the forein key, its necessary to assign the original table and the column the key is from.

To establish the relationship the object db.relationship is assigned to a variable with the name of the relating entity, if the relationship is one to many , a plural is used to represent the many and singular for the one. We also add arguments to the object like back-populate which allows access to related columns from the related models. Two variables are created , one on each entity which shows the connection between the two and cascade represents the flow of the relationship if information is deleted it will also need to be deleted from the related model.


#### User Model

```py
class User(db.Model):
    __tablename__ = 'users'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    #Table Feilds
    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique = True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    admin_acc = db.Column(db.Boolean, default=False)

    #Relationships
    trips = db.relationship('Trip', back_populates='user', cascade= 'delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')



class UserSchema(ma.Schema):
    f_name = fields.String(validate=And(Length(min=1, error='Please enter at least one character.'), Regexp('^[a-zA-Z ]+$', error='Please enter letters only.')))
    l_name = fields.String(validate=And(Length(min=1, error='Please enter at least one character.'), Regexp('^[a-zA-Z ]+$', error='Please enter letters only.')))
    username = fields.String(validate= Regexp('^[a-zA-Z0-9_]{3,20}$', error = "Invalid username, Must be at least 3 Chars"))
    password = fields.String(validate= Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z\d@$#$^()!%*?&]{10,}$', error='Password must have a minimum of ten characters + At least one uppercase letter, lowercase letter and number'))
    email = fields.String(validate= Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', error = "Invalid Email address, please check and re-enter"))

    class Meta:
        fields = ("id", "username", "email", "password", "admin_acc", "f_name", "l_name")

```
This User model handles all information related to the user having an account. The User model has two relationships with other entities. Both relationships are back-popualated to the User model but foreign keys /attributes are not utilized on the model, only the other direction from the entity.

**Trip Model**

This relationship is one to many. A user can have multiple Trip models associated with it and a Trip can only have one user associated. The Trip model information back populates to the user, however no Trip infomation is utilized when serializing the User Schema with Marshmallow. The User attributes ID ( The primary key of the User model) is used to show ownership of the Trip as a ForeignKey on the Trip model.

**Comment Model**

The relationship is one to many, similarly to the relationship with the Trip model but in this case the User model's username is used as a ForeignKey in the Comment model rather than the User Id. This is done because as comments are public, some users do not want there name shown on the web, so an alias (username) is used instead. So a user can have multiple comments associated with them but a comment can only have one user associated.


#### Trip Model
```py
class Trip(db.Model):
    __tablename__ = 'trips'

    #Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Table Fields
    trip_name = db.Column(db.String(70), nullable=False, unique = True)
    start_date = db.Column(db.Date, nullable=False)
    finish_date = db.Column(db.Date, nullable=False)
    estimated_budget = db.Column(db.Integer, nullable=False)
    trip_desc = db.Column(db.Text, nullable=False)

    #Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   
    #Relationships
    user = db.relationship('User', back_populates='trips')
    destinations = db.relationship('Destination', back_populates='trip', cascade='all, delete')


class TripSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username'])
    destinations = fields.Nested('DestinationSchema', exclude=['activities'], many= True)

    class Meta:
        fields = ("id", "trip_name","start_date", "finish_date",'estimated_budget',"trip_desc","user", "destinations")

class FullTripSchema(ma.Schema):
    destinations = fields.Nested('DestinationSchema', many= True, exclude=['activities.activity_location_URL', 'continent'])

    class Meta:
        fields = ("id", "trip_name","start_date", "finish_date",'estimated_budget',"trip_desc", "destinations")
```
The Trip model is used to represent a overview of the trip planned by the user and includes information about what they are doing in a general sense. It contains some date inforamtion and budget info. You can notice that there are two schemas. TripSchema is for the user when creating/organizing the trip in their account and utilizes the relationship to depict the username. And the FullTripSchema is for displaying larger amount of data with destination info. The Trip model informationn as well as related destination information.

**User**

As mentioned previously the Trip model is the many part of the relationship in the one-to-many relationship. The Foreign Key in the Trip model is the User model's Id. It is a necessary field in the Trip model and has to be allocated to a User, symbolzing ownership. i.e The user plans/organizes the trip. What is also is important to note is that although back-populated the trip does not cascade backwards but forwards to the Destination Model.

**Destination**

The relationship with the Destination model is similar to the User > Trip relationship. It is one to many, the Trip model's Id attribute is the foreign key of the Destination model. So, a trip can have multiple Destinations but the destination is part of one trip. i.e You can go many places destinations on a trip but its regarded as one trip. Also, the cascade arguement is 'all, delete', which means that if the trip is deleted the destinations will also be deleted, maintaining data integrity.

#### Destination Model

```py

VALID_CONTINENTS = ("NorthAmerica", "SouthAmerica", "Asia", "Oceania", "Europe", "Africa", "Antartica")

class Destination(db.Model):
    __tablename__ = "destinations"

    #Primary key
    id = db.Column(db.Integer, primary_key=True)

    #Table Fields
    dest_country = db.Column(db.String(30), nullable = False)
    dest_name = db.Column(db.String(30), nullable = False)
    continent = db.Column(db.String(30), nullable = False)

    #Foreign Key
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    
    # Relationships
    trip = db.relationship('Trip', back_populates='destinations')
    activities = db.relationship('Activity', back_populates='destination', cascade='all, delete')
    

class DestinationSchema(ma.Schema):
    continent = fields.String(validate = OneOf(VALID_CONTINENTS), error = 'Continent can only be NorthAmerica, SouthAmerica, Asia, Oceania, Europe, Africa, Antartica')
    activities = fields.Nested('ActivitySchema', many = True, exclude=['comments'])


    class Meta:
        fields = ( "id","dest_country", "dest_name","continent","activities", "trip_id")

class DestinationPublicSchema(ma.Schema):
    activities = fields.Nested('ActivitySchema', many = True, exclude=['budget'])

    class Meta:
        fields = ( "id","dest_country", "dest_name", "activities", "continent")

```
The Destination model represents the countries, cities/locations and continents that will be visitied on the users trip. The destination model has two Schemas: The DestinationSchema is for handling/viewing just the destination information where as the DestinationPublicSchema is used to display at lot of information and excludes and includes specific information for this purpose. As you may begin to realize the relationship between the Models are quite similar, The model id becomes a foreign key on the next model and then that next model back populates with the former and share a one to many relationship. The relationships on the Destination model are as follows.

**Trip**

The Destination Model is the many part of the one-to-many relationship, so many destinations can be related to a Trip's Id.  The Trip information is back populated which means Trip info can be accessed and is utilized in the DestinationSchema and can related information can be displayed. The db.realtionship created with the Trip model also does not utilize the cascade arguement, meaning deletion will not flow backwards to the related Trip model if a Destination is deleted from the database.

**Activity**

The Activity model relationship with the Destination model is similar to the User > Trip relationship, Trip > Destination relationships. The Destination model relationship with the Activity model is a one to many relationship. So one destination can have multiple activities but every activity needs only one destination. A deletion of a destination will effect the activities related to it.

#### Activity Model

```py
class Activity(db.Model):
    __tablename__ = "activities"
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Table Fields
    activity_name = db.Column(db.String(100), nullable=False, unique = True)
    activity_location_URL = db.Column(db.String)
    budget = db.Column(db.Integer)
    date_available = db.Column(db.String(50), default= 'Anytime')
    activity_desc = db.Column(db.String(150), nullable=False)

    # Foreign Key
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
    
    #Relationships
    destination = db.relationship('Destination', back_populates='activities')
    comments = db.relationship('Comment', back_populates='activity', cascade= 'all, delete')
 

class ActivitySchema(ma.Schema):

    activity_location_URL = fields.Str(validate=Regexp("^https://maps\.app\.goo\.gl/[-a-zA-Z0-9@:%._+~#=]{1,256}$", error="Invalid URL format, please only use Google Maps, Short URL"))
    comments = fields.Nested('CommentSchema', many= True, exclude= ['id'])


    class Meta:
        fields = ("id","activity_name", "activity_location_URL", "budget", "activity_desc","date_available", "comments","destination_id")

```
The Activity model contains all activity information. It represents the things the user wants to do at the destination. The table fields are very open so, could be anything from a music festival, meeting a friend and trying a restaurant.In the Activity model the Schema displays some comment information from the Comment model as there is a relationship connection set-up. As you can see from previous models that the models are connected in sequence by one to many relationships. The activity model contains two relationships and a Foreign key relationship.

**Destination**
The destination id fom he Desination model is the foreign key associated withe Activity model. It acts as ownership of the activity , much like the User > Trip, Trip > Destination etc. The db.realtionship between these two are very useful for this API as it facilitates the public search GET requests. The user can search by Destination model dest_country or continent to pull a list of all matching activities.

**Comment**
The Comment model acts as the "child" in the one to many relationship meaning that the activity id is the foreign key assocated with the comment content. So the activity can have multiple comments but only one activity can be associated with one comment. Similar to previous models , comments also contain cascade. , Which means that the Activity/Comment models are associated with other models through the relationships that have with other models.

#### Comment Model

```py
class Comment(db.Model):
    __tablename__ = "comments"
    #Primary key
    id = db.Column(db.Integer, primary_key=True)
    #Table Feilds
    message= db.Column(db.String(200), nullable=False)
    #Foreign keys
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    #Relationships
    activity = db.relationship('Activity', back_populates='comments', cascade='all, delete')
    user = db.relationship('User', back_populates='comments')

 
class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ['username'])

    class Meta:
        fields = ("id","message","user","activity_id")

```
The Comment model simply represents the text, writing , questions etc that a user wants to write on their own or another users acitvity , for the public to see. It uses it relationship with the User model to utilize the users username as an identifier as to who wrote the comment. Similiar to social media sites a comment needs an author (username from User model), a message (the users message saved in the message field) and a place to write i.e people to see/react/reply (the Activity model). The comment model is slightly diffrent to previous models as this is where the cascade flow stops.

**Activity**
The activity is similar to previous relationships. The foreign key on this model represents the activity where the comment is placed. The actvity can host many comments , so this is the many side of the one to many relationship. The single/one side is represented by the comment, the single comment can only be hosted on one activity. Please note Activity also cascades , so if the User creates a Trip, some destinations, some activities and some people comment on these activities. If the user were to be deleted all this trip,destination, activity and comment data would follow with it, This ensures integrity in the database. 

**User**
The user foreign key on this model represents the user writing the comment. It is back populated to gather the information but cannot be cascaded to the User model. If this were to happen all models would be linked and deleting something , would result in all data in the database getting deleted. So the Comment model acts as an end to the cascading connection for deletion. This relation is also one to many as well, the Username (user) can write many comments but a comment can only have one writer (user).


In conclusion, below is a small visual depiction of the relationship cycle between the models.


User.id > Trip.id > Destination.id > Activity.id > Comment.id < User.username


### R9 Discuss the database relations to be implemented in your application

The relationships depicted in the User models are the same in nature but are displayed different in the database. As the ERD in R6 shows the lines linking the Primary keys and the foreign keys. The symbols of the end of these lines represent the nature of the the relationships. For my application the same type of relationship is used throughout the entities and this is the one to many relationship. This is depicted using the below. the left side represents one entity and the right side represents 0 or many that can be related with.

![crowsfoot](./docs/one%20to%20many.png)

#### Users and Trips
A user can have multiple trips or zero, (right) assigned to it and a Trip can only user one user (left). The User entity primary key "id" is the foreign key on the Trip entity. This depicts ownership on the trip. The user can own many trips or zero.

#### Trips and Destinations
A trip can have many destinatons, i.e you can  go many places on a holiday/trip , so similarly to the above. The Trip can be assigned to zero or many (right) destinations, But the destination can only be assigned to one trip. The primary key on Trip , the "id" entity is the foreign key on the destination entity. 
As you can see becuase User and Trip are realted and Trip and Dest are related. A user can be related to a destination. This is used throughout my model and really assists with authoristaion.

#### Destinations and Activities
At each detination , you have many things you want to do , but the acitivity can only be done in this destination (place). So the same relationship between is used to define them . One destination (left) can host many or zero activities (right). The primary key on Destination , the "id" entity is the foreign key on The activities entity. Similarly to the above the chain extends so User and Activity are defacto connected.

#### Activties and Comments
Each activity can have zero or many (right) comments assigned to it , but each unique comment can only have one activity (left) it is assigned to. Multiple instances can be displayed on an activity, but an acitvity cannot share a single comment. The activity entities primary key "id" is used as the foreign key on the comments entity.

#### Comments and Users
This relationship is different from the previous discussed. The comment entity has two foreign keys displayed. The first one is as expected, the activity id, depicting that the comment can be assigned to one activity (left) but the activity can have multiple or zero (right) comments assigned to it. 

So the attribute username from the users entity is a foreign key on the comments entity. The username depicts the author of the comment and their can only be one author for the comment. But the author can write several comments, so the author is the one (left) and the comment is the many or one (right) side of the relationship.


### R10 Describe the way tasks are allocated and tracked in your project

To track progress and monitor tasks throughtout my project, I used Trello , a project tracking web application. Trello allows customization and easy creation of tasks and subtasks which provide a clear picture of what needs to be done. Trello also allows deadlines and dates functions to track when certain tasks need to be completed by. I did not use this feature on this project as I wanted to explore options and different relationship/ entity set-ups and couldnt reallistically give a timeframe for this.

I found it extremely helpful to add tasks throughtout my project, at the beginning its hard to understand the scope of what needs to be and as you face this problems , I could easily create a task to remind myself to follow-up on or check. It can be very easy to get overwhelmed by visually seeing what needs to be completed and what needs to be tracked is a a really helpful tool.

The cards are placed into 4 categories, which represent what stage of the task you are currently at.  The stages I used were "backlog" (need to begin), "working", "Testing" and "Completed". When working on the project , I would consult the working section and move to the testing section for further checks. After there was nothing in the working section, I would begin a task from the backlog category. And of course after testing , I would move to the "Completed" category.

Below are some photos of the daily changes in the trello and the completed sub tasks list.

#### Daily Flow

![day1](./docs/Trello/day1%20-1.png)
![day1-2](./docs/Trello/day1%20-2.png)
![day2](./docs/Trello/day2%20-1.png)
![day3](./docs/Trello/day3%20-1.png)
![day4](./docs/Trello/day4%20-1.png)
![day5](./docs/Trello/day5%20-1.png)
![day6](./docs/Trello/day6%20-1.png)
![day7](./docs/Trello/day7%20-1.png)
![day8](./docs/Trello/day8%20-1.png)
![day9](./docs/Trello/day9%20-1.png)
![day10](./docs/Trello/day10%20-1.png)
![day11](./docs/Trello/day11%20-1.png)
![day12](./docs/Trello/day12%20-1.png)
![day13](./docs/Trello/day13%20-1.png)

#### Completed Subtasks

![st1](./docs/Trello/day4%20-2.png)
![st2](./docs/Trello/day4%20-3.png)
![st3](./docs/Trello/day6%20-3.png)
![st3](./docs/Trello/day13%20-2.png)


### References

About (no date) PostgreSQL. Available at: https://www.postgresql.org/about/ (Accessed: 16 December 2023). 

AltexSoft (2023) Database Management Systems (DBMS) comparison: Mysql, postgr, AltexSoft. Available at: https://www.altexsoft.com/blog/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/ (Accessed: 16 December 2023). 

Abba, I.V. (2022) What is an ORM – the meaning of object relational mapping database tools, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/ (Accessed: 16 December 2023). 

Password regex python (no date) Password regex Python | UI Bakery. Available at: https://uibakery.io/regex-library/password-regex-python (Accessed: 16 December 2023). 

Email regex python (no date) Email regex Python | UI Bakery. Available at: https://uibakery.io/regex-library/email-regex-python (Accessed: 16 December 2023). 

PSYCOPG 2.9.9 documentation (no date) Psycopg. Available at: https://www.psycopg.org/docs/ (Accessed: 16 December 2023). 

Rahman, Md.N. (2020) Flask with SQLAlchemy &amp; Marshmallow, Medium. Available at: https://medium.com/craftsmenltd/flask-with-sqlalchemy-marshmallow-2ec34ecfd9d4 (Accessed: 16 December 2023). 

Object–relational mapping (2023) Wikipedia. Available at: https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping (Accessed: 16 December 2023). 

What is Bcrypt and how it works? (2023) NordVPN. Available at: https://nordvpn.com/blog/what-is-bcrypt/ (Accessed: 16 December 2023). 

JWT-extended’s documentation¶ (no date) Flask. Available at: https://flask-jwt-extended.readthedocs.io/en/stable/ (Accessed: 16 December 2023). 

Simplified object serialization¶ (no date) marshmallow. Available at: https://marshmallow.readthedocs.io/en/stable/ (Accessed: 16 December 2023). 
