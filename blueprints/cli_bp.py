from init import db, bcrypt
from flask import Blueprint
from models.user import User
from models.trip import Trip
from models.destination import Destination
from models.activity import Activity
from models.comment import Comment

bp_DBCli = Blueprint('db',__name__ )

@bp_DBCli.cli.command('drop')
def drop():
    db.drop_all()
    print('All dropped')


@bp_DBCli.cli.command('create')
def db_drop_and_create():
    db.drop_all()
    db.create_all()
    print('Tables dropped + created successfully')

@bp_DBCli.cli.command('seed')
def seed_db():
    users = [
        User(
            username = "OyukiDaisuki",
            f_name = "Sally",
            l_name = "Snowboarder",
            email = "sally@japantravel.com",
            password=bcrypt.generate_password_hash('Iwannago2Japan').decode('utf-8')
        ),

        User(
            username = "EuroStar44",
            email = "Bazza@email.com",
            f_name = "Barry",
            l_name = "Backpacker",
            password= bcrypt.generate_password_hash('LetsgototoSpain22').decode('utf-8')
        ),

        User(
            username = "MotoManiac",
            f_name = "Victor",
            l_name = "Vietnam",
            email = "vic@motobike.com",
            password=bcrypt.generate_password_hash('HaybaiXiao3').decode('utf-8'),
        ),

        User(
            username = "CommentKing",
            f_name = "Johnny",
            l_name = "Commentalot",
            email = "justbrowsing@gmail.com",
            password=bcrypt.generate_password_hash('Ilovecommenting45').decode('utf-8'),
        ),
        User(
            username = "SuperAdmin",
            f_name = "Admin",
            l_name = "Administrator",
            email = "undeleteable@admin.com",
            password=bcrypt.generate_password_hash('Iloveadmin1234').decode('utf-8'),
            admin_acc = True
        )

    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    trips = [
        Trip(
            trip_name ="Winter Snowboarding + Tokyo",
            start_date = '2023/01/15',
            finish_date = '2023/1/29',
            estimated_budget = 7000,
            trip_desc = "Snowboarding in two resorts on the northern island of Hokkaido + a few days in Tokyo",
            user_id = users[0].id
        ),

        Trip(
            trip_name ="Backpacking Mainland Europe",
            start_date = '2023/07/15',
            finish_date = '2023/9/15',
            estimated_budget = 15000,
            trip_desc = "Spain, France, Italy and Germany - Festivals",
            user_id = users[1].id

        ),

        Trip(
            trip_name ="Vietnam on Motorbike",
            start_date = '2023/08/10',
            finish_date = '2023/08/15',
            estimated_budget = 2000,
            trip_desc = "Riding from Hanoi to Hoi An",
            user_id = users[2].id
        ),

        Trip(
            trip_name ="Nothern Lights Trip",
            start_date = '2024/02/4',
            finish_date = '2024/3/11',
            estimated_budget = 6500,
            trip_desc = "Camping in the wilderness and hoping to see the Aurora Borealis",
            user_id = users[0].id
        ),

        Trip(
            trip_name ="Paris Olympics",
            start_date = '2024/07/26',
            finish_date = '2024/8/11',
            estimated_budget = 20000,
            trip_desc = "Moving around Paris and seeing many events Games",
            user_id = users[3].id
        )
    ]
    db.session.query(Trip).delete()
    db.session.add_all(trips)
    db.session.commit()

    destinations = [

        Destination(
            dest_country = 'Japan',
            dest_name = 'Niseko Ski Resort',
            continent = 'Asia',
            trip_id = trips[0].id
        ),

        Destination(
            dest_country = 'Japan',
            dest_name = 'Nozawa Onsen Ski Resort',
            continent = 'Asia',
            trip_id = trips[0].id
        ),

        Destination(
            dest_country = 'Japan',
            dest_name = 'Tokyo',
            continent = 'Asia',
            trip_id = trips[0].id

        ),

        Destination(
            dest_country = 'Spain',
            dest_name = 'Bunol',
            continent = 'Europe',
            trip_id = trips[1].id

        ),

        Destination(
            dest_country = 'Spain',
            dest_name = 'Pamplona',
            continent = 'Europe',
            trip_id = trips[1].id

        ),
        Destination(
            dest_country = 'France',
            dest_name = 'Chamonix',
            continent = 'Europe',
            trip_id = trips[1].id

        ),

        Destination(
            dest_country = 'Italy',
            dest_name = 'Rome',
            continent = 'Europe',
            trip_id = trips[1].id

        ),

        Destination(
            dest_country = 'Germany',
            dest_name = 'Munich',
            continent = 'Europe',
            trip_id = trips[1].id
        ),

        Destination(
            dest_country = 'Germany',
            dest_name = 'Hohenschwangau',
            continent = 'Europe',
            trip_id = trips[1].id
        ),

        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hanoi',
            continent = 'Asia',
            trip_id = trips[2].id

        ),

        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Bai Bien Vinh Thai beach',
            continent = 'Asia',
            trip_id = trips[2].id
        ),

        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hue',
            continent = 'Asia',
            trip_id = trips[2].id

        ),

        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hoi An',
            continent = 'Asia',
            trip_id = trips[2].id
        ),

        Destination(
            dest_country = 'Canada',
            dest_name = 'La Crete',
            continent = 'NorthAmerica',
            trip_id = trips[3].id
        )
    ]

    db.session.query(Destination).delete()
    db.session.add_all(destinations)
    db.session.commit()
    
    activities = [

        Activity(
            activity_name = 'Snowboarding Niseko resort',
            activity_desc = 'Explore the resort and riding from the peak to the bottom',
            activity_location_URL = 'https://maps.app.goo.gl/WN9YHnqVA7MSowBT8',
            budget = 2000,
            date_available = "December to April",
            destination_id = destinations[0].id
        ),

        Activity(
            activity_name = 'Hike Mt Yotei',
            activity_desc = 'Rent snowshoes/poles and and a guide to take us to the top to ride down',
            activity_location_URL = 'https://maps.app.goo.gl/WN9YHnqVA7MSowBT8',
            budget = 500,
            date_available = "Late January, Early February (best time)",
            destination_id = destinations[0].id
        ),

        Activity(
            activity_name = 'Snowboarding Nozawa Onsen Resort',
            activity_desc = 'Explore the resort and ride the backcountry',
            activity_location_URL = 'https://maps.app.goo.gl/xkqVSWxRvw1zS85W9',
            budget = 1700,
            date_available = "December to March",
            destination_id = destinations[1].id
        ),

        Activity(
            activity_name = 'Have an onsen in a Soto-yu',
            activity_desc = 'Use of the many free public baths to relax , post snowboarding',
            activity_location_URL = 'https://maps.app.goo.gl/xkqVSWxRvw1zS85W9',
            budget = 0,
            destination_id = destinations[1].id
        ),

        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 200,
            destination_id = destinations[2].id
        ),

        Activity(
            activity_name = 'Shopping in Harajuku',
            activity_desc = 'Walk around and look for some crazy fashion to buy',
            activity_location_URL = 'https://maps.app.goo.gl/K4uuJJYzsR9ek8Fh9',
            budget = 500,
            destination_id = destinations[2].id
        ),

        Activity(
            activity_name = 'Joining La Tomatina Festival',
            activity_desc = 'Throw tomatoes at everyone',
            activity_location_URL = 'https://maps.app.goo.gl/gkoE1mjfwye2wAjF8',
            budget = 200,
            date_available = "Late August",
            destination_id = destinations[3].id
        ),

        Activity(
            activity_name = 'Run with Bulls',
            activity_desc = 'Join one of the daily bull runs and run around in the stadium with bulls',
            activity_location_URL = 'https://maps.app.goo.gl/ECajwSUKBF1Bq9zY7',
            budget = 150,
            date_available = "July 7th - 14th",
            destination_id = destinations[4].id
        ),

        Activity(
            activity_name = 'The San Fermin Festival opening ceremony',
            activity_desc = 'Join the festival and get amognst the festivities',
            activity_location_URL = 'https://maps.app.goo.gl/uFgp5LcguFTFnM1f7',
            budget = 120,
            date_available = "July 6th",
            destination_id = destinations[4].id
        ),

        Activity(
            activity_name = 'Chamonix Jazz Music Festival',
            activity_desc = 'Try a lot of wines, foods and watch live music',
            activity_location_URL = 'https://maps.app.goo.gl/X9yzp921LR7uMCuV8',
            budget = 300,
            date_available = "22nd July to 29th July",
            destination_id = destinations[5].id
        ),

        Activity(
            activity_name = 'Visit the coleseum',
            activity_desc = 'Do the coleseum tour and eat and drink afterwards',
            activity_location_URL = 'https://maps.app.goo.gl/ajUedXi4puh2fGeT7',
            budget = 330,
            destination_id = destinations[6].id
        ),

        Activity(
            activity_name = 'Join the Oktoberfest Beer Festival',
            activity_desc = 'Buy and wear traditional clothes, try at least three different beer tents',
            activity_location_URL = 'https://maps.app.goo.gl/qUGNxXha6GBBifM88',
            budget = 450,
            date_available = "Mid September until the first Sunday of October",
            destination_id = destinations[7].id
        ),

        Activity(
            activity_name = 'Visit original Hof Brau Haus',
            activity_desc = 'Go to the original location for the festival, drink beer and try the pork-knuckle',
            activity_location_URL = 'https://maps.app.goo.gl/t1WUTGm58fXPG22D9',
            budget = 70,
            destination_id = destinations[7].id
        ),

        Activity(
            activity_name = 'Visit the inspiration for the Disney Castle',
            activity_desc = 'Go on a tour of the Neuscwanstein Castle' ,
            activity_location_URL = 'https://maps.app.goo.gl/XPuQrZLhW1rdUyZz8',
            budget = 120,
            destination_id = destinations[8].id
        ),

        Activity(
            activity_name = 'See water puppet show',
            activity_desc = 'Buy tickets for the show in central Hanoi',
            activity_location_URL = 'https://maps.app.goo.gl/57rr6wfoyJTuk98x8',
            budget = 20,
            destination_id = destinations[9].id
        ),

        Activity(
            activity_name = 'Wander around Hanoi city',
            activity_desc = 'Walk around the markets, bars and restaurants around central Hanoi',
            activity_location_URL = 'https://maps.app.goo.gl/oWWij22p9awGZZQe8',
            budget = 60,
            destination_id = destinations[9].id
        ),
        
        Activity(
            activity_name = 'Visit the Beach and Swim',
            activity_desc = 'Stop off and spend some time relaxing',
            activity_location_URL = 'https://maps.app.goo.gl/XdfBCrXYfUKgvGyy8',
            budget = 20,
            destination_id = destinations[10].id
        ),
        
        Activity(
            activity_name = 'Hue abondoned Water Park',
            activity_desc = 'Walk around the park, climb on the attractions, take some cool photos',
            activity_location_URL = 'https://maps.app.goo.gl/u4cmPtRF4C2nqHv6A',
            budget = 10,
            destination_id = destinations[11].id
        ),
        
        Activity(
            activity_name = 'Watch the lanterns being lit on the river at the night market',
            activity_desc = 'Stroll through Hoi an, take in the atmosphere and eat Banh Mi',
            activity_location_URL = 'https://maps.app.goo.gl/ayM4FLZUnqoseNjE6',
            budget = 50,
            destination_id = destinations[12].id
        ),

        Activity(
            activity_name = 'Camp and watch the Aurora Borealis',
            activity_desc = 'Make a campfire everynight and wait for the Northern lights',
            activity_location_URL = 'https://maps.app.goo.gl/ZKrMLLTLNWz99WET6',
            budget = 500,
            date_available = "Late August to mid April",
            destination_id = destinations[13].id
        )
    ]

    db.session.query(Activity).delete()
    db.session.add_all(activities)
    db.session.commit()

    comments = [

        Comment(
            message = 'This resort is so crowded \U0001F62E',
            activity_id = activities[0].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'Its not as crowded in late January.',
            activity_id = activities[0].id,
            user_id =users[0].id
        ),

        Comment(
            message = 'Seems fun, Can you recommmend a guide?',
            activity_id = activities[1].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'My favorite onsen was Ogama, its the oldest and biggest?',
            activity_id = activities[3].id,
            user_id =users[0].id
        ),

        Comment(
            message = 'Im going Golden Gai tomorrow night , Whats the best bar for sake? \U0001F376',
            activity_id = activities[4].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'Try this one ...https://maps.app.goo.gl/2RfcE5WScpHyqWMq8',
            activity_id = activities[4].id,
            user_id =users[0].id
        ),

        Comment(
            message = 'Thanks! \U0001F64F',
            activity_id = activities[4].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'Cant miss this , Its a must-do in Tokyo',
            activity_id = activities[5].id,
            user_id =users[0].id
        ),

        Comment(
            message = 'Dont wear anything valuable and wear goggles \U0001F345',
            activity_id = activities[6].id,
            user_id =users[1].id
        ),

        Comment(
            message = 'If your not into running and danger, the bars and parties after the run are great!',
            activity_id = activities[7].id,
            user_id =users[2].id
        ),

        Comment(
            message = 'Best atmoshphere Ive been in. Try the sangria !!',
            activity_id = activities[8].id,
            user_id =users[1].id
        ),

        Comment(
            message = 'Wheres a good place to stay for the festival?',
            activity_id = activities[9].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'You should stay around Cham Sud, theres a lot of good hotels there!',
            activity_id = activities[9].id,
            user_id =users[1].id
        ),

        Comment(
            message = 'Dont ride the rollercoaster after beer \U0001F92E',
            activity_id = activities[11].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'Do you need to make a reservation?',
            activity_id = activities[12].id,
            user_id =users[0].id
        ),

        Comment(
            message = 'On the weekend, you might have to. Enjoy! \U0001F356 \U0001F37B?',
            activity_id = activities[12].id,
            user_id =users[1].id
        ),

        Comment(
            message = 'Pretty Boring, Doest even look like the Disney Castle! \U0001F641',   
            activity_id = activities[13].id,
            user_id =users[1].id,
        ),

        Comment(
            message = 'Amazing Show, You have to do this in Hanoi',
            activity_id = activities[14].id,
            user_id =users[2].id
        ),

        Comment(
            message = 'Dont eat the fruit, it will make you sick',
            activity_id = activities[15].id,
            user_id =users[2].id
        ),

        Comment(
            message = 'Where did you buy the motorbike and around How much?',
            activity_id = activities[15].id,
            user_id =users[3].id
        ),

        Comment(
            message = 'Water is not so clean, but a great spot for lunch',
            activity_id = activities[16].id,
            user_id =users[2].id
        ),

        Comment(
            message = 'A real hidden gem',
            activity_id = activities[17].id,
            user_id =users[2].id
        ),

        Comment(
            message = 'Be careful after the rain, some of the structures are really slippery',
            activity_id = activities[17].id,
            user_id =users[3].id
        ),

        Comment(

            message = 'Its so beautiful , you need a real clear sky to see it',
            activity_id = activities[19].id,
            user_id =users[1].id
        ),
        Comment(
            message = 'I was there three days and missed it! hopefully you see it',
            activity_id = activities[19].id,
            user_id =users[3].id
        )
    ]

    db.session.query(Comment).delete()
    db.session.add_all(comments)
    db.session.commit()
    print("Tables successfully seeded.")
